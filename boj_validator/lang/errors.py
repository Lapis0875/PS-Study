from typing import Final
from errors import BOJValidatorError

class LanguageRunnerError(BOJValidatorError):
    """Base Error class for Language-specific features."""
    lang_ext: Final[str]

    def __init__(self, lang_ext: str, msg: str):
        self.lang_ext = lang_ext
        super().__init__(msg)
    
    def __repr__(self) -> str:
        return f"BOJValidatorError::LanguageRunnerError"

class UnsupportedLanguageError(LanguageRunnerError):
    """Error raised when validator try to run unsupported(Not implemented in lang/) language file."""

    def __init__(self, lang_ext: str):
        super().__init__(lang_ext, f"{lang_ext} is not supported. If you need, please consider implementing {lang_ext} runner for yourself!")
    
    def __repr__(self) -> str:
        return f"BOJValidatorError::LanguageRunnerError::UnsupportedLanguageError"
