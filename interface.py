import abc


def aged_brie(item):
    if item.quality < 50:
        item.quality = item.quality + 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1


def sulfuras(item):
    item.sell_in = item.sell_in + 1
    item.sell_in = item.sell_in - 1

    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1


def backstage_pass(item):
    item.quality = item.quality + 1
    if item.sell_in < 11:
        if item.quality < 50:
            item.quality = item.quality + 1
    if item.sell_in < 6:
        if item.quality < 50:
            item.quality = item.quality + 1
    if item.sell_in <= 0:
        item.quality = 0

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1


def conjured(item):
    if item.quality > 2:
        item.quality = item.quality - 2
    elif item.quality == 1:
        item.quality = item.quality - 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1


def regular(item):
    if item.quality > 0:
        item.quality = item.quality - 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1


ITEM_UPDATE_FUNCTIONS = {
    "Aged Brie": aged_brie,
    "Sulfuras, Hand of Ragnaros": sulfuras,
    "Backstage passes to a TAFKAL80ETC concert": backstage_pass,
    "Conjured Mana Cake": conjured,
    "foo": regular
}


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class UpdatableItemInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    def update_quality(self, item: Item):
        raise NotImplementedError


class UpdatableItem(Item, UpdatableItemInterface):
    def __init__(self, name, sell_in, quality):
        super(UpdatableItem, self).__init__(name, sell_in, quality)
        self._update_quality = ITEM_UPDATE_FUNCTIONS[self.name]

    def update_quality(self, item: Item):
        self._update_quality(self)
