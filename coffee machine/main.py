MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def ingredientesSuficientes(tipoCafe):
    """Delvuelve True si es posible hacer el cafe False en su defecto"""
    for ingrediente in tipoCafe:
        if tipoCafe[ingrediente]>resources[ingrediente]:
            print(f"Lo siento no hay suficiente{ingrediente}.")
            return False
    return True

def saldo():
    """Devuelve el saldo disponible para comprar"""
    print("Por favor inserta monedas.")
    total=int(input("Cuantos cuartos: "))*0.25
    total+=int(input("Cuantas monedas de 10 centavos: "))*0.1
    total+=int(input("Cuantas monedas de 5 centavos: "))*0.05
    total+=int(input("Cuantos centavos: "))*0.01

    return total

def compraExitosa(dinero,costoBebida):
    """Devuelve True si se acepto el pago  o False si el dinero es insuficiente """
    if dinero>=costoBebida:
        cambio=round(dinero-costoBebida,2)
        print("**************************************")
        print(f"Aqui tienes {cambio} de cambio.")
        global profit
        profit+=costoBebida
        return True
    else:
        print("Lo siento dinero insuficiente. Dinero devuelto")
        return False

def preparaCafe(bebidaDeseada,ingredientes):
    """Resta los ingredientes a la bebida hecha"""
    for ingrediente in ingredientes:
        resources[ingrediente]-=ingredientes[ingrediente]
    print(f"Aquí tienes tu {bebidaDeseada} ☕️. Disfrutalo!")

prendida=True

while prendida:
    quiero=input("""
    ¿Qué te gustaría beber?
        'espresso'
        'latte'
        'cappuccino'
    (tambien puede escribir 'apagar' para apagar la cafetera o 'reporte ' para ver los recursos disponibles)
    : """).lower()
    if quiero=='apagar':
        prendida=False
    elif quiero=='reporte':
        print("\n*********************************")
        print(f"Agua: {resources['water']}ml")
        print(f"Leche: {resources['milk']}ml")
        print(f"Café: {resources['coffee']}g")
        print(f"Dinero: ${profit}")
    else:
        bebida=MENU[quiero]
        if ingredientesSuficientes(bebida["ingredients"]):
            pagar=saldo()
            if compraExitosa(pagar,bebida["cost"]):
                preparaCafe(quiero,bebida["ingredients"])


