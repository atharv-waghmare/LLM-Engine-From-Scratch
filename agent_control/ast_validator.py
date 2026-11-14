import ast
FORBIDDEN_NAMES = {
    "exec", "eval", "compile", "open", "__import__", "getattr", "setattr",
    "delattr", "globals", "locals", "vars", "input", "breakpoint",
}


class SecurityException(Exception):
    pass


class ASTValidator(ast.NodeVisitor):
    def __init__(self):
        self.errors = []

    def visit_Import(self, node):
        self.errors.append("Imports are not allowed")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        self.errors.append("Imports are not allowed")
        self.generic_visit(node)

    def visit_Name(self, node):
        if node.id in FORBIDDEN_NAMES:
            self.errors.append(f"Use of {node.id} is not allowed")
        elif node.id.startswith("__") and node.id.endswith("__"):
            self.errors.append(f"Dunder name ({node.id}) is not allowed")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if node.attr.startswith("__") and node.attr.endswith("__"):
            self.errors.append(f"Dunder attribute access ({node.attr}) is not allowed")
        self.generic_visit(node)


def validate_code(code_string: str) -> bool:
    try:
        tree = ast.parse(code_string)
    except SyntaxError as e:
        raise SecurityException(f"Syntax error: {e}")

    validator = ASTValidator()
    validator.visit(tree)

    if validator.errors:
        raise SecurityException(" | ".join(validator.errors))

    return True

    
    if validator.errors:
        raise SecurityException(" | ".join(validator.errors))
        
    return True
