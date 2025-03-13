class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []
    
    def add(self, child):
        self.children.append(child)
        return self
    
    def operation(self):
        return f"Coposite({', '.join([c.operation() for c in self.children])})"

if __name__ == "__main__":
    root = Composite()\
        .add(Composite()\
             .add(Leaf())\
             .add(Composite()\
                  .add(Leaf())\
                  .add(Leaf())))\
        .add(Leaf())
    print(root.operation())
    
