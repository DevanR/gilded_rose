# -*- coding: utf-8 -*-

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


def regular(item, original_quality):
    if item.quality > 0:
        item.quality = item.quality - 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1




class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.original_qualities = [item.quality for item in self.items]
        self.last_qualities = [item.quality for item in self.items]

    def get_original_quality(self, item_index):
        return self.original_qualities[item_index]

    def get_last_quality(self, item_index):
        return self.original_qualities[item_index]

    def apply_promotion(self, item, item_index):
        if item.sell_in == 0:
            item.quality = self.get_original_quality(item_index)

    def was_on_promotion(self, item, item_index):
        if item.sell_in == 0 and item.quality == self.original_qualities[item_index]:
            return True
        else:
            return False

    def post_promo_reset(self, item, last_quality):
        item.quality = last_quality

    def update_quality(self):

        for item_index, item in enumerate(self.items):

            self.last_qualities[item_index] = item.quality

            if self.was_on_promotion(item, item_index):
                self.post_promo_reset(item, self.last_qualities[item_index])

            if item.name == "Aged Brie":
                aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage_pass(item)
            elif item.name == "Conjured Mana Cake":
                conjured(item)
            else:
                regular(item, self.original_qualities[item_index])

            self.apply_promotion(item, item_index)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
