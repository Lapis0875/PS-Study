from performance import calculate_memory
from result import SolutionResult
from .base_validator import PSValidator

__all__ = ("BOJValidator", )

class BOJValidator(PSValidator, dir_root="boj"):
    """
    Solution Result Handling
    """
          
    def _handle_incorrect(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** 틀렸습니다 **\n")
        print("Input:\n")
        print(input, end="\n\n")
        print("Answer:\n")
        print(f"```\n{expected_output}\n```", end="\n\n")
        print("Your Output:\n")
        print(f"```\n{solution_res.stdout}\n```", end="\n\n")
        print(f"\n\nMessage: {solution_res.message}")
    
    def _handle_output_overflow(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** 출력 초과 **\n")
        print("Input:\n")
        print(input, end="\n\n")
        print("Answer:\n")
        print(f"```\n{expected_output}\n```", end="\n\n")
        print("Your Output:\n")
        print(f"```\n{solution_res.stdout}\n```", end="\n\n")
     
    def _handle_timeout(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** 시간 초과 **\n")
        print("제한 시간:")
        print(self.time_limit)
    
    def _handle_memory_overflow(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** 메모리 초과 **\n")
        print("제한 메모리:")
        print(self.time_limit)
        print("사용된 메모리:")
        print(solution_res.memory, end="\n\n")
    
    def _handle_runtime_error(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** 런타임 에러 **")
        print("Error:")
        print(solution_res.stderr, end="\n\n")
    
    def _handle_correct(self, input: str, expected_output: str, solution_res: SolutionResult):
        print("** 맞았습니다 **\n")
        print(f"실행 시간 : {solution_res.time:.4f}초")
        print(f"사용 메모리 : {calculate_memory(solution_res.memory)}")
    
    def __str__(self) -> str:
        return f"BOJ_Validator<lang={self.lang}>"
