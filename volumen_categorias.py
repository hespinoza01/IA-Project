"""
    Volumen categorías
"""
import pandas as pd
import os

# Nombres de las columnas del data_frame
names = ['product_id', 'product_name', 'supplier_id', 'category_id', 'quantity_per_unit', 'unit_price', 'units_in_stock', 'units_on_order', 'reorder_revel', 'discontinued', 'category_id_detail', 'category_name', 'description', 'picture']

# Carga del data_frame
data = pd.read_csv(
f"{os.getcwd()}/products.csv", header=None, index_col=False, names=names)

# Se limpia el data_frame y solo se muestran las columnas necesarias
name_dummies = ['product_id', 'product_name', 'category_id', 'discontinued', 'category_name']

data = data[[*name_dummies]]

categorys = data.groupby('category_id')['product_id'].agg(list)

# Se calcula el volumen por categoría
category_volumen = []
for rkey, row in categorys.iteritems():
    category_volumen.append(len(row))
    
categorys = pd.DataFrame({'category_id': categorys.index, 'product_id': categorys.values})
categorys = categorys.assign(category_volumen=category_volumen)
categorys = categorys.drop('product_id', 1)

display(categorys)
categorys.plot(x='category_id', y='category_volumen', kind='bar')