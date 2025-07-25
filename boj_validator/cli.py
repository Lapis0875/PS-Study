from click import group, argument, help_option, INT, STRING, FLOAT, BOOL
from pathlib import Path
from os import mkdir, makedirs

from lang import Language, LangMap
from lang.errors import UnsupportedLanguageError
from validator import BOJValidator
from migration import migrate as migrate_task
from generator import CaseGenerator, checks
from path_util import SolutionPath

__all__ = ("cli",)

@group()
def cli(): pass

@cli.command()
@argument("boj_number", type=INT)
@argument("lang_ext", type=STRING)
def create(boj_number: int, lang_ext: str):
    path = SolutionPath()
    path.question(boj_number).lang(lang_ext)
    makedirs(path.cases, exist_ok=True)
    with (
        open(file=path.solution, mode="w") as sol_file,
        open(file=f"./boj/templates/solution.{lang_ext}", mode="r") as template
    ):
        sol_file.write(template.read())
    print(">>> Done!")

@cli.command()
@argument("boj_number", type=INT)
@argument("lang_ext", type=STRING)
@argument("time", type=FLOAT, default=1.0)
@argument("memory", type=INT, default=128)
@argument("extra_time", type=BOOL, default=True)
def run(boj_number: int, lang_ext: str, time: float = 1.0, memory: int = 128, extra_time: bool = True):
    """Judge the solution of the BOJ problem."""
    lang: Language = LangMap[lang_ext]()
    validator = BOJValidator(lang, time, memory, extra_time)
    validator.parse_question_data(boj_number)
    validator.run()

@cli.command()
@argument("boj_number", type=INT)
@argument("amount", type=INT)
def cases(boj_number: int, amount: int):
    """Command to automatically create input and output files for the test cases. (Content should be manually filled.)"""
    path = SolutionPath()
    path.question(boj_number)
    for i in range(amount):
        Path(f"{path.cases}/{i}.in").touch()
        Path(f"{path.cases}/{i}.out").touch()
    print(">>> Done!")

@cli.command()
@argument("boj_number", type=INT)
@argument("lang_ext", type=STRING, default="cpp")
@argument("time", type=FLOAT, default=30.0)
@argument("memory", type=INT, default=1024)
@argument("extra_time", type=BOOL, default=True)
def debug_mode(boj_number: int, lang_ext: str = "cpp", time: float = 30.0, memory: int = 1024, extra_time: bool = True):
    """Just a command to add '#define DEBUG' to the code. (Only for C++ and C)"""
    if lang_ext not in ("cpp", "c"):
        print(">>> This feautre is only for C++ and C. This feature just adds '#define DEBUG' to the code, so other languages do not need this.")
        return
    
    lang: Language = LangMap[lang_ext]()
    validator = BOJValidator(lang, time, memory, extra_time)
    validator.parse_question_data(boj_number)
    validator.debug()

@cli.command()
@argument("boj_number", type=INT)
@argument("lang_ext", type=STRING)
@argument("case_number", type=INT)
@argument("time", type=FLOAT, default=1.0)
@argument("memory", type=INT, default=128)
@argument("extra_time", type=BOOL, default=True)
def debug_case(boj_number: int, lang_ext: str, case_number: int, time: float, memory: int, extra_time: bool):
    """Test a certain case input to the solution."""
    lang: Language = LangMap[lang_ext]()
    validator = BOJValidator(lang, time, memory, extra_time)
    validator.parse_question_data(boj_number)
    validator.debug_case(case_number)

@cli.command()
def migrate():
    """Command to automatically migrate old boj solution files (bojXXXXX.{lang_ext}) to the new format (boj/XXXXXX/solution.{lang_ext})."""
    print("Migrating old boj solutions ...")
    migrate_task("./boj")
    print(">>> Done!")

@cli.group()
def generator():
    """Command group to run/manage 'generator' scripts for boj problems."""
    pass

@generator.command()
@argument("boj_number", type=INT, metavar="BOJ problem number.")
@argument("lang_ext", type=STRING, metavar="Language of generator script. Defines which language runner to use.")
def run(boj_number: int, lang_ext: str):
    """Run generator script of language {lang_ext} for boj problem {boj_number}.
    @raises UnsupportedLanguageError: If argument {lang_ext} is not supported.
    """
    try:
        gen = CaseGenerator(lang_ext, boj_number)
        gen.run()
    except UnsupportedLanguageError as e:
        print(e)

@generator.command()
@argument("boj_number", type=INT, metavar="BOJ problem number.")
@argument("lang_ext", type=STRING, default="", metavar="Specific language for generator script. If not supplied, then checks all of existing scripts.")
def check(boj_number: int, lang_ext: str = ""):
    """Check all/certain generator script in boj/{boj_number}."""
    try:
        gen_scripts = checks.check_generator(boj_number, lang_ext)
        print("\n".join(map(lambda sc: f"- ./{sc}", gen_scripts)))
    except UnsupportedLanguageError as e:
        print(e)
