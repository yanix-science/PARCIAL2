parser grammar FourierParser;

options { tokenVocab=FourierLexer; }

// Regla de inicio
program
    : (fourierFunction)* EOF
    ;

// Definición de la función fourier
fourierFunction
    : 'fourier' '(' expression ')'                     # FourierTransform
    ;

// Expresiones matemáticas generales
expression
    : expression PLUS expression                       # Add
    | expression MINUS expression                      # Subtract
    | expression MULT expression                       # Multiply
    | expression DIV expression                        # Divide
    | expression POW expression                        # Power
    | LPAREN expression RPAREN                         # Parens
    | ID                                               # Variable
    | NUMBER                                           # Number
    ;
