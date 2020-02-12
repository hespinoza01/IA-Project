"""
    Volumen de productos vendidos
"""
from main import data, pd

# Se agrupan los priductos por ID y se registran los cantidades de cada orden realizada
products = data.groupby('product_id')['quantity'].agg(list)
#display(products.head())

# Se calcula el volumen total por producto
product_volume = []
for rkey, row in products.iteritems():
    product_volume.append(sum(row))

products = pd.DataFrame({'product_id': products.index, 'product_quantity': products.values}, columns=['product_id', 'product_quantity'])

# Se añade la columna de los volumenes totales en el data frame
products = products.assign(product_volume=product_volume)

# Se dibuja la gráfica del volumen vendido para cada producto
products.plot(x='product_id', y='product_volume', kind='bar')
products = products.sort_values('product_volume', ascending=False)
#display(products)

# Se determina el top 10 de volumenes vendidos
top_products = products[0:10]
top_products = top_products.drop('product_quantity', 1)

display(top_products)
top_products.plot(x='product_id', y='product_volume', kind='bar')