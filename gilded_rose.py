# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def apply_promotion(self, item):
        if item.sell_in == 0:
            item.quality = item.original_quality

    def was_on_promotion(self, item):
        if item.sell_in == 0 and item.quality == item.original_quality:
            return True
        else:
            return False

    def update_quality(self):

        for item_index, item in enumerate(self.items):

            item.update_quality(item)

            if self.was_on_promotion(item):
                item.quality = item.last_quality

            self.apply_promotion(item)

