from typing import Final
from errors import BOJValidatorError

class GeneratorError(BOJValidatorError):
    """Base Error class for Generator-specific features."""
    boj_id: Final[int]

    def __init__(self, boj_id: int, msg: str):
        self.boj_id = boj_id
        super().__init__(msg)
    
    def __repr__(self) -> str:
        return f"BOJValidatorError::GeneratorError"

class GeneratorNotFound(GeneratorError):
    """Error raised when there is no generator file available in solution directory."""

    def __init__(self, boj_id: int):
        super().__init__(boj_id, f"There is no generator scripts for BOJ {boj_id} exists.")
    
    def __repr__(self) -> str:
        return f"BOJValidatorError::GeneratorError::GeneratorNotFound"

class GeneratorForLangNotSupported(GeneratorError):
    """Error raised when generator of {lang_ext} is not exist in solution directory."""
    lang_ext: Final[str]

    def __init__(self, boj_id: int, lang_ext: str):
        super().__init__(boj_id, f"There is no generator scripts of language {lang_ext} for BOJ {boj_id} exists.")
    
    def __repr__(self) -> str:
        return f"BOJValidatorError::GeneratorError::GeneratorForLangNotSupported"
