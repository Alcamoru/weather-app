def tagged(func):
    def wrapper(func_args):
        return f"<title>{func(func_args)}</title>"
    return wrapper


@tagged
def from_input(inp):
    string = inp.strip()
    return string
