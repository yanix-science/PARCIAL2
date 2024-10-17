# Generated from FourierParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .FourierParser import FourierParser
else:
    from FourierParser import FourierParser

# This class defines a complete listener for a parse tree produced by FourierParser.
class FourierParserListener(ParseTreeListener):

    # Enter a parse tree produced by FourierParser#program.
    def enterProgram(self, ctx:FourierParser.ProgramContext):
        pass

    # Exit a parse tree produced by FourierParser#program.
    def exitProgram(self, ctx:FourierParser.ProgramContext):
        pass


    # Enter a parse tree produced by FourierParser#FourierTransform.
    def enterFourierTransform(self, ctx:FourierParser.FourierTransformContext):
        pass

    # Exit a parse tree produced by FourierParser#FourierTransform.
    def exitFourierTransform(self, ctx:FourierParser.FourierTransformContext):
        pass


    # Enter a parse tree produced by FourierParser#Add.
    def enterAdd(self, ctx:FourierParser.AddContext):
        pass

    # Exit a parse tree produced by FourierParser#Add.
    def exitAdd(self, ctx:FourierParser.AddContext):
        pass


    # Enter a parse tree produced by FourierParser#Divide.
    def enterDivide(self, ctx:FourierParser.DivideContext):
        pass

    # Exit a parse tree produced by FourierParser#Divide.
    def exitDivide(self, ctx:FourierParser.DivideContext):
        pass


    # Enter a parse tree produced by FourierParser#Variable.
    def enterVariable(self, ctx:FourierParser.VariableContext):
        pass

    # Exit a parse tree produced by FourierParser#Variable.
    def exitVariable(self, ctx:FourierParser.VariableContext):
        pass


    # Enter a parse tree produced by FourierParser#Number.
    def enterNumber(self, ctx:FourierParser.NumberContext):
        pass

    # Exit a parse tree produced by FourierParser#Number.
    def exitNumber(self, ctx:FourierParser.NumberContext):
        pass


    # Enter a parse tree produced by FourierParser#Parens.
    def enterParens(self, ctx:FourierParser.ParensContext):
        pass

    # Exit a parse tree produced by FourierParser#Parens.
    def exitParens(self, ctx:FourierParser.ParensContext):
        pass


    # Enter a parse tree produced by FourierParser#Multiply.
    def enterMultiply(self, ctx:FourierParser.MultiplyContext):
        pass

    # Exit a parse tree produced by FourierParser#Multiply.
    def exitMultiply(self, ctx:FourierParser.MultiplyContext):
        pass


    # Enter a parse tree produced by FourierParser#Subtract.
    def enterSubtract(self, ctx:FourierParser.SubtractContext):
        pass

    # Exit a parse tree produced by FourierParser#Subtract.
    def exitSubtract(self, ctx:FourierParser.SubtractContext):
        pass


    # Enter a parse tree produced by FourierParser#Power.
    def enterPower(self, ctx:FourierParser.PowerContext):
        pass

    # Exit a parse tree produced by FourierParser#Power.
    def exitPower(self, ctx:FourierParser.PowerContext):
        pass



del FourierParser