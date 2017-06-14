# tuple comprehension
groupby_cols, agg_funcs = ['shop_id', 'happened_at'], [(F.sum, 'adjustment', 'dollars'), (F.count, 'adjustment', 'count')]
redeemed_df = order_transactions.where(order_transactions['kind'] == 'sale')\
                                .groupby(groupby_cols)\
                                .agg(*(func(F.col(col)).alias('redeemed_' + suf) for func, col , suf in agg_funcs))


groupby_cols, agg_funcs = ['shop_id', 'happened_at'], [F.sum, F.count]
redeemed_df = order_transactions.filter(order_transactions['gift_card_id'].isNotNull())\
                             .filter(order_transactions['kind'] == 'sale')\
                             .groupby(groupby_cols)\
                             .agg(*(f(F.col('adjustment')).alias('redeemed_' + ('dollars' if f == F.sum else 'count')) for f in agg_funcs))


# using windowing function vs sys.maxsize, 0
# much prettier
closing_balance_partions = Window.partitionBy(['shop_id']).orderBy('happened_at').rowsBetween(-sys.maxsize, 0)
closing_balance_partions = Window.partitionBy(['shop_id']).orderBy('happened_at').rowsBetween(Window.unboundedPreceding, Window.currentRow)

# cannot with withColumn on withColumn'ed columns in the same withColumn
gift_cards = with_named_columns(gift_cards, {
    'happened_at': _day_in_shop_timezone(gift_cards['created_at'], gift_cards['shop_timezone']),
    'disabled_at': _day_in_shop_timezone(gift_cards['disabled_at'], gift_cards['shop_timezone']),
    'expires_on': _day_in_shop_timezone(gift_cards['expires_on'], gift_cards['shop_timezone']),
    'current_date': _current_day_in_shop_timezone(gift_cards['shop_timezone']),
    'initial_value': (gift_cards['initial_value'] * 100).cast('long'),
    'balance': (gift_cards['balance'] * 100).cast('long'),
})
