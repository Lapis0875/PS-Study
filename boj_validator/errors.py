__all__ = (
    "BojValidatorError",
)

class BOJValidatorError(Exception):
    """Base Error class for BOJ Validator module."""
    msg: str

    def __init__(self, msg: str) -> str:
        self.msg = msg


    def __str__(self) -> str:
        return self.msg
    
    def __repr__(self) -> str:
        return f"BOJValidatorError"