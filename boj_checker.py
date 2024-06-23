"""
One File Implementation of BOJ Checking Utiltiy.
@Copyright 2023
@Author Lapis0875
"""
from abc import ABCMeta
from enum import Enum
from os import listdir, mkdir
import subprocess
from resource import getrusage, RUSAGE_CHILDREN, struct_rusage
from typing import Final, Type
from functools import cached_property
import click
import time

FILE_SIZE_SUFFIX: tuple[str, str, str, str] = ("B", "KB", "MB", "GB")
def calculate_memory(mem: float) -> str:
    suffix: int = 0
    while mem > 1024:
        mem /= 1024
        suffix += 1
    
    return f"{mem:.4f}{FILE_SIZE_SUFFIX[suffix]}"

class ValidationResultType(Enum):
    CORRECT = SUCCESS = "맞았습니다"
    INCORRECT = FAIL = "틀렸습니다"
    TIMEOUT = "시간 초과"
    OUTPUT_OVERFLOW = "출력 초과"
    MEMORY_OVERFLOW = "메모리 초과"
    RUNTIME_ERROR = "런타임 에러"

class ValidationResult:
    """BOJ 문제 풀이의 결과를 나타내는 객체입니다."""
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

class DebugResult:
    """디버깅 결과를 나타내는 객체입니다."""
    input_case: int
    stdout: str
    stderr: str
    time: float
    memory: float
    message: str
    
    def __init__(self, stdout: str | None = None, stderr: str | None = None, time: float = 0.0, memory: float = 0.0, message: str | None = None):
        self.input_case = -1    # set later.
        self.stdout = stdout
        self.stderr = stderr
        self.time = time
        self.memory = memory
        self.message = message
    
    def set_case_number(self, case_number: int):
        """코드 실행 흐름을 일관되게 사용하기 위해, 입력 케이스의 번호는 나중에 입력받는다."""
        self.input_case = case_number
    
    def info(self) -> str:
        info_data: list[str] = [
            "# Debug for input case {self.input_case}",
            "[STDOUT]",
            *self.stdout.splitlines(),
            "\n",
            "[STDERR]",
            *self.stderr.splitlines(),
            "\n",
            "[TIME]",
            f"{self.time:.4f} sec",
            "\n",
            "[MEMORY]",
            calculate_memory(self.memory),
            "\n",
            "[COMMENT]",
            self.message,
        ]
        return "\n".join(info_data)
    
    def __str__(self) -> str:
        return self.info()

