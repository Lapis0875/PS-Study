from typing import Final, Self

class SolutionPath:
    """
    Class for handling the path of the solution.
    Solution's path structure is fixed for this validator, so this class makes handling path easier.
    """
    root: Final[str]
    __lang_ext: str
    __question_id: int
    def __init__(self, root: str = "./boj/"):
        self.root = root
        self.__lang_ext = ""
        self.__question_id = -1
        self.__question_group = ""
    
    def lang(self, lang_ext: str) -> Self:
        self.__lang_ext = lang_ext
        return self
    
    def question(self, question_id: int) -> Self:
        self.__question_id = question_id
        self.__question_group = f"{self.__question_id // 1000:02d}XXX"
        return self

    @property
    def question_group(self) -> int:
        return self.__question_group
    
    @property
    def question_path(self):
        if self.__question_id == -1:
            raise ValueError("SolutionPath: question_id is not set!")
        return f"{self.root}/{self.__question_group}/{self.__question_id}"
    
    @property
    def cases(self):
        return f"{self.question_path}/cases/"
    
    @property
    def solution(self):
        if self.__lang_ext == "":
            raise ValueError("SolutionPath: lang_ext is not set!")
        return f"{self.question_path}/solution.{self.__lang_ext}"