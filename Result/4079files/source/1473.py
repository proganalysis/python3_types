from core.item import Item

class Item(Item):
    def __init__(self):
        pass
    def __str__(self) -> str:
        return " ".join(map(str, self.items))

    def __repr__(self) -> str:
        return " ".join(map(str, self.items))