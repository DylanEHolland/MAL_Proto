class Env:

    def __init__(self, outer = None):
        self.data = {}
        self.outer = outer

    def find(self, symbol):
        if symbol in self.data:
            return self.data
        else:
            if self.outer is not None:
                self.outer.find(symbol)
            else: 
                raise NameError("Function not found")

    def set(self, symbol, arg):
        self.data[symbol] = arg

    def get(self, symbol):
        
        buffer = self.find(symbol)
        return buffer[symbol]