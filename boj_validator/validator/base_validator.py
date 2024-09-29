from typing import Any, Final
from abc import ABCMeta
from os import listdir
from path_util import SolutionPath
from performance import calculate_memory
from lang.language import Language
from result import SolutionResult

__all__ = ("PSValidator",)

class PSValidator(metaclass=ABCMeta):
    dir_root: str
    path: SolutionPath
    lang: Final[Language]
    time_limit: float = 1.0     # 이 문제의 시간 제한
    memory_limit: int = 128     # 이 문제의 메모리 제한
    extra_time: bool            # 언어에 따라 추가 시간이 주어지는지에 대한 여부.
    inputs: list[str]
    outputs: list[str]
    
    @classmethod
    def __init_subclass__(cls, dir_root: str, **kwargs: Any):
        cls.dir_root = dir_root
    
    def __init__(self, lang: Language, time = 1.0, memory = 128, extra_time: bool = True):
        self.lang = lang
        self.time_limit = time
        self.memory_limit = memory
        self.extra_time = extra_time
        self.path = SolutionPath(self.dir_root)
        self.path.lang(lang.ext)

    def parse_question_data(self, question_id: int):
        """
        이 문제의 입출력 데이터를 불러옵니다.
        """
        case_path: str = self.path.question(question_id).cases
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
    
    """
    Solution Result Handling
    Custom PS Validators can override these methods to handle the results of the solution.
    They can define a new handler of certain result type by defining a method with the name of `_handle_{result_type}`.
    """
          
    def _handle_incorrect(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** Incorrect! **\n")
        print("Input:\n")
        print(input, end="\n\n")
        print("Answer:\n")
        print(f"```\n{expected_output}\n```", end="\n\n")
        print("Your Output:\n")
        print(f"```\n{solution_res.stdout}\n```", end="\n\n")
        print(f"\n\nMessage: {solution_res.message}")
    
    def _handle_output_overflow(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** Output Exceeded! **\n")
        print("Input:\n")
        print(input, end="\n\n")
        print("Answer:\n")
        print(f"```\n{expected_output}\n```", end="\n\n")
        print("Your Output:\n")
        print(f"```\n{solution_res.stdout}\n```", end="\n\n")
     
    def _handle_timeout(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** Timeout! **\n")
        print("Time Limit:")
        print(self.time_limit)
    
    def _handle_memory_overflow(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** Memory Overflow! **\n")
        print("Memory Limit:")
        print(self.time_limit)
        print("Used Memory (assummed):")
        print(solution_res.memory, end="\n\n")
    
    def _handle_runtime_error(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** Runtime Error **")
        print(solution_res.stderr, end="\n\n")
    
    def _handle_correct(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** Correct! **\n")
        print(f"Running Time : {solution_res.time:.4f}초")
        print(f"Memory Used : {calculate_memory(solution_res.memory)}")

    def print_case(self, input: str, expected_output: str, solution_res: SolutionResult):
        """
        특정 케이스의 실행 결과 정보를 출력합니다. 주로 예상한 출력과 실제 출력이 다름을 표시하기 위해 사용되는 메소드입니다.
        """
        print("=" * 20)
        getattr(self, f"_handle_{solution_res.res_type.name.lower()}")(input, expected_output, solution_res)
        print()     # 가독성을 위한 추가 개행

    def run(self):
        """해당 문제의 풀이 코드를 채점한다."""
        for idx, (input, output) in enumerate(zip(self.inputs, self.outputs)):
            res = self.lang.run(self.path.solution, self.time_limit, self.memory_limit, input, output, self.extra_time)
            print(f"{idx}: ")
            self.print_case(input, output, res)

    def debug(self):
        """해당 문제의 풀이 코드에 대해 테스트 케이스들을 모두 디버깅해 본다."""
        for idx, (input, output) in enumerate(zip(self.inputs, self.outputs)):
            res = self.lang.debug(self.path.solution, self.time_limit, self.memory_limit, input, output, self.extra_time)
            res.set_case_number(idx)
            print(res.info())

    def debug_case(self, case_number: int):
        """해당 문제의 풀이 코드에 대해 특정 테스트 케이스를 디버깅해 본다."""
        input = self.inputs[case_number]
        output = self.outputs[case_number]
        res = self.lang.debug(self.path.solution, self.time_limit, self.memory_limit, input, output, self.extra_time)
        res.set_case_number(case_number)
        print(res.info())
    
    def __str__(self) -> str:
        return f"PSValidator<lang={self.lang}>"