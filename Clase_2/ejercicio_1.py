saldo = 0

print("Bienvenido a su cajero de confianza")
def menu_inicial():
    print("Si desea realizar un DEPOSITO apriete ------> 1")
    print("Si desea realizar una EXTRACCION apriete ---> 2")
    print("Si desea realizar un TRANFERENCIA apriete --> 3")
    print("Si desea SALIR apriete ---------------------> 4")

eleccion = 0
while (eleccion != "4"):
    menu_inicial()
    eleccion = input()
    if eleccion == "1":
        monto_depositar = int(input("Ha elegido depositar, ingrese el monto: "))
        saldo += monto_depositar
        print("Su Saldo actual es: ", saldo)
    elif eleccion == "2":
        monto_extraer = int(input("Ha elegido extraer, ingrese el monto: "))
        saldo -= monto_extraer
        print("Su Saldo actual es: ", saldo)
    elif eleccion == "3":
        monto_transferir = int(input("Ha elegido transferir, ingrese el monto: "))
        saldo -= monto_transferir
        print("Su Saldo actual es: ", saldo)
    else:
        print("No ha ingresado una opcion correcta, intente nuevamente")


    
