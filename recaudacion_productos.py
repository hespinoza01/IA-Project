"""
    Recaudación venta productos
"""
import main

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