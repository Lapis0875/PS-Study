from typing import Final
from os import listdir
from .performance import calculate_memory
from .language import Language
from .validation import ValidationResult, ValidationResultType

__all__ = ("BOJValidator", )

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

    def parse_question_data(self, question_id: int):
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
    
    def dir_path(self) -> str:
        """
        이 문제의 코드 경로를 반환합니다.
        """
        return f"./boj/{self.boj_id}/"
    
    def code_file(self) -> str:
        return f"solution.{self.lang.ext}"
    
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
