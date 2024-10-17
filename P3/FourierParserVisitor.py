# Generated from FourierParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .FourierParser import FourierParser
else:
    from FourierParser import FourierParser

# This class defines a complete generic visitor for a parse tree produced by FourierParser.

class FourierParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FourierParser#program.
    def visitProgram(self, ctx:FourierParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#FourierTransform.
    def visitFourierTransform(self, ctx:FourierParser.FourierTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#Add.
    def visitAdd(self, ctx:FourierParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#Divide.
    def visitDivide(self, ctx:FourierParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#Variable.
    def visitVariable(self, ctx:FourierParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#Number.
    def visitNumber(self, ctx:FourierParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#Parens.
    def visitParens(self, ctx:FourierParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#Multiply.
    def visitMultiply(self, ctx:FourierParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#Subtract.
    def visitSubtract(self, ctx:FourierParser.SubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FourierParser#Power.
    def visitPower(self, ctx:FourierParser.PowerContext):
        return self.visitChildren(ctx)



del FourierParser