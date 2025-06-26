from typing import Any, Final, Type
import subprocess
from debug import DebugResult
from result import SolutionResult

__all__ = ("Language", "LangMap")

LangMap: dict[str, Type["Language"]] = {}

class Language:
    """이 문제의 풀이 언어를 나타내는 클래스입니다. 문제 풀이를 실행하고 그 결과를 반환하는 역할을 수행합니다."""
    ext: Final[str]
    
    def __init__(self, ext: str = ""):
        self.ext = ext
    
    @classmethod
    def __init_subclass__(cls, extension: str, **kwargs: Any):
        super().__init_subclass__(**kwargs)
        LangMap.update({extension: cls})
    
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

    def run_script(self, code_path: str, input: str, time_limit: float = 0.0) -> subprocess.CompletedProcess:
        """Run script with language.
        @param code_path: script file path.
        @param input: input data.
        @param time_limit: time limit for script.
        """
        raise NotImplementedError()     # Should be implemented per language.
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_benefit: bool = True) -> SolutionResult:
        """Run solution code with this language setting, then return the result as `SolutionResult`.

        Args:
            code_path (str): Path str for solution script.
            time_limit (float): Time limit for this problem. If exceeded, then result would be timeout.
                                If this language needs extra time, you can internally implement to calculate extra time.
            memory_limit (int): Memory usage limit for this problem. If exceeded, then result would be memory overflow.
                                If this language needs extra memory, you can internally implment to calculate extra memory limit.
            input (str): Input data to the solution. It is intended to receive single test case input.
            output (str): Output data to compare with solution's result. It is intended to receive single test case output.
            extra_benefit (bool): Flag value to use extra time & memory limit. Defaults to `True`.

        Returns:
            SolutionResult: Result data of this solution with given test case.
        """
        raise NotImplementedError()     # Should be implemented per language.
    
    def debug(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_benefit: bool = True) -> DebugResult:
        """Debug solution code with this language setting, then return the result as `SolutionResult`.

        Args:
            code_path (str): Path str for solution script.
            time_limit (float): Time limit for this problem. If exceeded, then result would be timeout.
                                If this language needs extra time, you can internally implement to calculate extra time.
            memory_limit (int): Memory usage limit for this problem. If exceeded, then result would be memory overflow.
                                If this language needs extra memory, you can internally implment to calculate extra memory limit.
            input (str): Input data to the solution. It is intended to receive single test case input.
            output (str): Output data to compare with solution's result. It is intended to receive single test case output.
            extra_benefit (bool): Flag value to use extra time & memory limit. Defaults to `True`.

        Returns:
            SolutionResult: Result data of this solution with given test case.
        """
        raise NotImplementedError()
    
    def __str__(self) -> str:
        """

        Returns:
            str: 이 언어 객체의 정보를 담은 문자열입니다.
        """
        return f"{self.__class__.__name__}<ext={self.ext}>"
