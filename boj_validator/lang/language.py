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
    
    def run(self, code_path: str, time_limit: float, memory_limit: int, input: str, output: str, extra_time: bool = True) -> SolutionResult:
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
            SolutionResult: 실행 결과에 대한 분석입니다.
        """
        raise NotImplementedError()     # 언어별로 구현되어야 합니다.
    
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
