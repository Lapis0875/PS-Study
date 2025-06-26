import os
from lang import LangMap, Language
from lang.errors import UnsupportedLanguageError
from .errors import GeneratorNotFound

def check_generator(boj_id: int, lang_ext: str = "") -> list[str]:
    problem_path = os.path.join(os.getcwd(), "boj", str(boj_id))
    generators = []
    for file in os.listdir(problem_path):
        if os.path.isfile(os.path.join(problem_path, file)):
            name, ext = os.path.splitext(file)
            if name == "generator":
                try:
                    if lang_ext != "":
                        if ext == lang_ext:
                            generators.append(file)
                    else:
                        generators.append(file)
                except KeyError:
                    pass
            break
    return generators