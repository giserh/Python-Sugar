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

gc_df = with_named_columns(gift_cards, {
    'issued_dollar': F.when(gift_cards['line_item_id'].isNull(), gift_cards['initial_value']).otherwise(0),
    'issued_count': F.when(gift_cards['line_item_id'].isNull(), 1).otherwise(0),
    'sold_dollar': F.when(gift_cards['line_item_id'].isNotNull(), gift_cards['initial_value']).otherwise(0),
    'sold_count': F.when(gift_cards['line_item_id'].isNotNull(), 1).otherwise(0),
})

# using the sql.function.when <3
gc_df = with_named_columns(gift_cards, {
    'issued_dollar': F.when(gift_cards['line_item_id'].isNull(), gift_cards['initial_value']).otherwise(0),
    'issued_count': F.when(gift_cards['line_item_id'].isNull(), 1).otherwise(0),
    'sold_dollar': F.when(gift_cards['line_item_id'].isNotNull(), gift_cards['initial_value']).otherwise(0),
    'sold_count': F.when(gift_cards['line_item_id'].isNotNull(), 1).otherwise(0),
})

# can join twice
return issued_df.join(disabled_df, groupby_cols, how='outer')\
                .join(expired_df, groupby_cols, how='outer')\
                .fillna(long(0))\
                .select(self.OUTPUT.column_names())

# filtering on multiple values.
# filtering with multiple expressions.
order_transactions = order_transactions.where((F.col('gift_card_id').isNotNull()) &
                                                      (F.col('status') == 'success') &
                                                      (order_transactions['kind'].isin(F.lit('refund'), F.lit('sale'), F.lit('capture'))))


# union hack
df1.union(df2.select(*df1.columns))


# this is a trick to use dataframe methods on column object.
# date_format returns a column object, but if you do a select on it, it becomes a 
# dataframe variable, thus collect is able to work on the column object.
df = spark.createDataFrame([('2015-04-08',)], ['a'])
df.select(date_format('a', 'MM/dd/yyy').alias('date')).collect()
# [Row(date=u'04/08/2015')]
