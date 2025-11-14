# Generated from Gramar_ide.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Gramar_ideParser import Gramar_ideParser
else:
    from Gramar_ideParser import Gramar_ideParser

# This class defines a complete generic visitor for a parse tree produced by Gramar_ideParser.

class Gramar_ideVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Gramar_ideParser#program.
    def visitProgram(self, ctx:Gramar_ideParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramar_ideParser#statement.
    def visitStatement(self, ctx:Gramar_ideParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramar_ideParser#assing.
    def visitAssing(self, ctx:Gramar_ideParser.AssingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramar_ideParser#type.
    def visitType(self, ctx:Gramar_ideParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramar_ideParser#print.
    def visitPrint(self, ctx:Gramar_ideParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramar_ideParser#if_statement.
    def visitIf_statement(self, ctx:Gramar_ideParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramar_ideParser#for_statement.
    def visitFor_statement(self, ctx:Gramar_ideParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramar_ideParser#block.
    def visitBlock(self, ctx:Gramar_ideParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramar_ideParser#expr.
    def visitExpr(self, ctx:Gramar_ideParser.ExprContext):
        return self.visitChildren(ctx)



del Gramar_ideParser