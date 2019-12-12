import re
from . import Types
Symbol = Types.Symbol
 
class MalData:
    data_type = None
    data = None

class Reader:

    tokens = None

    def __init__(self, tokens):

        self.index = 0
        self.tokens = tokens

    def next(self):
        """Return the current token and increment the working index"""
        
        buffer = self.peek()
        self.index += 1

        return buffer

    def peek(self):
        """Show the current token"""
        
        return self.tokens[self.index]

def pr_str(node):

    if type(node) == list:
        buffer = []
        for data in node:
            buffer.append(pr_str(data))

        return "(" + " ".join(buffer) + ")"
    elif isinstance(node, MalData):
        return str(node.data)
    else:
        return node

def read_atom(reader):

    int_re = re.compile(r"-?[0-9]+$")
    string_re = re.compile(r'"(?:[\\].|[^\\"])*"')
    token = reader.peek()

    if re.match(int_re, token): 
        return int(token)
    elif re.match(string_re, token):
        return token

    return Symbol(token)

def read_form(reader):

    token = reader.peek()
    buffer = MalData()
    if token == "(":
        reader.next()
        return read_list(reader)
    else:
        buffer.data = read_atom(reader)
        if type(buffer.data) == int:
            buffer.data_type = 'INT'
        elif type(buffer.data) == str:
            buffer.data_type = 'STR'
        elif type(buffer.data) == Symbol:
            buffer.data_type = 'SYM'

        reader.next()
        return buffer

def read_list(reader):

    buffer = []
    while True:
        token = reader.peek()

        if token == ')': return buffer
        else: 
            data = read_form(reader)
            if data is not None:
                buffer.append(data)

def read_str(string):

    buffer = Reader(tokenize(string))
    return read_form(buffer)

def tokenize(string):

    ex = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""");
    return re.findall(ex, string)