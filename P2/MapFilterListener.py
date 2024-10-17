# Generated from MapFilter.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MapFilterParser import MapFilterParser
else:
    from MapFilterParser import MapFilterParser

# This class defines a complete listener for a parse tree produced by MapFilterParser.
class MapFilterListener(ParseTreeListener):

    # Enter a parse tree produced by MapFilterParser#prog.
    def enterProg(self, ctx:MapFilterParser.ProgContext):
        pass

    # Exit a parse tree produced by MapFilterParser#prog.
    def exitProg(self, ctx:MapFilterParser.ProgContext):
        pass


    # Enter a parse tree produced by MapFilterParser#stat.
    def enterStat(self, ctx:MapFilterParser.StatContext):
        pass

    # Exit a parse tree produced by MapFilterParser#stat.
    def exitStat(self, ctx:MapFilterParser.StatContext):
        pass


    # Enter a parse tree produced by MapFilterParser#mapFunction.
    def enterMapFunction(self, ctx:MapFilterParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by MapFilterParser#mapFunction.
    def exitMapFunction(self, ctx:MapFilterParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by MapFilterParser#filterFunction.
    def enterFilterFunction(self, ctx:MapFilterParser.FilterFunctionContext):
        pass

    # Exit a parse tree produced by MapFilterParser#filterFunction.
    def exitFilterFunction(self, ctx:MapFilterParser.FilterFunctionContext):
        pass


    # Enter a parse tree produced by MapFilterParser#iterable.
    def enterIterable(self, ctx:MapFilterParser.IterableContext):
        pass

    # Exit a parse tree produced by MapFilterParser#iterable.
    def exitIterable(self, ctx:MapFilterParser.IterableContext):
        pass


    # Enter a parse tree produced by MapFilterParser#list.
    def enterList(self, ctx:MapFilterParser.ListContext):
        pass

    # Exit a parse tree produced by MapFilterParser#list.
    def exitList(self, ctx:MapFilterParser.ListContext):
        pass


    # Enter a parse tree produced by MapFilterParser#tuple.
    def enterTuple(self, ctx:MapFilterParser.TupleContext):
        pass

    # Exit a parse tree produced by MapFilterParser#tuple.
    def exitTuple(self, ctx:MapFilterParser.TupleContext):
        pass


    # Enter a parse tree produced by MapFilterParser#function.
    def enterFunction(self, ctx:MapFilterParser.FunctionContext):
        pass

    # Exit a parse tree produced by MapFilterParser#function.
    def exitFunction(self, ctx:MapFilterParser.FunctionContext):
        pass


    # Enter a parse tree produced by MapFilterParser#elements.
    def enterElements(self, ctx:MapFilterParser.ElementsContext):
        pass

    # Exit a parse tree produced by MapFilterParser#elements.
    def exitElements(self, ctx:MapFilterParser.ElementsContext):
        pass


    # Enter a parse tree produced by MapFilterParser#lambdaExpr.
    def enterLambdaExpr(self, ctx:MapFilterParser.LambdaExprContext):
        pass

    # Exit a parse tree produced by MapFilterParser#lambdaExpr.
    def exitLambdaExpr(self, ctx:MapFilterParser.LambdaExprContext):
        pass


    # Enter a parse tree produced by MapFilterParser#op.
    def enterOp(self, ctx:MapFilterParser.OpContext):
        pass

    # Exit a parse tree produced by MapFilterParser#op.
    def exitOp(self, ctx:MapFilterParser.OpContext):
        pass


    # Enter a parse tree produced by MapFilterParser#var.
    def enterVar(self, ctx:MapFilterParser.VarContext):
        pass

    # Exit a parse tree produced by MapFilterParser#var.
    def exitVar(self, ctx:MapFilterParser.VarContext):
        pass


    # Enter a parse tree produced by MapFilterParser#expr.
    def enterExpr(self, ctx:MapFilterParser.ExprContext):
        pass

    # Exit a parse tree produced by MapFilterParser#expr.
    def exitExpr(self, ctx:MapFilterParser.ExprContext):
        pass



del MapFilterParser