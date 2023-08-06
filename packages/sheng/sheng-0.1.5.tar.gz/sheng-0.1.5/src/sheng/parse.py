from .ply import yacc
from .lex import *
from .ast import *
from .builtins import *
from .exception import *


# Precedence rules
precedence = (
    ('left', 'OR', 'AND'),
    ('left', 'LESS', 'GREATER', 'LESSEQUAL', 'GREATEREQUAL', 'EQEQUAL', 'NOTEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'STAR', 'SLASH', 'DOUBLESLASH', 'PERCENT'),
    ('left', 'DOUBLESTAR'),
    ('right', 'NOT', 'UADD', 'USUB')
)

# Rule for a program
def p_program(p):
    '''program : statements'''
    p[0] = Program(p[1])

# Rule for statement sequence
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if (len(p) == 2 and p[1]):
        statement = p[1]
        p[0] = [statement]
    elif (len(p) == 3):
        statements = p[1]
        if (p[2]): statements.append(p[2])
        p[0] = statements

# Statement rule for function definition
def p_statement_functiondef(p):
    '''statement : FUNCTIONDEF NAME LPAR parameters RPAR BEGIN statements END'''
    name = Name(p[2])
    parameters = p[4]
    body = p[7]
    p[0] = FunctionDef(name, parameters, body)

# Rule for return
def p_statement_return(p):
    '''statement : RETURN expression'''
    p[0] = Return(p[2])

# Statement rule for assignment
def p_statement_assignment(p):
    '''statement : NAME EQUAL expression'''
    name = Name(p[1])
    p[0] = Assignment(name, p[3])

# Statement rule for if-then
def p_statement_ifthen(p):
    '''statement : IF expression THEN statements statement_elifs END'''
    expression = p[2]
    statements = p[4]
    elifs = p[5]
    p[0] = If(expression, statements, elifs)

# Statement rule for if-then-else
def p_statement_ifthenelse(p):
    '''statement : IF expression THEN statements statement_elifs ELSE statements END'''
    expression = p[2]
    statements_if = p[4]
    statements_else = p[7]
    elifs = p[5]
    p[0] = If(expression, statements_if, elifs, statements_else)

# Rule for elif sequence
def p_statement_elifs(p):
    '''statement_elifs : statement_elifs ELIF expression THEN statements
                       | ELIF expression THEN statements
                       | empty'''
    if (len(p) == 5):
        expression = p[2]
        statements = p[4]
        p[0] = [(expression, statements)]
    elif (len(p) == 6):
        elifs = p[1]
        expression = p[3]
        statements = p[5]
        if (p[2]): elifs.append((expression, statements))
        p[0] = elifs
    else:
        p[0] = []

# Statement rule for iterate
def p_statement_iterate(p):
    '''statement : FOR NAME ITERATE NAME BEGIN statements END'''
    variable = p[2]
    iterable = Name(p[4])
    statements = p[6]
    p[0] = Iterate(variable, iterable, statements)

# Statement rule for loop
def p_statement_loop(p):
    '''statement : LOOP expression BEGIN statements END'''
    expression = p[2]
    statements = p[4]
    p[0] = Loop(expression, statements)

# Statement rule for continue
def p_statement_continue(p):
    '''statement : CONTINUE'''
    p[0] = Continue()

# Statement rule for break
def p_statement_break(p):
    '''statement : BREAK'''
    p[0] = Break()

# Statement rule for expression
def p_statement_expression(p):
    '''statement : expression'''
    p[0] = p[1]

# Rule for expressions
def p_expressions(p):
    '''expressions : expressions COMMA expression
                   | expression
                   | empty'''
    if (len(p) == 2 and p[1]):
        expression = p[1]
        p[0] = [expression]
    elif (len(p) == 4):
        expressions = p[1]
        if (p[3]): expressions.append(p[3])
        p[0] = expressions
    else:
        p[0] = []

# Rule for parameters
def p_parameters(p):
    '''parameters : expressions'''
    for node in p[1]:
        if (type(node) != Name):
            raise SyntaxException(
                f'invalid parameter type: {type(node).__name__}'
            )
    p[0] = p[1]

# Expression rule for group surrounded with parentheses
def p_expression_group(p):
    '''expression : LPAR expression RPAR'''
    p[0] = p[2]

# Expression rule for unary operator
def p_expression_unary_operators(p):
    '''expression : NOT expression %prec NOT
                  | PLUS expression %prec UADD
                  | MINUS expression %prec USUB'''
    value = p[2]
    operator = EXACT_TOKEN_TYPES[p[1]]
    if (operator == 'NOT'):
        p[0] = Not(value)
    elif (operator == 'PLUS'):
        p[0] = UAdd(value)
    elif (operator == 'MINUS'):
        p[0] = USubtract(value)

# Expression rule for binary operator
def p_expression_binary_operators(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression STAR expression
                  | expression SLASH expression
                  | expression PERCENT expression
                  | expression DOUBLESTAR expression
                  | expression DOUBLESLASH expression'''
    left = p[1]
    right = p[3]
    operator = EXACT_TOKEN_TYPES[p[2]]
    if (operator == 'PLUS'):
        p[0] = Add(left, right)
    elif (operator == 'MINUS'):
        p[0] = Subtract(left, right)
    elif (operator == 'STAR'):
        p[0] = Multiply(left, right)
    elif (operator == 'SLASH'):
        p[0] = Divide(left, right)
    elif (operator == 'PERCENT'):
        p[0] = Modulo(left, right)
    elif (operator == 'DOUBLESTAR'):
        p[0] = Power(left, right)
    elif (operator == 'DOUBLESLASH'):
        p[0] = FloorDivide(left, right)

# Expression rule for boolean operator
def p_expression_boolean_operators(p):
    '''expression : expression AND expression
                  | expression OR expression'''
    left = p[1]
    right = p[3]
    operator = EXACT_TOKEN_TYPES[p[2]]
    if (operator == 'AND'):
        p[0] = And(left, right)
    elif (operator == 'OR'):
        p[0] = Or(left, right)

# Expression rule for compare operator
def p_expression_compare_operators(p):
    '''expression : expression EQEQUAL expression
                  | expression NOTEQUAL expression
                  | expression LESS expression
                  | expression LESSEQUAL expression
                  | expression GREATER expression
                  | expression GREATEREQUAL expression'''
    left = p[1]
    right = p[3]
    operator = EXACT_TOKEN_TYPES[p[2]]
    if (operator == 'EQEQUAL'):
        p[0] = Equal(left, right)
    elif (operator == 'NOTEQUAL'):
        p[0] = NotEqual(left, right)
    elif (operator == 'LESS'):
        p[0] = Less(left, right)
    elif (operator == 'LESSEQUAL'):
        p[0] = LessEqual(left, right)
    elif (operator == 'GREATER'):
        p[0] = Greater(left, right)
    elif (operator == 'GREATEREQUAL'):
        p[0] = GreaterEqual(left, right)

# Expression rule for boolean constant
def p_expression_boolean(p):
    '''expression : TRUE
                  | FALSE'''
    constant = EXACT_TOKEN_TYPES[p[1]]
    if (constant == 'TRUE'):
        p[0] = Boolean(1)
    elif (constant == 'FALSE'):
        p[0] = Boolean(0)

# Expression rule for integer number
def p_expression_integer(p):
    '''expression : INTEGER'''
    p[0] = Integer(p[1])

# Expression rule for float number
def p_expression_float(p):
    '''expression : FLOAT'''
    p[0] = Float(p[1])

# Expression rule for complex number
def p_expression_complex(p):
    '''expression : COMPLEX'''
    p[0] = Complex(p[1])

# Expression rule for string
def p_expression_string(p):
    '''expression : STRING'''
    p[0] = String(p[1])

# Expression rule for list
def p_expression_list(p):
    '''expression : LSQB expressions RSQB'''
    expressions = p[2]
    p[0] = List(expressions)

# Expression rule for iterable index
def p_expression_iterable_index(p):
    '''expression : NAME INDEX expression'''
    name = Name(p[1])
    expression = p[3]
    p[0] = IterableIndex(name, expression)

# Expression rule for null
def p_expression_null(p):
    '''expression : NULL'''
    p[0] = Null()

# Expression rule for variable name
def p_expression_name(p):
    '''expression : NAME'''
    p[0] = Name(p[1])

# Expression rule for function call
def p_expression_functioncall(p):
    '''expression : NAME LPAR expressions RPAR'''
    name = Name(p[1])
    expressions = p[3]
    p[0] = FunctionCall(name, expressions)

# Rule for nothing
def p_empty(p):
    '''empty : '''

# Error rule for syntax error
def p_error(p):
    raise SyntaxException(f'invalid token {p.value}, line {p.lineno}')

# Build the parser
parser = yacc.yacc()
