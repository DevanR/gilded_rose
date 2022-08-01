# -*- coding: utf-8 -*-

def post_promo_reset(item, last_quality):
    item.quality = last_quality


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

    def update_quality(self):

        for item_index, item in enumerate(self.items):

            self.last_qualities[item_index] = item.quality

            if self.was_on_promotion(item, item_index):
                post_promo_reset(item, self.last_qualities[item_index])

            item.update_quality(item)

            self.apply_promotion(item, item_index)

