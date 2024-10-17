# Generated from MapFilter.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MapFilterParser import MapFilterParser
else:
    from MapFilterParser import MapFilterParser

# This class defines a complete generic visitor for a parse tree produced by MapFilterParser.

class MapFilterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MapFilterParser#prog.
    def visitProg(self, ctx:MapFilterParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#stat.
    def visitStat(self, ctx:MapFilterParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#mapFunction.
    def visitMapFunction(self, ctx:MapFilterParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#filterFunction.
    def visitFilterFunction(self, ctx:MapFilterParser.FilterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#iterable.
    def visitIterable(self, ctx:MapFilterParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#list.
    def visitList(self, ctx:MapFilterParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#tuple.
    def visitTuple(self, ctx:MapFilterParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#function.
    def visitFunction(self, ctx:MapFilterParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#elements.
    def visitElements(self, ctx:MapFilterParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:MapFilterParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#op.
    def visitOp(self, ctx:MapFilterParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#var.
    def visitVar(self, ctx:MapFilterParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterParser#expr.
    def visitExpr(self, ctx:MapFilterParser.ExprContext):
        return self.visitChildren(ctx)



del MapFilterParser