from services.service import Service
from models.model import Model

def main():
    service = Service()
    model = Model("Foo")
    service.print_hello(model)

if __name__ == "__main__":
    main()

