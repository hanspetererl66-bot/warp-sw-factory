import unittest

from quote_service.pricing import Quote, apply_discount


class PricingTest(unittest.TestCase):
    def test_net_price_uses_integer_cents(self):
        q = apply_discount(Quote("Q-1", 1999), 10)
        self.assertEqual(q.net_price_cents, 1799)

    def test_discount_above_max_is_rejected(self):
        with self.assertRaises(ValueError):
            apply_discount(Quote("Q-1", 1000), 41)

    def test_negative_discount_is_rejected(self):
        with self.assertRaises(ValueError):
            apply_discount(Quote("Q-1", 1000), -1)


if __name__ == "__main__":
    unittest.main()
