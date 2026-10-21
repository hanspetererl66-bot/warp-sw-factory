# Run 1: happy path

Issue to file (label `factory-ready`):

> **Discount approval.** Sales reps can apply discounts up to 10% on a quote.
> Anything above 10% must be approved by a manager before it takes effect.
> We need to know who approved what.

Expected: spec with Gherkin and open questions (for example "does 10% itself
need approval?", "what happens to a pending discount if the list price
changes?") -> Gate 1 -> plan -> Gate 2 -> implementation with tests ->
review clean -> Gate 3 (human merge) -> staging -> Gate 4 -> production.
