from antlr4 import *
from FourierLexer import FourierLexer
from FourierParser import FourierParser

class FourierVisitor(ParseTreeVisitor):
    def visitFourierTransform(self, ctx):
        expr_value = self.visit(ctx.expression())
        # Aquí realizarías el cálculo de la transformada de Fourier
        print(f"Calculando transformada de Fourier de: {expr_value}")
        return expr_value

    def visitAdd(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left + right

    def visitSubtract(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left - right

    def visitMultiply(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left * right

    def visitDivide(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left / right

    def visitPower(self, ctx):
        base = self.visit(ctx.expression(0))
        exponent = self.visit(ctx.expression(1))
        return base ** exponent

    def visitNumber(self, ctx):
        return float(ctx.getText())

    def visitVariable(self, ctx):
        # Puedes añadir una lógica para manejar variables
        return 0

# Ejemplo de uso
if __name__ == "__main__":
    input_stream = InputStream("fourier(3 + 5 * 2)")
    lexer = FourierLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = FourierParser(token_stream)
    tree = parser.program()

    visitor = FourierVisitor()
    visitor.visit(tree)
