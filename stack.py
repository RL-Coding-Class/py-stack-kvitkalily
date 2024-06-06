class Stack:
    """Provides stack container"""
    def __init__(self, typee = None):
        self.items  = []
        self.typee = typee

    def push(self, data):
        self.items.append(data)

    def pop(self):
        data = self.items[-1]
        self.items.pop()
        return data 
        

    def get(self):
        pass

    def length(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
