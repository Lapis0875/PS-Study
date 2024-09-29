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
    python_tle_ratio: Final[float] = 2.0    # python은 실제 채점 제한보다 여유가 있으므로, 실제 채점 제한보다 더 여유를 준다. 추정치이므로 실제와 다르다.
    python_mem_ratio: Final[float] = 2.0    # python은 실제 채점 제한보다 여유가 있으므로, 실제 채점 제한보다 더 여유를 준다. 추정치이므로 실제와 다르다.
    
    def __init__(self):
        super().__init__("py")
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> SolutionResult:
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
                return SolutionResult(SolutionResultType.RUNTIME_ERROR, stdout=stdout, stderr=res.stderr)
            if res_info.ru_maxrss // (1024 ** 2) > (memory_limit*self.python_mem_ratio):
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
        res: subprocess.CompletedProcess = self.run_subprocess(
            ["python", code_path],
            input=input,
            timeout=time_limit*self.python_tle_ratio if extra_time else time_limit
        )
        duration = time.time() - before
        res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
        return DebugResult(stdout=res.stdout.rstrip(), stderr=res.stderr.rstrip(), time=duration, memory=res_info.ru_maxrss, message="디버그 결과를 확인하세요.")