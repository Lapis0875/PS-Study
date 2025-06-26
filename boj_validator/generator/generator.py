from typing import Final
import os
from lang import LangMap, Language
from .case import Case

class CaseGenerator:
    """Runner class for test case generator script.
    
    Generator script should write test case data to stdout in following format:
    ```
    {Input Data 1}
    ---
    {Output Data 1}
    ---
    {Input Data 2}
    ---
    {Output Data 2}
    ...
    ```
    """
    lang_ext: Final[str]
    boj_number: Final[int]
    solution_path: Final[str]
    script_path: Final[str]
    
    def __init__(self, lang_ext: str, boj_number: int):
        self.lang_ext = lang_ext
        self.boj_number = boj_number
        self.solution_path = os.path.join(os.getcwd(), "boj", str(boj_number))
        self.script_path = os.path.join(self.solution_path, f"generator.{lang_ext}")
    
    def run(self) -> list[Case]:
        lang: Language = LangMap[self.lang_ext]
        proc = lang.run_script(self.script_path)  # For now, we don't supply input to generator script.
        output = proc.stdout.strip()
        self.parse(output)
    
    def parse(self, output_txt: str) -> list[Case]:
        """Parse output from generator script to list of Case objects."""
        case_data = output_txt.split("---\n")
        return [
            Case(boj_id=self.boj_number, input_data=case_data[i].strip(), output_data=case_data[i+1].strip())
            for i in range(0, len(case_data), 2)
        ]
