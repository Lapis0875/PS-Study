__all__ = ("calculate_memory", )

FILE_SIZE_SUFFIX: tuple[str, str, str, str] = ("B", "KB", "MB", "GB")
def calculate_memory(mem: float) -> str:
    suffix: int = 0
    while mem > 1024:
        mem /= 1024
        suffix += 1
    
    return f"{mem:.4f}{FILE_SIZE_SUFFIX[suffix]}"