class Language(metaclass=ABCMeta):
    """이 문제의 풀이 언어를 나타내는 클래스입니다. 문제 풀이를 실행하고 그 결과를 반환하는 역할을 수행합니다."""
    ext: Final[str]
    
    def __init__(self, ext: str = ""):
        self.ext = ext
    
    def run_subprocess(self, args: list[str], *, input: str, timeout: float) -> subprocess.CompletedProcess:
        """주어진 인자로 서브프로세스를 실행하고, 그 결과를 반환합니다.
        
        Args:
            args (list[str]): 실행할 프로세스의 인자들입니다.
            timeout (float): 프로세스의 제한 시간입니다. 해당 BOJ 문제의 제한 시간을 사용합니다.

        Returns:
            subprocess.CompletedProcess: 완료된 자식 프로세스에 대한 객체.
        """
        return subprocess.run(
            args,
            text=True,
            encoding="utf-8",
            input=input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> ValidationResult:
        """이 언어의 실행 환경으로 BOJ의 풀이를 실행하고, 그 결과를 반환합니다.

        Args:
            code_path (str): 실행할 코드 파일의 상대 경로입니다.
            time_limit (float): 이 문제의 시간 제한입니다. 시간 초과를 일으키는 경우를 파악하기 위해 사용합니다.
                                일부 언어에 대해서는 문제의 시간 제한보다 실제 채점 제한이 더 여유로울 수 있습니다.
            memory_limit (int): 이 문제의 메모리 제한입니다. 메모리 초과를 일으키는 경우를 파악하기 위해 사용합니다.
                                일부 언어에 대해서는 문제의 시간 제한보다 실제 채점 제한이 더 여유로울 수 있습니다.
            input (str): 테스트 케이스의 입력입니다.
            output (str): 대조할 정답 출력입니다.

        Returns:
            ValidationResult: 실행 결과에 대한 분석입니다.
        """
        ...
    
    def debug(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> DebugResult:
        """이 언어의 실행 환경으로 BOJ의 풀이 코드를 디버깅하고, 그 결과를 반환합니다.

        Args:
            code_path (str): 실행할 코드 파일의 상대 경로입니다.
            time_limit (float): 이 문제의 시간 제한입니다. 시간 초과를 일으키는 경우를 파악하기 위해 사용합니다.
                                일부 언어에 대해서는 문제의 시간 제한보다 실제 채점 제한이 더 여유로울 수 있습니다.
            memory_limit (int): 이 문제의 메모리 제한입니다. 메모리 초과를 일으키는 경우를 파악하기 위해 사용합니다.
                                일부 언어에 대해서는 문제의 시간 제한보다 실제 채점 제한이 더 여유로울 수 있습니다.
            input (str): 테스트 케이스의 입력입니다.
            output (str): 대조할 정답 출력입니다.

        Returns:
            DebugRes: 디버그 결과에 대한 분석입니다.
        """
        raise NotImplementedError()     # 아직 대부분의 언어에서 구현되지 않은 상태입니다.
    
    def __str__(self) -> str:
        """디버깅을 위해 사용하는 문자열 변환 오버로딩입니다.

        Returns:
            str: 이 언어 객체의 정보를 담은 문자열입니다.
        """
        return f"{self.__class__.__name__}<ext={self.ext}>"

class Python(Language):
    """
    Python language runner for solutions written in Python3.
    """
    python_tle_ratio: Final[float] = 2.0    # python은 실제 채점 제한보다 여유가 있으므로, 실제 채점 제한보다 더 여유를 준다. 추정치이므로 실제와 다르다.
    python_mem_ratio: Final[float] = 2.0    # python은 실제 채점 제한보다 여유가 있으므로, 실제 채점 제한보다 더 여유를 준다. 추정치이므로 실제와 다르다.
    
    def __init__(self):
        super().__init__("py")
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> ValidationResult:
        try:
            before: float = time.time()
            res: subprocess.CompletedProcess = self.run_subprocess(
                ["python", code_path],
                input=input,
                timeout=time_limit*self.python_tle_ratio if extra_time else time_limit
            )
            duration = time.time() - before
            res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
            # print(f"time: {res_info.ru_utime} (user) {res_info.ru_stime} (system) {res_info.ru_utime + res_info.ru_stime} (total)")
            # print(f"memory: {res_info.ru_maxrss} (max) {res_info.ru_ixrss} (shared) {res_info.ru_idrss} (unshared) {res_info.ru_isrss} (stack)")
            stdout = res.stdout.rstrip()
            if res.stderr is not None and res.stderr != "":
                return ValidationResult(ValidationResultType.RUNTIME_ERROR, stdout=stdout, stderr=res.stderr)
            if res_info.ru_maxrss // (1024 ** 2) > (memory_limit*self.python_mem_ratio):
                return ValidationResult(ValidationResultType.MEMORY_OVERFLOW, memory=res_info.ru_maxrss)
            if stdout.count("\n") > output.count("\n"):
                return ValidationResult(ValidationResultType.OUTPUT_OVERFLOW, stdout=stdout)
            
            for i,(std_line, expected_line) in enumerate(zip(stdout, output)):
                if std_line.rstrip() != expected_line.rstrip():
                    return ValidationResult(ValidationResultType.INCORRECT, stdout=stdout, message=f"{i} 번째 줄의 출력이 다릅니다!:\nStdout:\n{std_line}\n\nAnswer:\n{expected_line}")
            
            return ValidationResult(ValidationResultType.CORRECT, time=duration, memory=res_info.ru_maxrss)
        except subprocess.TimeoutExpired:
            return ValidationResult(ValidationResultType.TIMEOUT)
    
    def debug(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> DebugResult:
        before: float = time.time()
        res: subprocess.CompletedProcess = self.run_subprocess(
            ["python", code_path],
            input=input,
            timeout=time_limit*self.python_tle_ratio if extra_time else time_limit
        )
        duration = time.time() - before
        res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
        return DebugResult(stdout=res.stdout.rstrip(), stderr=res.stderr.rstrip(), time=duration, memory=res_info.ru_maxrss, message="디버그 결과를 확인하세요.")

class C(Language):
    """
    C language runner for solutions written in Python3.
    """
    def __init__(self):
        super().__init__("c")
    
    def compile(self, directory: str, code_path: str) -> bool:
        res: subprocess.CompletedProcess = subprocess.run(
            ["clang", "-std=c11", code_path, "-o", f"{directory}/solution.out"],
            text=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return res.stderr is None or res.stderr == ""
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> ValidationResult:
        directory: str = code_path[:-len("solution.cpp")]
        if not self.compile(directory, code_path):
            return ValidationResult(ValidationResultType.RUNTIME_ERROR, message="컴파일에 실패했습니다.")
        try:
            before: float = time.time()
            res: subprocess.CompletedProcess = self.run_subprocess([f"{directory}/solution.out"], input=input, timeout=time_limit)
            duration = time.time() - before
            
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
            
            return ValidationResult(ValidationResultType.CORRECT, time=duration, memory=res_info.ru_maxrss)
        except subprocess.TimeoutExpired:
            return ValidationResult(ValidationResultType.TIMEOUT)
    
    def debug(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> DebugResult:
        directory: str = code_path[:-len("solution.cpp")]
        self.compile(directory, code_path)
        try:
            res: subprocess.CompletedProcess = self.run_subprocess([f"{directory}/solution.out"], input=input, timeout=time_limit)
            res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
            stdout = res.stdout.rstrip()
            stderr = res.stderr.rstrip()
            return DebugResult(stdout=stdout, stderr=stderr, time=res_info.ru_utime + res_info.ru_stime, memory=res_info.ru_maxrss, message="디버그 결과를 확인하세요.")
            
        except subprocess.TimeoutExpired:
            res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
            return DebugResult(stdout="(시간 초과로 인해 수집되지 않음)", stderr="(시간 초과로 인해 수집되지 않음)", time=time_limit, memory=res_info.ru_maxrss, message="30초를 넘어가는 경우 분석의 편의를 위해 강제 종료합니다.\n루프에 갇히는 경우가 있는지 확인하세요.")

class CPlusPlus(Language):
    """
    C++ language runner for solutions written in Python3.
    """
    def __init__(self):
        super().__init__("cpp")
    
    def compile(self, directory: str, code_path: str) -> bool:
        res: subprocess.CompletedProcess = subprocess.run(
            ["clang++", "-std=c++17", code_path, "-o", f"{directory}/solution.out"],
            text=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return res.stderr is None or res.stderr == ""
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> ValidationResult:
        directory: str = code_path[:-len("solution.cpp")]
        if not self.compile(directory, code_path):
            return ValidationResult(ValidationResultType.RUNTIME_ERROR, message="컴파일에 실패했습니다.")
        try:
            before: float = time.time()
            res: subprocess.CompletedProcess = self.run_subprocess([f"{directory}/solution.out"], input=input, timeout=time_limit)
            duration = time.time() - before
            
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
            
            return ValidationResult(ValidationResultType.CORRECT, time=duration, memory=res_info.ru_maxrss)
        except subprocess.TimeoutExpired:
            return ValidationResult(ValidationResultType.TIMEOUT)
    
    def debug(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> DebugResult:
        directory: str = code_path[:-len("solution.cpp")]
        self.compile(directory, code_path)
        try:
            res: subprocess.CompletedProcess = self.run_subprocess([f"{directory}/solution.out"], input=input, timeout=time_limit)
            res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
            stdout = res.stdout.rstrip()
            stderr = res.stderr.rstrip()
            return DebugResult(stdout=stdout, stderr=stderr, time=res_info.ru_utime + res_info.ru_stime, memory=res_info.ru_maxrss, message="디버그 결과를 확인하세요.")
            
        except subprocess.TimeoutExpired:
            res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
            return DebugResult(stdout="(시간 초과로 인해 수집되지 않음)", stderr="(시간 초과로 인해 수집되지 않음)", time=time_limit, memory=res_info.ru_maxrss, message="30초를 넘어가는 경우 분석의 편의를 위해 강제 종료합니다.\n루프에 갇히는 경우가 있는지 확인하세요.")

LangMap: dict[str, Type[Language]] = {
    "py": Python,
    "c": C,
    "cpp": CPlusPlus
}

class BOJValidator:
    boj_id: Final[int]
    lang: Final[Language]
    time_limit: float = 1.0     # 이 문제의 시간 제한
    memory_limit: int = 128     # 이 문제의 메모리 제한
    extra_time: bool            # 언어에 따라 추가 시간이 주어지는지에 대한 여부.
    inputs: list[str]
    outputs: list[str]
    
    def __init__(self, boj_id: int, lang: Language, time = 1.0, memory = 128, extra_time: bool = True):
        self.boj_id = boj_id
        self.lang = lang
        self.time_limit = time
        self.memory_limit = memory
        self.extra_time = extra_time
        
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
            res = self.lang.run(self.file_path, self.time_limit, self.memory_limit, input, output, self.extra_time)
            print(f"{idx}: ")
            self.print_case(input, output, res)

    def debug(self):
        """해당 문제의 풀이 코드에 대해 테스트 케이스들을 모두 디버깅해 본다."""
        for idx, (input, output) in enumerate(zip(self.inputs, self.outputs)):
            res = self.lang.debug(self.file_path, self.time_limit, self.memory_limit, input, output, self.extra_time)
            res.set_case_number(idx)
            print(res.info())

    def debug_case(self, case_number: int):
        """해당 문제의 풀이 코드에 대해 테스트 케이스들을 모두 디버깅해 본다."""
        input = self.inputs[case_number]
        output = self.outputs[case_number]
        res = self.lang.debug(self.file_path, self.time_limit, self.memory_limit, input, output, self.extra_time)
        res.set_case_number(case_number)
        print(res.info())
    
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
@click.argument("extra_time", type=click.BOOL, default=True)
def run(boj_number: int, lang_ext: str, time: float = 1.0, memory: int = 128, extra_time: bool = True):
    """CLI로 실행된 경우 수행할 코드."""
    lang: Language = LangMap[lang_ext]()
    validator = BOJValidator(boj_number, lang, time, memory, extra_time)
    validator.run()

@cli.command()
@click.argument("boj_number", type=click.INT)
@click.argument("lang_ext", type=click.STRING, default="cpp")
@click.argument("time", type=click.FLOAT, default=30.0)
@click.argument("memory", type=click.INT, default=1024)
@click.argument("extra_time", type=click.BOOL, default=True)
def debug(boj_number: int, lang_ext: str = "cpp", time: float = 30.0, memory: int = 1024, extra_time: bool = True):
    """디버그 함수. 현재 C++ 코드에 #define DEBUG를 추가하는 기능만 수행한다."""
    lang: Language = LangMap[lang_ext]()
    validator = BOJValidator(boj_number, lang, time, memory, extra_time)
    validator.debug()

@cli.command()
@click.argument("boj_number", type=click.INT)
@click.argument("lang_ext", type=click.STRING)
@click.argument("case_number", type=click.INT)
@click.argument("time", type=click.FLOAT, default=1.0)
@click.argument("memory", type=click.INT, default=128)
@click.argument("extra_time", type=click.BOOL, default=True)
def debug_case(boj_number: int, lang_ext: str, case_number: int, time: float, memory: int, extra_time: bool):
    """특정 케이스를 입력으로 해답 코드를 실행해본다."""
    lang: Language = LangMap[lang_ext]()
    validator = BOJValidator(boj_number, lang, time, memory, extra_time)
    validator.debug_case(case_number)

# 이 파이썬 코드가 python ~~.py 명령어로 실행된 파일일 때 (다른 파일에서 모듈로 불러와진 경우를 제외해준다)
if __name__ == "__main__":
    cli()
