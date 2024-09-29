from enum import Enum
from performance import calculate_memory

__all__ = ("SolutionResultType", "SolutionResult")

class SolutionResultType(Enum):
    CORRECT = SUCCESS = "맞았습니다"
    INCORRECT = FAIL = "틀렸습니다"
    TIMEOUT = "시간 초과"
    OUTPUT_OVERFLOW = "출력 초과"
    MEMORY_OVERFLOW = "메모리 초과"
    RUNTIME_ERROR = "런타임 에러"

class SolutionResult:
    """BOJ 문제 풀이의 결과를 나타내는 객체입니다."""
    res_type: SolutionResultType
    stdout: str | None
    stderr: str | None
    time: float
    memory: float
    message: str | None
    
    def __init__(self, res_type: SolutionResultType, stdout: str | None = None, stderr: str | None = None, time: float = 0.0, memory: float = 0.0, message: str | None = None):
        self.res_type = res_type
        self.stdout = stdout
        self.stderr = stderr
        self.time = time
        self.memory = memory
        self.message = message
    
    def __repr__(self) -> str:
        return f"SolutionResult<type={self.res_type}, stdout={self.stdout}, stderr={self.stderr}, time={self.time}, memory={calculate_memory(self.memory)}>"
    
    def __str__(self) -> str:
        return self.res_type.value