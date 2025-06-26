import os
from generator.case import Case

def convert_to_cli_spec(cases: list[Case]):
    """Convert generator script output to BOJ Validator's cli case spec."""
    case_dir = os.path.join("./boj", cases[0].boj_id, "cases")
    os.makedirs(case_dir, exist_ok=True)
    for i, case in enumerate(cases):
        with open(os.path.join(case_dir, f"{i}.in"), "w") as f:
            f.write(case.input)
        with open(os.path.join(case_dir, f"{i}.out"), "w") as f:
            f.write(case.output)

def convert_to_CPH(cases: list[Case]):
    """Convert generator script output to CPH Judge plugin spec."""
    raise NotImplementedError("Converter for CPH Judge plugin spec is not implemented yet.")
