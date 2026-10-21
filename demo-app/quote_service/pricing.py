"""Quote pricing. Money is integer cents, never floats."""

from dataclasses import dataclass

MAX_DISCOUNT_PCT = 40


@dataclass(frozen=True)
class Quote:
    quote_id: str
    list_price_cents: int
    discount_pct: int = 0

    @property
    def net_price_cents(self) -> int:
        return self.list_price_cents * (100 - self.discount_pct) // 100


def apply_discount(quote: Quote, discount_pct: int) -> Quote:
    """Return a copy of the quote with the discount applied.

    The factory demo feature adds an approval rule on top of this function:
    discounts above a threshold must be approved by a manager.
    """
    if not 0 <= discount_pct <= MAX_DISCOUNT_PCT:
        raise ValueError(f"discount must be between 0 and {MAX_DISCOUNT_PCT}")
    return Quote(quote.quote_id, quote.list_price_cents, discount_pct)
