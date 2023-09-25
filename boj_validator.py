from abc import ABCMeta
from os import listdir
import sys
from typing import Final, Type
from functools import cached_property


class Language(metaclass=ABCMeta):
    ext: Final[str] = ""
    
    def run(self, code_path: str, input: str, output: str) -> tuple[bool, str]:
        ...

class Python(Language):
    """
    Python language runner for solutions written in Python3.
    """

class C(Language):
    """
    C language runner for solutions written in Python3.
    """

class CPlusPlus(Language):
    """
    C++ language runner for solutions written in Python3.
    """

LangMap: dict[str, Type[Language]] = {
    "py": Python,
    "c": C,
    "cpp": CPlusPlus
}

class BOJValidator:
    boj_id: Final[int]
    lang: Final[Language]
    inputs: list[str]
    outputs: list[str]
    
    def __init__(self, boj_id: int, lang: Language):
        self.boj_id = boj_id
        self.lang = lang

    def parse_question_data(self):
        """
        이 문제의 입출력 데이터를 불러옵니다.
        """
        case_path: str = self.dir_path + "cases/"
        cases: list[str] = listdir(case_path)
        cases.sort()

        self.inputs = []
        self.outputs = []
        for case in cases:
            if case.endswith(".in"):                    # input data
                with open(case_path + case, "r") as f:
                    self.inputs.append(f.read())
            elif case.endswith(".out"):                 # output data
                with open(case_path + case, "r") as f:
                    self.outputs.append(f.read())
        
        if len(self.inputs) != len(self.outputs):
            # input&output data does not match!
            print("** Warning **\nInput&Output data does not match! ")
            

    def print_case(self, input: str, expected_output: str, code_output: str):
        """
        특정 케이스의 실행 결과 정보를 출력합니다. 주로 예상한 출력과 실제 출력이 다름을 표시하기 위해 사용되는 메소드입니다.
        """
        print("=" * 20)
        print("** Wrong Output **")
        print("Input:")
        print(input)
        print("Answer:")
        print(expected_output)
        print("Your Output:")
        print(code_output)
    
    @cached_property
    def dir_path(self) -> str:
        """
        이 문제의 코드 경로를 반환합니다.
        """
        return f"./boj/{self.boj_id}/"
    
    @cached_property
    def code_file(self) -> str:
        return f"solution.{self.lang.ext}"
    
    @cached_property
    def file_path(self) -> str:
        return f"{self.dir_path}{self.code_file}"

    def run(self):
        """해당 문제의 풀이 코드에 대해 테스트 케이스들을 모두 점검해 본다."""
        for input, output in zip(self.inputs, self.outputs):
            is_valid_code, code_output = self.lang.run(self.file_path, input, output)
            if not is_valid_code:
                self.print_case(input, output, code_output)

# main.py

def main():
    """CLI로 실행된 경우 수행할 코드."""
    boj_number: int = int(sys.argv[1])
    lang_ext: str = sys.argv[2]

    lang: Language = LangMap[lang_ext]()
    validator = BOJValidator(boj_number, lang)

    validator.run()

# 이 파이썬 코드가 python ~~.py 명령어로 실행된 파일일 때 (다른 파일에서 모듈로 불러와진 경우를 제외해준다)
if __name__ == "__main__":
    main()
