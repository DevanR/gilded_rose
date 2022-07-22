# -*- coding: utf-8 -*-

def aged_brie(item, original_quality):
    last_quality = item.quality

    if item.quality < 50:
        item.quality = item.quality + 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1

    return last_quality


def sulfuras(item, original_quality):
    last_quality = item.quality

    item.sell_in = item.sell_in + 1
    item.sell_in = item.sell_in - 1

    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1

    return last_quality


def backstage_pass(item, original_quality):
    last_quality = item.quality

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

    return last_quality


def conjured(item, original_quality):
    last_quality = item.quality

    if item.quality > 2:
        item.quality = item.quality - 2
    elif item.quality == 1:
        item.quality = item.quality - 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1

    return last_quality


def regular(item, original_quality):
    last_quality = item.quality

    # Reset after Promotion
    if item.sell_in == 0 and item.quality == original_quality:
        item.quality = last_quality - 2

    if item.quality > 0:
        item.quality = item.quality - 1

    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality > 0:
        item.quality = item.quality - 1

    return last_quality


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

    def update_quality(self):

        for item_index, item in enumerate(self.items):
            if item.name == "Aged Brie":
                selected_function = aged_brie
            elif item.name == "Sulfuras, Hand of Ragnaros":
                selected_function = sulfuras
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                selected_function = backstage_pass
            elif item.name == "Conjured Mana Cake":
                selected_function = conjured
            else:
                selected_function = regular

            self.last_qualities[item_index] = selected_function(item, self.original_qualities[item_index])
            self.apply_promotion(item, item_index)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)