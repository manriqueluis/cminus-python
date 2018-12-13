from antlr4 import *
from gen.CminusLexer import CminusLexer
from gen.CminusParser import CminusParser

input_stream = FileStream('files/code_test.c-')
lexer = CminusLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = CminusParser(stream)
tree = parser.program()

