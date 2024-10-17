grammar MapFilter;  // Nombre de la gramática

// Reglas principales
prog:   stat+ ;  // La regla 'prog' es el punto de entrada del programa, compuesto por una o más declaraciones (stat).

// Una declaración puede ser una función map o filter seguida de una nueva línea
stat:   mapFunction NEWLINE   // La regla 'stat' permite una función map seguida de una nueva línea
    |   filterFunction NEWLINE // O una función filter seguida de una nueva línea
    ;

// Definición de la función map
mapFunction: 'map' '(' lambdaExpr ',' iterable ')' ;
// Definición de la función filter
filterFunction: 'filter' '(' lambdaExpr ',' iterable ')' ;

// Un iterable puede ser una lista o una tupla
iterable: list | tuple ;

// Definición de una lista
list: '[' elements? ']' ;  // Una lista está definida por corchetes y puede tener elementos opcionales
// Definición de una tupla
tuple: '(' elements? ')' ; // Una tupla está definida por paréntesis y puede tener elementos opcionales

// Definición de una función. 
// Puede ser una operación matemática, transformación de string (upper, lower, etc.), una operación sobre índices o una función anidada
function: ID op var
        | ID '.upper()'
        | ID '.lower()'
        | ID '.capitalize()'
        | 'len(' ID ')' (op var)?
        | ID op var op var (' and '|' or ')? function?
        | ID '[' INT ']' (op var)?
        ;

// Una lista de elementos, separados por comas
elements: expr (',' expr)* ;  // Los elementos de una lista o tupla son expresiones, y pueden estar separados por comas

// Expresión lambda, donde el argumento de la lambda es una variable y la función es una operación
lambdaExpr: 'lambda' ID ':' function ;  // Definición de una expresión lambda, con un identificador y una función

// Definición de operadores
op: '+' | '-' | '*' | '/' | '%' | '**' | '.' ID '()' // Los operadores pueden ser aritméticos, de comparación o funciones de string
   | '==' | '!=' | '<' | '>' | '<=' | '>=' ;  // Operadores de comparación

// Las variables pueden ser identificadores, enteros o flotantes
var: ID | INT | FLOAT ;

// Una expresión puede ser un número entero, un flotante o una cadena de texto
expr: INT | FLOAT | STRING ;

// Definición de los tokens para enteros, identificadores, flotantes y cadenas
INT: [0-9]+ ;          // Un entero está compuesto por uno o más dígitos
ID: [a-zA-Z]+ ;        // Un identificador está compuesto por letras
FLOAT: [0-9]+ '.' [0-9]+ ; // Un flotante tiene un punto decimal
STRING: '"' .*? '"' ;   // Una cadena de texto está rodeada por comillas dobles

// Definición de operadores matemáticos
MUL :   '*' ;          // Multiplicación
DIV :   '/' ;          // División
ADD :   '+' ;          // Suma
SUB :   '-' ;          // Resta

// Manejo de nueva línea para identificar el final de una declaración
NEWLINE: '\r'? '\n' ;  // Una nueva línea es un retorno de carro opcional seguido de una nueva línea

// Ignorar espacios en blanco y tabulaciones
WS  :   [ \t]+ -> skip ; // Los espacios en blanco y tabulaciones son ignorados

