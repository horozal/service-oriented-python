class Model:
    def __init__(self, attribute):
        self.attribute = attribute

    def __str__(self):
        return f"Model with Attribute: {self.attribute}"

# Create an instance of the Model class
model = Model("Foo")

# Print the string representation of the Model object
print(model)

  
