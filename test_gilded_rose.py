# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from interface import UpdatableItem


class GildedRoseTest(unittest.TestCase):
    def test_item_quality_decreases(self):
        items = [UpdatableItem("foo", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_item_quality_is_never_negative(self):
        items = [UpdatableItem("foo", 2, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)

    def test_item_quality_degrades_twice_past_sell_in_date(self):
        items = [UpdatableItem("foo", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_aged_brie_quality_does_not_exceed_fifty(self):
        items = [UpdatableItem("Aged Brie", 3, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(48, items[0].quality)

    def test_sulfuras_quality_does_not_vary(self):
        items = [UpdatableItem("Sulfuras, Hand of Ragnaros", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(2, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_backstage_quality_increases_twice_ten_to_six(self):
        items = [UpdatableItem("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(20, items[0].quality)

    def test_backstage_quality_increases_thrice_five_to_1(self):
        items = [UpdatableItem("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(26, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(29, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(32, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(20, items[0].quality)
        gilded_rose.update_quality()

    def test_backstage_quality_zeros_at_sell_in(self):
        items = [UpdatableItem("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_quality_stays_zero_past_sell_in(self):
        items = [UpdatableItem("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_quality_degrades_twice(self):
        items = [UpdatableItem("Conjured Mana Cake", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)
        self.assertEqual(4, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(3, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(2, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

    def test_get_item_original_price(self):
        items = [UpdatableItem("Conjured Mana Cake", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.get_original_quality(0), 5)

    def test_promotion_price_on_last_day(self):
        items = [UpdatableItem("foo", 3, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(5, items[0].quality)


if __name__ == '__main__':
    unittest.main()
