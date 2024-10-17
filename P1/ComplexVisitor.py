# Generated from Complex.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ComplexParser import ComplexParser
else:
    from ComplexParser import ComplexParser

# This class defines a complete generic visitor for a parse tree produced by ComplexParser.

class ComplexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplexParser#prog.
    def visitProg(self, ctx:ComplexParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#printExpr.
    def visitPrintExpr(self, ctx:ComplexParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#assign.
    def visitAssign(self, ctx:ComplexParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#blank.
    def visitBlank(self, ctx:ComplexParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#parens.
    def visitParens(self, ctx:ComplexParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#MulDiv.
    def visitMulDiv(self, ctx:ComplexParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#AddSub.
    def visitAddSub(self, ctx:ComplexParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#complex.
    def visitComplex(self, ctx:ComplexParser.ComplexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplexParser#id.
    def visitId(self, ctx:ComplexParser.IdContext):
        return self.visitChildren(ctx)



del ComplexParser