from app.models.model import Model

model = Model("Foo")

class Service:
    def __init__(self):
        pass

    def print_hello(self, model):
        self.model = model
        print(f"Hello, {model}!")






