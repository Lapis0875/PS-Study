"""
BOJ Validator

A Simple Python CLI tool for checking test-cases & judging Problem-Solving solutions.
Especially for BOJ (Baekjoon Online Judge), but can be extended to other PS platforms.
"""
from .lang import Language, LangMap
from .result import SolutionResultType, SolutionResult
from .debug import DebugResult
from .tool import BOJValidator

__all__ = ("Language", "LangMap", "BOJValidator", "SolutionResultType", "SolutionResult", "DebugResult")

__version__= (2, 0, 0)      # major, minor, hotfix