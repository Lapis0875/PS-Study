__all__ = ("DebugResult",)

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