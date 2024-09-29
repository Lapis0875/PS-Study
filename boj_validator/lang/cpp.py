import time
import subprocess
from resource import getrusage, RUSAGE_CHILDREN, struct_rusage
from debug import DebugResult
from result import SolutionResultType, SolutionResult
from .language import Language

class CPlusPlus(Language, extension="cpp"):
    """
    C++ language runner for solutions written in C++.
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
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> SolutionResult:
        directory: str = code_path[:-len("solution.cpp")]
        if not self.compile(directory, code_path):
            return SolutionResult(SolutionResultType.RUNTIME_ERROR, message="컴파일에 실패했습니다.")
        try:
            before: float = time.time()
            res: subprocess.CompletedProcess = self.run_subprocess([f"{directory}/solution.out"], input=input, timeout=time_limit)
            duration = time.time() - before
            
            res_info: struct_rusage = getrusage(RUSAGE_CHILDREN)
            # print(f"time: {res_info.ru_utime} (user) {res_info.ru_stime} (system) {res_info.ru_utime + res_info.ru_stime} (total)")
            # print(f"memory: {res_info.ru_maxrss} (max) {res_info.ru_ixrss} (shared) {res_info.ru_idrss} (unshared) {res_info.ru_isrss} (stack)")
            stdout = res.stdout.rstrip()
            if res.stderr is not None and res.stderr != "":
                return SolutionResult(SolutionResultType.RUNTIME_ERROR, stdout=stdout, stderr=res.stderr)
            if res_info.ru_maxrss // (1024 ** 2) > memory_limit:
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

