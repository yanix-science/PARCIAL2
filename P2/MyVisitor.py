from MapFunctionVisitor import MapFunctionVisitor  # Importa el Visitor generado por ANTLR
from MapFunctionParser import MapFunctionParser    # Importa el Parser generado por ANTLR

# Definición de la clase MyVisitor que extiende MapFunctionVisitor
class MyVisitor(MapFunctionVisitor):
    def __init__(self):
        # Inicializa un diccionario llamado 'functions' que contiene algunas funciones predefinidas
        # Estas funciones son usadas para transformar datos en el contexto de la operación map
        self.functions = {
            'Upper': lambda x: x.upper(),     # Convierte el texto a mayúsculas
            'Lower': lambda x: x.lower(),     # Convierte el texto a minúsculas
            'Squared': lambda x: x ** 2,      # Calcula el cuadrado de un número
            'Cube': lambda x: x ** 3,         # Calcula el cubo de un número
            'Module2': lambda x: x % 2,       # Calcula el módulo 2 de un número
        }

    # Función que visita las expresiones map definidas en la gramática
    def visitMapFunction(self, ctx):
        # Obtiene el nombre de la función lambda del contexto (ctx)
        function_name = ctx.lambdaExpr().getText()
        # Obtiene los elementos del iterable (lista o tupla)
        iterable_elements = ctx.iterable().getText()

        # Convierte los elementos del iterable de texto a una lista eliminando los corchetes/paréntesis
        iterable_elements = list(iterable_elements[1:-1].split(','))

        # Si el primer elemento es un número, convierte todos los elementos de la lista a enteros
        if iterable_elements[0].isdigit():
            iterable_elements = list(map(int, iterable_elements))

        # Asegúrate de que el 'lambda' tenga un espacio después para evitar problemas con eval()
        function_name = function_name.replace('lambda', 'lambda ')
        
        # Aplica la función lambda usando map() sobre los elementos del iterable
        result = list(map(eval(function_name), iterable_elements))

        # Imprime y retorna el resultado
        print(result)
        return result

    # Función que visita las expresiones filter definidas en la gramática
    def visitFilterFunction(self, ctx):
        # Obtiene el nombre de la función lambda del contexto (ctx)
        function_name = ctx.lambdaExpr().getText()
        # Obtiene los elementos del iterable (lista o tupla)
        iterable_elements = ctx.iterable().getText()

        # Convierte los elementos del iterable de texto a una lista eliminando los corchetes/paréntesis
        iterable_elements = list(iterable_elements[1:-1].split(','))

        # Si el primer elemento es un número, convierte todos los elementos de la lista a enteros
        if iterable_elements[0].isdigit():
            iterable_elements = list(map(int, iterable_elements))

        # Asegúrate de que el 'lambda' tenga un espacio después para evitar problemas con eval()
        function_name = function_name.replace('lambda', 'lambda ')

        # Aplica la función lambda usando filter() sobre los elementos del iterable
        result = list(filter(eval(function_name), iterable_elements))

        # Imprime y retorna el resultado
        print(result)
        return result

    # Función que visita los elementos dentro de una lista o tupla
    def visitElements(self, ctx):
        # Recorre todos los elementos (expresiones) y los visita (evalúa) recursivamente
        return [self.visit(expr) for expr in ctx.expr()]

    # Función que visita un entero (INT)
    def visitINT(self, ctx):
        # Convierte el texto que representa un número entero a un valor int
        return int(ctx.getText())

    # Función que visita un flotante (FLOAT)
    def visitFLOAT(self, ctx):
        # Convierte el texto que representa un número flotante a un valor float
        return float(ctx.getText())

    # Función que visita una cadena (STRING)
    def visitSTRING(self, ctx):
        # Devuelve el texto de la cadena eliminando las comillas al principio y al final
        return ctx.getText()[1:-1]

    # Función que visita un identificador (ID)
    def visitID(self, ctx):
        # Retorna el texto del identificador tal como está
        return ctx.getText()

