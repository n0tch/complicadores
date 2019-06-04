from .tag import Tag
from .token import Token

class SymbolTable():
    def __init__(self):
        self.table = dict()
        self.table['if'] = Token(Tag.KEYWORD_IF, 'if')
        self.table['else'] = Token(Tag.KEYWORD_ELSE, 'else')
        self.table['while'] = Token(Tag.KEYWORD_WHILE, 'while')
        self.table['float'] = Token(Tag.KEYWORD_FLOAT, 'float')
        self.table['char'] = Token(Tag.KEYWORD_CHAR, 'char')
        self.table['void'] = Token(Tag.KEYWORD_VOID, 'void')
        self.table['prnt'] = Token(Tag.KEYWORD_PRNT, 'prnt')
        self.table['int'] = Token(Tag.KEYWORD_INT, 'int')
        self.table['and'] = Token(Tag.KEYWORD_AND, 'and')
        self.table['or'] = Token(Tag.KEYWORD_OR, 'or')
        self.table['not'] = Token(Tag.KEYWORD_NOT, 'not')
        self.table['proc'] = Token(Tag.KEYWORD_PROC, 'proc')
        self.table['var'] = Token(Tag.KEYWORD_VAR, 'var')

    def includeNewSymbol(self, lexeme, tag):
        token = self.table.get(lexeme, None)
        if not token:
            token = Token(tag, lexeme)
            self.table[lexeme] = token
        return token