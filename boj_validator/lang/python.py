from typing import Final
import time
import subprocess
from resource import getrusage, RUSAGE_CHILDREN, struct_rusage
from debug import DebugResult
from result import SolutionResultType, SolutionResult
from .language import Language

class Python(Language, extension="py"):
    """
    Python language runner for solutions written in Python3.
    """

    @staticmethod
    def get_additional_time_limit(orignial_limit: float) -> float:
        return orignial_limit * 3 + 2
    
    @staticmethod
    def get_additional_memory_limit(orignial_limit: float) -> float:
        return orignial_limit * 3 + 128
    
    def __init__(self):
        super().__init__("py")

    def run_script(self, code_path: str, input: str, time_limit: float = 0.0) -> subprocess.CompletedProcess:
        """Run python script.
        @param code_path: python script file path.
        @param input: input data.
        @param time_limit: time limit for script.
        """
        if time_limit > 0:
            return self.run_subprocess(
                ["python", code_path],
                input=input,
                timeout=Python.get_additional_time_limit(time_limit)
            )
        else:
            return self.run_subprocess(
                ["python", code_path],
                input=input
            )

    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> SolutionResult:
        """Run python solution file.
        @param code_path: python script file path.
        @param time_limit: time limit for script.
        @param memory_limit: memory limit for script. If value is 0, then runner does not check memory usage.
        @param input: input data.
        @param output: output data.
        """
        try:
            before: float = time.time()
            res: subprocess.CompletedProcess = self.run_script(code_path, input, self.get_additional_time_limit(time_limit) if extra_time else time_limit)
            duration = time.time() - before
            res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
            # print(f"time: {res_info.ru_utime} (user) {res_info.ru_stime} (system) {res_info.ru_utime + res_info.ru_stime} (total)")
            # print(f"memory: {res_info.ru_maxrss} (max) {res_info.ru_ixrss} (shared) {res_info.ru_idrss} (unshared) {res_info.ru_isrss} (stack)")
            stdout = res.stdout.rstrip()
            if res.stderr is not None and res.stderr != "":
                return SolutionResult(SolutionResultType.RUNTIME_ERROR, stdout=stdout, stderr=res.stderr)
            if memory_limit > 0 and res_info.ru_maxrss // (1024 ** 2) > self.get_additional_memory_limit(memory_limit):
                return SolutionResult(SolutionResultType.MEMORY_OVERFLOW, memory=res_info.ru_maxrss)
            if stdout.count("\n") > output.count("\n"):
                return SolutionResult(SolutionResultType.OUTPUT_OVERFLOW, stdout=stdout)
            
            for i,(std_line, expected_line) in enumerate(zip(stdout, output)):
                if std_line.rstrip() != expected_line.rstrip():
                    return SolutionResult(SolutionResultType.INCORRECT, stdout=stdout, message=f"{i} 번째 줄의 출력이 다릅니다!:\nStdout:\n{std_line}\n\nAnswer:\n{expected_line}")
            
            return SolutionResult(SolutionResultType.CORRECT, time=duration, memory=res_info.ru_maxrss)
        except subprocess.TimeoutExpired:
            return SolutionResult(SolutionResultType.TIMEOUT)
    
    def debug(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> DebugResult:
        before: float = time.time()
        res: subprocess.CompletedProcess = self.run_script(code_path, input, self.get_additional_time_limit(time_limit) if extra_time else time_limit)
        duration = time.time() - before
        res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
        return DebugResult(stdout=res.stdout.rstrip(), stderr=res.stderr.rstrip(), time=duration, memory=res_info.ru_maxrss, message="디버그 결과를 확인하세요.")