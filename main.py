from app.services.service import Service
from app.models.model import Model

def main():
    service = Service()
    model = Model("Foo")
    service.print_hello(model)

if __name__ == "__main__":
    main()

