from dataclasses import dataclass


@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
       TODO реализуйте метод покупки
           Проверьте количество продукта используя метод check_quantity
           Если продуктов не хватает, то выбросите исключение ValueError
       """
        if self.check_quantity(quantity) is True:
            self.quantity -= quantity
            return self.quantity
        else:
            raise ValueError('Не хватает продуктов')

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """

    def remove_product(self, product: Product, quantity=None):
        if product in self.products:
            if quantity is None or quantity >= self.products[product]:
                del self.products[product]
            else:
                self.products[product] -= quantity

        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0.0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price

    def buy(self):
        for product, quantity in self.products.items():
            if product.check_quantity(quantity):
                product.buy(quantity)
            else:
                raise ValueError("Не хватает продуктов")
