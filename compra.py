'''0 > valorCompra < 100.000 -> 0%
   100.000 >= valorCompra <=200.000 ->'''


def total(valorCompra):
    valorCompra = float(input("Valor de la comprar"))
    if valorCompra < 100000:
        descuento = 0.0
    elif valorCompra >= 200000:
        descuento = 0.01
    elif valorCompra >= 500000:
        descuento = 0.05
        
    return valorCompra*(1-descuento)

print("El valor es",total(valorCompra))
