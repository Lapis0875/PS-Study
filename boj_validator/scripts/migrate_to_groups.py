import os
import shutil
from pprint import pprint

from typing import Final, Self

class SolutionPath:
    """
    Class for handling the path of the solution.
    Solution's path structure is fixed for this validator, so this class makes handling path easier.
    """
    root: Final[str]
    __lang_ext: str
    __question_id: int
    def __init__(self, root: str):
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

def wrap_single_file_to_directory(filepath: str):
    """
    This function is used to wrap a single file into a directory structure.
    It creates a directory with the same name as the file (without extension) and moves the file into that directory.
    """
    filename, lang_ext = os.path.splitext(filepath)
    boj_id: int = int(filename.strip("boj"))
    p = SolutionPath("./boj/").question(boj_id).lang(lang_ext[1:])
    os.makedirs(p.cases, exist_ok=True)
    shutil.move(os.path.join(p.root, filepath), p.solution)

print(f"Current Working Directory: {os.getcwd()}")
path = SolutionPath("./boj/")
problems = os.listdir("./boj/")

groups = {}
for group in range(1, 34):
    g = f"{int(group):02d}"
    groups[g] = f"./boj/{g}XXX"
    os.makedirs(groups[g], exist_ok=True)

print("Group migration started.")
for name in problems:
    if name == "templates" or name.endswith("XXX"):
        continue
    try:
        group = f"{int(name) // 1000:02d}"
        print(f"Moving... {name} -> {group}XXX")
        shutil.move(f"./boj/{name}", groups[group])
    except ValueError:
        # single file solution.
        # Wrap it to solution directory & move it to the correct group.
        print(f"Wrap & Move... {name} -> {group}XXX")
        wrap_single_file_to_directory(name)
