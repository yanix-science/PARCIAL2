lexer grammar FourierLexer;

// Palabras clave
FOURIER: 'fourier'; // Palabra clave para la función de transformada de Fourier
REAL: 'real';        // Parte real
IMAG: 'imag';        // Parte imaginaria

// Operadores
PLUS: '+'; 
MINUS: '-'; 
MULT: '*'; 
DIV: '/'; 
POW: '^';   // Exponenciación
LPAREN: '(';
RPAREN: ')';

// Identificadores y Números
ID: [a-zA-Z_][a-zA-Z_0-9]*;  // Identificadores (variables)
NUMBER: [0-9]+ ('.' [0-9]+)?; // Números decimales o enteros

// Espacios en blanco y comentarios
WS: [ \t\r\n]+ -> skip;  // Ignorar espacios y saltos de línea
