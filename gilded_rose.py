# -*- coding: utf-8 -*-

def aged_brie(item, original_quality):
    if item.quality < 50:
        item.quality = item.quality + 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1

    # New Promotion Requirement
    if item.sell_in == 0:
        item.quality = original_quality


def sulfuras(item, original_quality):
    item.sell_in = item.sell_in + 1
    item.sell_in = item.sell_in - 1

    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1

    # New Promotion Requirement
    if item.sell_in == 0:
        item.quality = original_quality


def backstage_pass(item, original_quality):
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

    # New Promotion Requirement
    if item.sell_in == 0:
        item.quality = original_quality


def conjured(item, original_quality):
    if item.quality > 2:
        item.quality = item.quality - 2
    elif item.quality == 1:
        item.quality = item.quality - 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1

    # New Promotion Requirement
    if item.sell_in == 0:
        item.quality = original_quality


def regular(item, original_quality):
    if item.quality > 0:
        item.quality = item.quality - 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1

    # New Promotion Requirement
    if item.sell_in == 0:
        item.quality = original_quality


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.original_qualities = [item.quality for item in self.items]

    def get_original_price(self, item_index):
        return self.original_qualities[item_index]

    def update_quality(self):

        for item_index, item in enumerate(self.items):
            if item.name == "Aged Brie":
                aged_brie(item, self.original_qualities[item_index])
            elif item.name == "Sulfuras, Hand of Ragnaros":
                sulfuras(item, self.original_qualities[item_index])
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage_pass(item, self.original_qualities[item_index])
            elif item.name == "Conjured Mana Cake":
                conjured(item, self.original_qualities[item_index])
            else:
                regular(item, self.original_qualities[item_index])


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)