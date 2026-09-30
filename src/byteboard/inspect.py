import dis


JUMP_WORDS = ("JUMP", "FOR_ITER", "POP_JUMP")


def inspect_function(func):
    instructions = []
    edges = []
    raw = list(dis.get_instructions(func))
    offsets = {item.offset for item in raw}
    for index, item in enumerate(raw):
        instructions.append(
            {
                "offset": item.offset,
                "opname": item.opname,
                "argrepr": item.argrepr,
                "line": item.starts_line,
            }
        )
        if any(word in item.opname for word in JUMP_WORDS) and isinstance(item.argval, int):
            edges.append((item.offset, item.argval))
        if index + 1 < len(raw) and item.opname not in {"RETURN_VALUE", "RAISE_VARARGS"}:
            next_offset = raw[index + 1].offset
            if next_offset in offsets:
                edges.append((item.offset, next_offset))
    return {
        "name": func.__name__,
        "constants": list(func.__code__.co_consts),
        "names": list(func.__code__.co_names),
        "instructions": instructions,
        "edges": sorted(set(edges)),
    }
