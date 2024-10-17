from ComplexVisitor import ComplexVisitor  # Importa la clase LabeledExprVisitor generada por ANTLR
from ComplexParser import ComplexParser    # Importa la clase LabeledExprParser generada por ANTLR

# Definición de la clase MyVisitor que hereda de 
class MyVisitor(ComplexVisitor):
    # Constructor que inicializa un diccionario para almacenar variables y sus valores
    def __init__(self):
        self.memory = {}

    # Función para manejar asignaciones de variables
    def visitAssign(self, ctx):
        # Obtiene el nombre de la variable (identificador) desde el contexto (ctx)
        name = ctx.ID().getText()
        # Evalúa la expresión a la derecha de la asignación y la convierte en un número complejo
        value = complex(self.visit(ctx.expr()))
        # Guarda el valor en el diccionario de memoria con el nombre de la variable como clave
        self.memory[name] = value
        # Retorna el valor asignado
        return value

    # Función para manejar la impresión de expresiones
    def visitPrintExpr(self, ctx):
        # Evalúa la expresión usando el visitor para obtener su valor
        value = self.visit(ctx.expr())
        # Imprime el valor en la consola
        print(value)
        # Retorna 0 (esto no afecta el comportamiento, pero es necesario retornar algo)
        return 0

    # Función para manejar literales complejos
    def visitComplex(self, ctx):
        # Retorna el valor del literal COMPLEX en formato de texto
        return ctx.COMPLEX().getText()

    # Función para manejar identificadores (variables)
    def visitId(self, ctx):
        # Obtiene el nombre de la variable desde el contexto
        name = ctx.ID().getText()
        # Si la variable existe en la memoria, retorna su valor
        if name in self.memory:
            return self.memory[name]
        # Si no existe, retorna 0
        return 0

    # Función para manejar multiplicación y división
    def visitMulDiv(self, ctx):
        # Evalúa la expresión de la izquierda y la convierte en un número complejo
        left = complex(self.visit(ctx.expr(0)))
        # Evalúa la expresión de la derecha y la convierte en un número complejo
        right = complex(self.visit(ctx.expr(1)))
        # Si el operador es de multiplicación, retorna el resultado de multiplicar los operandos
        if ctx.op.type == ComplexParser.MUL:
            return left * right
        # Si no, asume que es división y retorna el resultado de dividir los operandos
        return left / right

    # Función para manejar suma y resta
    def visitAddSub(self, ctx):
        # Evalúa la expresión de la izquierda y la convierte en un número complejo
        left = complex(self.visit(ctx.expr(0)))
        # Evalúa la expresión de la derecha y la convierte en un número complejo
        right = complex(self.visit(ctx.expr(1)))
        # Si el operador es suma, retorna la suma de los operandos
        if ctx.op.type == ComplexParser.ADD:
            return left + right
        # Si no, asume que es resta y retorna la resta de los operandos
        return left - right

    # Función para manejar expresiones entre paréntesis
    def visitParens(self, ctx):
        # Evalúa la expresión contenida dentro de los paréntesis
        return self.visit(ctx.expr())

