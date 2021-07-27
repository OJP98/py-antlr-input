grammar Decaf;

DIGIT: [0-9]+ ;

LETTER : ('a'..'z'|'A'..'Z'|'_')+ ;

charito : LETTER ;

id : LETTER ( LETTER | DIGIT )* ;

num : DIGIT ( DIGIT )* ;

program : 'class' 'Program' '{' declaration* '}' ;

declaration : structDeclaration | varDeclaration | methodDeclaration ;

varDeclaration : varType id ';' | varType id '[' num ']' ';' ;

structDeclaration : 'struct' id '{' varDeclaration* '}' ';'? ;

varType : 'int' | 'char' | 'boolean' | 'struct' id | structDeclaration | 'void' ;

methodDeclaration : methodType id '(' (parameter (',' parameter)*)* ')' block ;

methodType : 'int' | 'char' | 'boolean' | 'void' ;

parameter : parameterType id | parameterType id '[' ']' | 'void' ;

parameterType : 'int' | 'char' | 'boolean' ;

block : '{' (varDeclaration)* (statement)* '}' ;

statement : 'if' '(' expression ')' block ('else' block)?
          | 'while' '(' expression ')' block
          | 'return' expression? ';'
          | methodCall ';'
          | block
          | location '=' expression
          | expression? ';'
          ;

location : (id | id '[' expression ']') ('.' location)? ;

expression : location
            | methodCall
            | literal
            | expression ('*' | '/') expression
            | expression ('+' | '-') expression
            | expression op expression
            | '-' expression
            | '!' expression
            | '(' expression ')'
            ;

methodCall : id '(' (arg (',' arg)*)* ')' ;

arg : expression ;

op : arith_op | rel_op | eq_op | cond_op ;

arith_op : '*' | '/' | '+' | '-' | '%' ;

rel_op : '<' | '>' | '<=' | '>=' ;

eq_op : '==' | '!=' ;

cond_op : '&&' | '||' ;

literal : int_literal | char_literal | bool_literal ;

int_literal : num ;

char_literal : '\'' charito '\'' ;

bool_literal : 'true' | 'false' ;

WS : [ \t\n\r] + -> skip ;