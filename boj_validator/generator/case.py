from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class Case:
    """Test case model."""
    boj_id: Final[int]
    input: Final[str]
    output: Final[str]