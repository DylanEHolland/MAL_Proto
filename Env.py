class Env:

    def __init__(self, outer = None):
        self.data = {}
        self.outer = outer

    def find(self, symbol):
        if symbol in self.data:
            return self
        elif self.outer is not None:
            return self.outer.find(symbol)
        else: 
            return None

    def set(self, symbol, arg):
        self.data[symbol] = arg
        return arg

    def get(self, symbol):
        
        buffer = self.find(symbol)
        if not buffer:
            raise NameError("%s not found" % symbol)
        else:
            return buffer.data[symbol]