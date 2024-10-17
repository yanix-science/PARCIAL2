# Generated from Complex.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ComplexParser import ComplexParser
else:
    from ComplexParser import ComplexParser

# This class defines a complete listener for a parse tree produced by ComplexParser.
class ComplexListener(ParseTreeListener):

    # Enter a parse tree produced by ComplexParser#prog.
    def enterProg(self, ctx:ComplexParser.ProgContext):
        pass

    # Exit a parse tree produced by ComplexParser#prog.
    def exitProg(self, ctx:ComplexParser.ProgContext):
        pass


    # Enter a parse tree produced by ComplexParser#printExpr.
    def enterPrintExpr(self, ctx:ComplexParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#printExpr.
    def exitPrintExpr(self, ctx:ComplexParser.PrintExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#assign.
    def enterAssign(self, ctx:ComplexParser.AssignContext):
        pass

    # Exit a parse tree produced by ComplexParser#assign.
    def exitAssign(self, ctx:ComplexParser.AssignContext):
        pass


    # Enter a parse tree produced by ComplexParser#blank.
    def enterBlank(self, ctx:ComplexParser.BlankContext):
        pass

    # Exit a parse tree produced by ComplexParser#blank.
    def exitBlank(self, ctx:ComplexParser.BlankContext):
        pass


    # Enter a parse tree produced by ComplexParser#parens.
    def enterParens(self, ctx:ComplexParser.ParensContext):
        pass

    # Exit a parse tree produced by ComplexParser#parens.
    def exitParens(self, ctx:ComplexParser.ParensContext):
        pass


    # Enter a parse tree produced by ComplexParser#MulDiv.
    def enterMulDiv(self, ctx:ComplexParser.MulDivContext):
        pass

    # Exit a parse tree produced by ComplexParser#MulDiv.
    def exitMulDiv(self, ctx:ComplexParser.MulDivContext):
        pass


    # Enter a parse tree produced by ComplexParser#AddSub.
    def enterAddSub(self, ctx:ComplexParser.AddSubContext):
        pass

    # Exit a parse tree produced by ComplexParser#AddSub.
    def exitAddSub(self, ctx:ComplexParser.AddSubContext):
        pass


    # Enter a parse tree produced by ComplexParser#complex.
    def enterComplex(self, ctx:ComplexParser.ComplexContext):
        pass

    # Exit a parse tree produced by ComplexParser#complex.
    def exitComplex(self, ctx:ComplexParser.ComplexContext):
        pass


    # Enter a parse tree produced by ComplexParser#id.
    def enterId(self, ctx:ComplexParser.IdContext):
        pass

    # Exit a parse tree produced by ComplexParser#id.
    def exitId(self, ctx:ComplexParser.IdContext):
        pass



del ComplexParser