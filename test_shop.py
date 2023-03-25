"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    cart = Cart()
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        product.buy(1000)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_new_product(self, product, cart):
        cart.add_product(product, 5)
        assert cart.products[product] == 5

    def test_add_exist_product(self, product, cart):
        cart.add_product(product, 5)
        cart.add_product(product, 5)
        assert cart.products[product] == 10
        assert len(cart.products.items()) == 1

    def test_clear(self, product, cart):
        cart.add_product(product, 5)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 5)
        total_price = cart.get_total_price()
        assert total_price == 500

    def test_remove_products_without_quantity(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert len(cart.products.items()) == 0

    def test_remove_products_with_quantity(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product, 5)
        assert len(cart.products.items()) == 0

    def test_remove_higher_count_products(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product, 10)
        assert len(cart.products.items()) == 0

    def test_remove_less_products(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product, 2)
        assert cart.products[product] == 3

    def test_buy_all(self, product, cart):
        cart.add_product(product, 10)
        cart.buy()
        assert cart.products[product] == 10

    def test_buy_more_than_have(self, product, cart):
        with pytest.raises(ValueError):
            cart.add_product(product, 1001)
            cart.buy()
