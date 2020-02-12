# -*- coding: utf-8 -*-
import pandas as pd
import os


# Nombres de las columnas del data_frame
names=['order_id', 'customer_id', 'employee_id', 'order_date','required_date', 'shipped_date', 'ship_via', 'freight', 'ship_name', 'ship_address', 'ship_city', 'ship_region', 'ship_postal_code', 'ship_country', 'order_id_detail', 'product_id', 'init_price', 'quantity', 'discount']

# Carga del data_frame
data = pd.read_csv(
f"{os.getcwd()}/orders.csv", header=None, index_col=False, names=names)


# Se limpia el data_frame y solo se muestran las columnas necesarias
names_dummies = ['order_id', 'customer_id', 'order_date', 'order_date', 'product_id', 'init_price', 'quantity', 'discount']

data = data[[*names_dummies]]

#print(data.product_id.value_counts())

#print(f"Columnas originales: {list(data.columns)}\n")
"""
data_dummies = pd.get_dummies(data)

print(f"Columnas dummies: {list(data_dummies.customer_id_ANTON.values)}")"""


# Se calcula el total recaudado por orden y se añada una nueva columna al data_frame de esos totales
total = []
for key, value in data.iterrows():
    res = value.init_price * value.quantity - value.discount
    total.append(res)
    
data = data.assign(total=total)

products_group = data.groupby('product_id')['total'].agg(list)

# display(products_group)
# print(len(products_group))

# Se agrupan las recaudaciones por ID de producto para calcular la recaudación de cada uno
products_recaudation = []
i = 0
for rkey, row in products_group.iteritems():
    products_recaudation.append(sum(row))
    
products_group = pd.DataFrame({'product_id': products_group.index, 'product_total': products_group.values}, columns=['product_id', 'product_total'])
products_group = products_group.assign(product_recaudacion=products_recaudation)

products_group.plot(y='product_recaudacion', x='product_id', kind='bar')

products_group = products_group.sort_values('product_recaudacion', ascending=False)


# Se determina el top 10 de productos con mayor recaudación
top_products = products_group[0:10]
top_products = top_products.drop('product_total', 1)

# Se muestran los resultados de la recaudacion de productos y el top 10 de productos
display(top_products.head())
                   
top_products.plot(y='product_recaudacion', x='product_id', kind='bar')