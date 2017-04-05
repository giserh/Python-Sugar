"""
    Using the map function in python, you can map the select(cols) function to every dataframe in the dfs array.
    Then using reduce, you can union each df in the dfs array one at a time.
    #Python Sugar
"""

# ugly way of doing it
gift_cards_issued = with_named_columns(gift_cards_issued, {
    'disabled_amount': F.lit(0).cast('long'),
    'redeemed_amount': F.lit(0).cast('long'),
    'refunded_amount': F.lit(0).cast('long'),
})

gift_cards_disabled = with_named_columns(gift_cards_disabled, {
    'issued_amount': F.lit(0).cast('long'),
    'sold_amount': F.lit(0).cast('long'),
    'redeemed_amount': F.lit(0).cast('long'),
    'refunded_amount': F.lit(0).cast('long'),
})

gift_cards_redeemed = with_named_columns(gift_cards_redeemed, {
    'issued_amount': F.lit(0).cast('long'),
    'sold_amount': F.lit(0).cast('long'),
    'refunded_amount': F.lit(0).cast('long'),
    'disabled_amount': F.lit(0).cast('long'),
})

gift_cards_refunded = with_named_columns(gift_cards_refunded, {
    'issued_amount': F.lit(0).cast('long'),
    'sold_amount': F.lit(0).cast('long'),
    'redeemed_amount': F.lit(0).cast('long'),
    'disabled_amount': F.lit(0).cast('long'),
})

cols = ['shop_id', 'gift_card_id', 'happened_at', 'currency', 'issued_amount', 'sold_amount', 'disabled_amount',  'redeemed_amount', 'refunded_amount']

return gift_cards_issued.select(cols).union(gift_cards_disabled.select(cols))\
                        .select(cols).union(gift_cards_redeemed.select(cols))\
                        .select(cols).union(gift_cards_refunded.select(cols))\
                        .withColumnRenamed('happened_at', 'rollup_date')\
                        .select(self.OUTPUT.column_names())

# pretty way of doing it
gift_cards_issued = with_named_columns(gift_cards_issued, {
    'disabled_amount': F.lit(0).cast('long'),
    'redeemed_amount': F.lit(0).cast('long'),
    'refunded_amount': F.lit(0).cast('long'),
})

gift_cards_disabled = with_named_columns(gift_cards_disabled, {
    'issued_amount': F.lit(0).cast('long'),
    'sold_amount': F.lit(0).cast('long'),
    'redeemed_amount': F.lit(0).cast('long'),
    'refunded_amount': F.lit(0).cast('long'),
})

gift_cards_redeemed = with_named_columns(gift_cards_redeemed, {
    'issued_amount': F.lit(0).cast('long'),
    'sold_amount': F.lit(0).cast('long'),
    'refunded_amount': F.lit(0).cast('long'),
    'disabled_amount': F.lit(0).cast('long'),
})

gift_cards_refunded = with_named_columns(gift_cards_refunded, {
    'issued_amount': F.lit(0).cast('long'),
    'sold_amount': F.lit(0).cast('long'),
    'redeemed_amount': F.lit(0).cast('long'),
    'disabled_amount': F.lit(0).cast('long'),
})

cols = ['shop_id', 'gift_card_id', 'happened_at', 'currency', 'issued_amount', 'sold_amount', 'disabled_amount',  'redeemed_amount', 'refunded_amount']
dfs = [gift_cards_issued, gift_cards_disabled, gift_cards_redeemed, gift_cards_refunded]
dfs = map(lambda df : df.select(*cols), dfs)

return reduce(lambda a, b : a.union(b), dfs).withColumnRenamed('happened_at', 'rollup_date')\
                                            .select(self.OUTPUT.column_names())
