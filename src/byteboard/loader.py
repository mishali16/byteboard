import types
from pathlib import Path


def load_function(path, name):
    namespace = {}
    code = compile(Path(path).read_text(encoding="utf-8"), str(path), "exec")
    exec(code, namespace)
    func = namespace.get(name)
    if not isinstance(func, types.FunctionType):
        raise ValueError(f"{name!r} is not a function in {path}")
    return func
