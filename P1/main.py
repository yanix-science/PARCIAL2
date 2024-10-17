import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from ComplexLexer import ComplexLexer
from ComplexParser import ComplexParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = ComplexLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ComplexParser(token_stream)
    tree = parser.prog()

    visitor = MyVisitor()
    visitor.visit(tree)
