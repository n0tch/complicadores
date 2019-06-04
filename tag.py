from enum import Enum, unique, auto

@unique
class Tag(Enum):
    #Relacional Operators
    OPERATOR_LESS_THAN = auto()
    OPERATOR_GREATER_THAN = auto()
    OPERATOR_LESS_THAN_EQUALS = auto()
    OPERATOR_GREATER_THAN_EQUALS = auto()
    OPERATOR_EQUALS = auto()
    OPERATOR_DIFFERENT = auto()

    #Aritmetic Operators
    OPERATOR_PLUS = auto()
    OPERATOR_MINUS = auto()
    OPERATOR_MULTIPLICATION = auto()
    OPERATOR_DIVISION = auto()
    OPERATOR_PERCENT = auto()
    OPERATOR_AND = auto()
    OPERATOR_OR = auto()
    OPERATOR_NOT = auto()

    #Assign Operator
    OPERATOR_ASSIGN = auto()

    #Simbols
    SYMBOL_OPEN_PARENTHESIS = auto()
    SYMBOL_CLOSE_PARENTHESIS = auto()
    SYMBOL_COMMA = auto()
    SYMBOL_SEMMICOLON = auto()
    SYMBOL_OPEN_BRACKET = auto()
    SYMBOL_CLOSE_BRACKET = auto()

    #Values
    VALUE_NUMERIC = auto()
    VALUE_LITERAL = auto()

    #Language Keywords
    KEYWORD_IF = auto()
    KEYWORD_ELSE = auto()
    KEYWORD_WHILE = auto()
    KEYWORD_RETURN = auto()
    KEYWORD_FLOAT = auto()
    KEYWORD_CHAR = auto()
    KEYWORD_VOID = auto()
    KEYWORD_PRNT = auto()
    KEYWORD_INT = auto()
    KEYWORD_AND = auto()
    KEYWORD_OR = auto()
    KEYWORD_NOT = auto()
    KEYWORD_PROC = auto()
    KEYWORD_VAR = auto()

    # End of file
    END_OF_FILE = auto()