import pytest
from agent_control.ast_validator import validate_code, SecurityException

def test_safe():
    safe = ["x=1", "y=x", "def f(): pass", "for i in []: pass", "a=[1]", "b={1:2}", "c=(1,)", "d={1}", "if x: pass", "while 0: pass", "class A: pass", "try: pass\nexcept: pass", "max(1,2)", "lambda x: x", "list()", "x,y=1,2", "a=1 if True else 2", "[i for i in []]", "sum([])", "x=2"]
    for s in safe: assert validate_code(s)

def test_unsafe():
    unsafe = ["import os", "import sys", "import math", "import time", "import json", "from os import path", "from sys import exit", "from math import sin", "from time import sleep", "from json import loads", "exec('x=1')", "eval('1')", "x=exec('y=2')", "y=eval('2')", "[exec('pass')]", "a.__class__", "b.__dict__", "c.__init__", "d.__str__()", "e.__repr__()"]
    for s in unsafe:
        with pytest.raises(SecurityException): 
            validate_code(s)