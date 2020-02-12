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
    
products_group = products_group.to_frame()
products_group = products_group.assign(recaudacion=products_recaudation)
products_group = products_group.sort_values('recaudacion', ascending=False)


# Se determina el top 10 de productos con mayor recaudación
top_products = products_group[0:10]
top_products = top_products.drop('total', 1)

# Se muestran los resultados de la recaudacion de productos y el top 10 de productos
display(top_products.head())
ax = top_products.hist(column='recaudacion', bins=25, grid=False, figsize=(12,8), layout=(2,1), sharex=True, color='#86bf91', zorder=2, rwidth=0.9)
          
# Se modifican los estilos para el histograma
ax = ax[0]
for x in ax:

    # Despine
    x.spines['right'].set_visible(False)
    x.spines['top'].set_visible(False)
    x.spines['left'].set_visible(False)

    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    # Remove title
    x.set_title("")

    # Set x-axis label
    x.set_xlabel("Recaudación ($)", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    x.set_ylabel("ID Producto", labelpad=20, weight='bold', size=12)

    # Format y-axis label
    #x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))
                    