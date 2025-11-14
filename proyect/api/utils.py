from antlr4 import *
from lenguage.Gramar_ideLexer import Gramar_ideLexer
from lenguage.Gramar_ideParser import Gramar_ideParser
import traceback

import io
import sys
from lenguage.VIsittor import VIsittor

def run_code(code:str):
    input_stream = InputStream(code)
    lexer = Gramar_ideLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Gramar_ideParser(stream)
    tree=parser.program()

    old_stdout = sys.stdout
    buf = io.StringIO()
    sys.stdout = buf

    try:
        visitor = VIsittor()
        visitor.visit(tree)
        output  = buf.getvalue()
        return output
    except Exception:
        tb = traceback.format_exc()
        return tb
    finally:
        sys.stdout = old_stdout