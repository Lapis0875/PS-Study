from abc import ABCMeta
from enum import StrEnum
from os import listdir, mkdir
import sys
import subprocess
from resource import getrusage, RUSAGE_CHILDREN, struct_rusage
from typing import Final, Type
from functools import cached_property
import click

FILE_SIZE_SUFFIX: tuple[str, str, str, str] = ("B", "KB", "MB", "GB")
def calculate_memory(mem: float) -> str:
    suffix: int = 0
    while mem > 1024:
        mem /= 1024
        suffix += 1
    
    return f"{mem:.4f}{FILE_SIZE_SUFFIX[suffix]}"

class ValidationResultType(StrEnum):
    CORRECT = SUCCESS = "맞았습니다"
    INCORRECT = FAIL = "틀렸습니다"
    TIMEOUT = "시간 초과"
    OUTPUT_OVERFLOW = "출력 초과"
    MEMORY_OVERFLOW = "메모리 초과"
    RUNTIME_ERROR = "런타임 에러"

class ValidationResult:
    res_type: ValidationResultType
    stdout: str | None
    stderr: str | None
    time: float
    memory: float
    message: str | None
    
    def __init__(self, res_type: ValidationResultType, stdout: str | None = None, stderr: str | None = None, time: float = 0.0, memory: float = 0.0, message: str | None = None):
        self.res_type = res_type
        self.stdout = stdout
        self.stderr = stderr
        self.time = time
        self.memory = memory
        self.message = message
    
    def __repr__(self) -> str:
        return f"ValidationResult<type={self.res_type}, stdout={self.stdout}, stderr={self.stderr}, time={self.time}, memory={calculate_memory(self.memory)}>"
    
    def __str__(self) -> str:
        return self.res_type.value

class Language(metaclass=ABCMeta):
    ext: Final[str]
    
    def __init__(self, ext: str = ""):
        self.ext = ext
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str) -> ValidationResult:
        ...
    
    def __str__(self):
        return f"{self.__class__.__name__}<ext={self.ext}>"

class Python(Language):
    """
    Python language runner for solutions written in Python3.
    """
    def __init__(self):
        super().__init__("py")
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str) -> ValidationResult:
        try:
            res: subprocess.CompletedProcess = subprocess.run(
                ["python", code_path],
                text=True,
                encoding="utf-8",
                input=input,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=time_limit,
            )
            res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
            # print(f"time: {res_info.ru_utime} (user) {res_info.ru_stime} (system) {res_info.ru_utime + res_info.ru_stime} (total)")
            # print(f"memory: {res_info.ru_maxrss} (max) {res_info.ru_ixrss} (shared) {res_info.ru_idrss} (unshared) {res_info.ru_isrss} (stack)")
            stdout = res.stdout.rstrip()
            if res.stderr is not None and res.stderr != "":
                return ValidationResult(ValidationResultType.RUNTIME_ERROR, stdout=stdout, stderr=res.stderr)
            if res_info.ru_maxrss // (1024 ** 2) > memory_limit:
                return ValidationResult(ValidationResultType.MEMORY_OVERFLOW, memory=res_info.ru_maxrss)
            if stdout.count("\n") > output.count("\n"):
                return ValidationResult(ValidationResultType.OUTPUT_OVERFLOW, stdout=stdout)
            
            for i,(std_line, expected_line) in enumerate(zip(stdout, output)):
                if std_line.rstrip() != expected_line.rstrip():
                    return ValidationResult(ValidationResultType.INCORRECT, stdout=stdout, message=f"{i} 번째 줄의 출력이 다릅니다!:\nStdout:\n{std_line}\n\nAnswer:\n{expected_line}")
            
            return ValidationResult(ValidationResultType.CORRECT, time=res_info.ru_utime + res_info.ru_stime, memory=res_info.ru_maxrss)
        except subprocess.TimeoutExpired:
            return ValidationResult(ValidationResultType.TIMEOUT)

class C(Language):
    """
    C language runner for solutions written in Python3.
    """
    def __init__(self):
        super().__init__("c")

class CPlusPlus(Language):
    """
    C++ language runner for solutions written in Python3.
    """
    def __init__(self):
        super().__init__("cpp")

LangMap: dict[str, Type[Language]] = {
    "py": Python,
    "c": C,
    "cpp": CPlusPlus
}

