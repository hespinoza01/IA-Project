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
