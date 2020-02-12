"""
    Volumen de productos vendidos
"""
products_group = data.groupby('product_id')['quantity'].agg(list)
display(products_group.head())