class BOJValidator:
    boj_id: Final[int]
    lang: Final[Language]
    time_limit: float = 1.0         # time limit in seconds
    memory_limit: int = 128     # memory limit in megabytes
    inputs: list[str]
    outputs: list[str]
    
    def __init__(self, boj_id: int, lang: Language, time = 1.0, memory = 128):
        self.boj_id = boj_id
        self.lang = lang
        self.time_limit = time
        self.memory_limit = memory
        
        self.parse_question_data()

    def parse_question_data(self):
        """
        이 문제의 입출력 데이터를 불러옵니다.
        """
        case_path: str = self.dir_path + "cases/"
        cases: list[str] = listdir(case_path)
        cases.sort()

        self.inputs = []
        self.outputs = []
        for case in cases:
            if case.endswith(".in"):                    # input data
                with open(case_path + case, "r") as f:
                    self.inputs.append(f.read())
            elif case.endswith(".out"):                 # output data
                with open(case_path + case, "r") as f:
                    self.outputs.append(f.read())
        
        if len(self.inputs) != len(self.outputs):
            # input&output data does not match!
            print("** Warning **\nInput&Output data does not match! ")
            

    def print_case(self, input: str, expected_output: str, validation_res: ValidationResult):
        """
        특정 케이스의 실행 결과 정보를 출력합니다. 주로 예상한 출력과 실제 출력이 다름을 표시하기 위해 사용되는 메소드입니다.
        """
        print("=" * 20)
        match validation_res.res_type:
            case ValidationResultType.INCORRECT:
                print("** 틀렸습니다 **\n")
                print("Input:\n")
                print(input, end="\n\n")
                print("Answer:\n")
                print(f"```\n{expected_output}\n```", end="\n\n")
                print("Your Output:\n")
                print(f"```\n{validation_res.stdout}\n```", end="\n\n")
                print(f"\n\nMessage: {validation_res.message}")
            case ValidationResultType.OUTPUT_OVERFLOW:
                print("** 출력 초과 **\n")
                print("Input:\n")
                print(input, end="\n\n")
                print("Answer:\n")
                print(f"```\n{expected_output}\n```", end="\n\n")
                print("Your Output:\n")
                print(f"```\n{validation_res.stdout}\n```", end="\n\n")
            case ValidationResultType.TIMEOUT:
                print("** 시간 초과 **\n")
                print("제한 시간:")
                print(self.time_limit)
            case ValidationResultType.MEMORY_OVERFLOW:
                print("** 메모리 초과 **\n")
                print("제한 메모리:")
                print(self.time_limit)
                print("사용된 메모리:")
                print(validation_res.memory, end="\n\n")
            case ValidationResultType.RUNTIME_ERROR:
                print("** 런타임 에러 **")
                print("Error:")
                print(validation_res.stderr, end="\n\n")
            case ValidationResultType.CORRECT:
                print("** 맞았습니다 **\n")
                print(f"실행 시간 : {validation_res.time:.4f}초")
                print(f"사용 메모리 : {calculate_memory(validation_res.memory)}")
        print()     # 가독성을 위한 추가 개행
            
    
    @cached_property
    def dir_path(self) -> str:
        """
        이 문제의 코드 경로를 반환합니다.
        """
        return f"./boj/{self.boj_id}/"
    
    @cached_property
    def code_file(self) -> str:
        return f"solution.{self.lang.ext}"
    
    @cached_property
    def file_path(self) -> str:
        return f"{self.dir_path}{self.code_file}"

    def run(self):
        """해당 문제의 풀이 코드에 대해 테스트 케이스들을 모두 점검해 본다."""
        for idx, (input, output) in enumerate(zip(self.inputs, self.outputs)):
            res = self.lang.run(self.file_path, self.time_limit, self.memory_limit, input, output)
            print(f"{idx}: ")
            self.print_case(input, output, res)
    
    def __str__(self) -> str:
        return f"BOJ_Validator<boj_id={self.boj_id}, lang={self.lang}>"

# main.py

@click.group()
def cli(): pass

@cli.command()
@click.argument("boj_number", type=click.INT)
@click.argument("lang_ext", type=click.STRING)
def create(boj_number: int, lang_ext: str):
    mkdir(f"boj/{boj_number}")
    mkdir(f"boj/{boj_number}/cases")
    with (
        open(file=f"./boj/{boj_number}/solution.{lang_ext}", mode="w") as sol_file,
        open(file=f"./boj/templates/solution.{lang_ext}", mode="r") as template
    ):
        sol_file.write(template.read())
    print(f">>> Created new BOJ solution directory for boj{boj_number} with language {lang_ext}!")

@cli.command()
@click.argument("boj_number", type=click.INT)
@click.argument("lang_ext", type=click.STRING)
@click.argument("time", type=click.FLOAT, default=1.0)
@click.argument("memory", type=click.INT, default=128)
def run(boj_number: int, lang_ext: str, time: float = 1.0, memory: int = 128):
    """CLI로 실행된 경우 수행할 코드."""
    lang: Language = LangMap[lang_ext]()
    validator = BOJValidator(boj_number, lang, time, memory)
    validator.run()

# 이 파이썬 코드가 python ~~.py 명령어로 실행된 파일일 때 (다른 파일에서 모듈로 불러와진 경우를 제외해준다)
if __name__ == "__main__":
    cli()
