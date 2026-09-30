def render(data):
    lines = [f"BYTEBOARD: {data['name']}", "=" * (11 + len(data["name"])), ""]
    lines.append("Instructions")
    for item in data["instructions"]:
        arg = f" {item['argrepr']}" if item["argrepr"] else ""
        line = f" line {item['line']}" if item["line"] else ""
        lines.append(f"{item['offset']:>4}  {item['opname']:<24}{arg}{line}")
    lines.append("")
    lines.append("Control-flow edges")
    for start, end in data["edges"]:
        lines.append(f"- {start} -> {end}")
    lines.append("")
    lines.append(f"Constants: {data['constants']}")
    lines.append(f"Names: {data['names']}")
    return "
".join(lines)
