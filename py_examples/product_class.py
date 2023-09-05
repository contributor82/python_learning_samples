""""Module for product"""
class Product:
    """product class """
    product_id: int
    name: str
    unit_price: float
    quantity: int

    def __init__(self) -> None:
        """Initializing class members """
        self.product_id=0
        self.name=''
        self.unit_price = 0.0
        self.quantity =0

    def get_product_stock(self) -> dict[str, int | str]:
        """Get Product Stock """
        return {"product_id": self.product_id, "name": self.name, "quantity": self.quantity}

    def display_product_dtls(self)-> None:
        """Display product details """
        print("Product ID: ", self.product_id,
              "Name: ", self.name,
              "Unit Price:", self.unit_price,
              "Quantity: ", self.quantity)



if __name__ == '__main__':
    prod_instance = Product()
    print(prod_instance.get_product_stock())
