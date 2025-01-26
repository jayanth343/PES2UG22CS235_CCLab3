import json
from typing import List, Union
import products
from cart import dao
from products import Product


class Cart:
    def _init_(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> 'Cart':
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> List[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    all_product_ids = []
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        product_ids = json.loads(contents)  # Replace eval with json.loads
        all_product_ids.extend(product_ids)

    products_data = products.get_products(all_product_ids) 
    return products_data


def add_to_cart(username: str, product_id: int) -> None:
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int) -> None:
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str) -> None:
    dao.delete_cart(username)