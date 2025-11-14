# Generated from Gramar_ide.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Gramar_ideParser import Gramar_ideParser
else:
    from Gramar_ideParser import Gramar_ideParser

# This class defines a complete listener for a parse tree produced by Gramar_ideParser.
class Gramar_ideListener(ParseTreeListener):

    # Enter a parse tree produced by Gramar_ideParser#program.
    def enterProgram(self, ctx:Gramar_ideParser.ProgramContext):
        pass

    # Exit a parse tree produced by Gramar_ideParser#program.
    def exitProgram(self, ctx:Gramar_ideParser.ProgramContext):
        pass


    # Enter a parse tree produced by Gramar_ideParser#statement.
    def enterStatement(self, ctx:Gramar_ideParser.StatementContext):
        pass

    # Exit a parse tree produced by Gramar_ideParser#statement.
    def exitStatement(self, ctx:Gramar_ideParser.StatementContext):
        pass


    # Enter a parse tree produced by Gramar_ideParser#assing.
    def enterAssing(self, ctx:Gramar_ideParser.AssingContext):
        pass

    # Exit a parse tree produced by Gramar_ideParser#assing.
    def exitAssing(self, ctx:Gramar_ideParser.AssingContext):
        pass


    # Enter a parse tree produced by Gramar_ideParser#type.
    def enterType(self, ctx:Gramar_ideParser.TypeContext):
        pass

    # Exit a parse tree produced by Gramar_ideParser#type.
    def exitType(self, ctx:Gramar_ideParser.TypeContext):
        pass


    # Enter a parse tree produced by Gramar_ideParser#print.
    def enterPrint(self, ctx:Gramar_ideParser.PrintContext):
        pass

    # Exit a parse tree produced by Gramar_ideParser#print.
    def exitPrint(self, ctx:Gramar_ideParser.PrintContext):
        pass


    # Enter a parse tree produced by Gramar_ideParser#if_statement.
    def enterIf_statement(self, ctx:Gramar_ideParser.If_statementContext):
        pass

    # Exit a parse tree produced by Gramar_ideParser#if_statement.
    def exitIf_statement(self, ctx:Gramar_ideParser.If_statementContext):
        pass


    # Enter a parse tree produced by Gramar_ideParser#for_statement.
    def enterFor_statement(self, ctx:Gramar_ideParser.For_statementContext):
        pass

    # Exit a parse tree produced by Gramar_ideParser#for_statement.
    def exitFor_statement(self, ctx:Gramar_ideParser.For_statementContext):
        pass


    # Enter a parse tree produced by Gramar_ideParser#block.
    def enterBlock(self, ctx:Gramar_ideParser.BlockContext):
        pass

    # Exit a parse tree produced by Gramar_ideParser#block.
    def exitBlock(self, ctx:Gramar_ideParser.BlockContext):
        pass


    # Enter a parse tree produced by Gramar_ideParser#expr.
    def enterExpr(self, ctx:Gramar_ideParser.ExprContext):
        pass

    # Exit a parse tree produced by Gramar_ideParser#expr.
    def exitExpr(self, ctx:Gramar_ideParser.ExprContext):
        pass



del Gramar_ideParser