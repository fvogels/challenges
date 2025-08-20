from dataclasses import dataclass
import verilib
import importlib.util
import pathlib
import contextlib
import io
from fractions import Fraction


@dataclass
class Result:
    path: pathlib.Path
    grade: Fraction
    message: str


class Challenge:
    path: pathlib.Path
    verify_path: pathlib.Path
    module: importlib.machinery.ModuleSpec

    def __init__(self, path: pathlib.Path | str):
        if isinstance(path, str):
            self.path = pathlib.Path(path)
        else:
            self.path = path

        self.verify_path = self.path / "verify.py"
        self.module = Challenge.load_verifier(self.verify_path)

    @staticmethod
    def load_verifier_source(path: pathlib.Path):
        with path.open() as file:
            source = file.read()
        return source

    @staticmethod
    def load_verifier(path: pathlib.Path):
        module_name = pathlib.Path(path).stem
        source = Challenge.load_verifier_source(path)

        # Create a new module
        spec = importlib.util.spec_from_loader(module_name, loader=None)
        module = importlib.util.module_from_spec(spec)

        # Inject foo symbols before execution
        module.verilib = verilib

        # Execute decrypted code inside module namespace
        exec(source, module.__dict__)

        return module

    def verify(self):
        with contextlib.chdir(self.path):
            try:
                redirected_output = io.StringIO()
                with contextlib.redirect_stdout(redirected_output):
                    grade = self.module.verify()
                return Result(path=self.path, grade=grade, message=redirected_output.getvalue())

            except Exception as e:
                message = f"An error occurred during verification:\n{str(e)}"
                return Result(path=self.path, grade=0, message=message)


def discover_challenges() -> list[Challenge]:
    challenges = []
    for path in pathlib.Path("foo").rglob("verify.py"):
        challenges.append(Challenge(path.parent))
    return challenges


challenges = discover_challenges()

for challenge in challenges:
    result = challenge.verify()
    print(result)