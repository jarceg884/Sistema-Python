from datetime import (datetime)
today= datetime.today()

bebidas=["Mepsi","Sorpresa espuma","7dowm","Café Frío","Capuccino","Cafe con leche","Chocolate caliente"]
precios_bebidas=[2500,1500,3000,1500,1200,1000,1350]
codigos_bebidas=[101,102,103,104,105,106,107]


comidas=["Pinto","Huevos con jamón","Pancakes","Emparedado de Carne","Nuggets felices","Pan tostado gurmet"]
precios_comidas=[4500,6000,8000,4500,7000,12500]
codigos_comidas=[201,202,203,204,205,206]

clientes=["Lola Mento","Josepth Abelarno Massimo Segundo","Cindy Nero","Maria Juana"]
celular_cliente=[60194567,60194563,60194584,60194585]
cedula_cliente=[104320771,104320766,1043207682,1043207888]

print("=====================================================")
print("Bienvenidos a la Cafetería de Vale,Kevin,Tavo y David")
print("               Cafetería Jurassic Pan                ")
print("             Es un placer atenderlos hoy             ")
print("=====================================================")


def menu_principal():
    print("Este es el menú principal, selecccione que desea realizar:")
    menu=None
    while menu!="1" and menu!="2" and menu!="3" and menu!="4" and menu!="5" and menu!="6":
        menu=input("[1] para Mantenimiento de comidas\n"
                   "[2] para Mantenimiento de bebidas\n"
                   "[3] para Mantenimiento de clientes\n"
                   "[4] para Facturar comidas y bebidas\n"
                   "[5] para Cierre de cajas\n"
                   "[6] para Salir del sistema\n"
                   "_")
        if menu=="6":
            exit()
        elif menu=="1":
            mantenimiento_de_comidas()
        elif menu=="2":
            mantenimiento_de_bebidas()
        elif menu=="3":
            mantenimiento_de_clientes()
        elif menu=="4":
            facturar_comidas_y_bebidas()
        elif menu=="5":
            cierre_de_cajas()
        elif menu=="6":
            print("Gracias por elegirnos")
            print("xdxdxdxxdxxdxdxdxdxdd")
            exit()



def mantenimiento_de_comidas():
    agregar_o_quitar=None
    while agregar_o_quitar !=1 and agregar_o_quitar!=2:
        agregar_o_quitar=int(input("Desea agregar o quitar comida?\n"
                               "[1] para agregar\n"
                               "[2] para eliminar\n"
                               "- "))
        if agregar_o_quitar==1:
            agregar_comidas()
        elif agregar_o_quitar==2:
            eliminar_comidas()
        continuar= None
        while continuar!=1 and continuar!=2:
            continuar = int(input("Desea agregar o quitar más comidas? [1]si/[2]no: "))
            if continuar == 2:
                menu_principal()
            while continuar == 1:
                mantenimiento_de_comidas()





def agregar_comidas():
    print("======================================")
    agregar=input("Añada la comida deseada: ")
    comidas.append(agregar)
    agregar=int(input("Agregue el precio: "))
    precios_comidas.append(agregar)
    agregar=int(input("Agregue el código del producto: "))
    codigos_comidas.append(agregar)
    print("La comida ha sido agregada con éxito")
    print("======================================")
    continuar = None
    while continuar != 1 and continuar != 2:
        continuar = int(input("Desea agregar más comidas? [1]si/[2]no: "))
        if continuar == 2:
            menu_principal()
        while continuar == 1:
            agregar_comidas()

def eliminar_comidas():
    print("======================================")
    print(comidas)
    print(codigos_comidas)
    eliminar_comida=None
    while eliminar_comida not in codigos_comidas:
        eliminar_comida=int(input("Digite el código de la comida para eliminar: "))
    pos_comida = codigos_comidas.index(eliminar_comida)
    comidas.pop(pos_comida)
    precios_comidas.pop(pos_comida)
    codigos_comidas.pop(pos_comida)
    print("La comida ha sido eliminada con éxito!")
    print("=======================================")
    continuar = None
    while continuar != 1 and continuar != 2:
        continuar = int(input("Desea quitar más comidas? [1]si/[2]no: "))
    if continuar == 2:
        menu_principal()
    while continuar == 1:
        eliminar_comidas()



def mantenimiento_de_bebidas():
    agregar_o_quitar=int(input("Desea agregar o quitar bebidas?\n"
                           "[1] para agregar\n"
                           "[2] para eliminar\n"
                           "- "))
    if agregar_o_quitar==1:
        agregar_bebidas()
    elif agregar_o_quitar==2:
        eliminar_bebidas()
    continuar = None
    while continuar != 1 and continuar != 2:
        continuar = int(input("Desea agregar o quitar más bebidas? [1]si/[2]no: "))
        if continuar == 2:
            menu_principal()
        while continuar == 1:
            mantenimiento_de_bebidas()

def agregar_bebidas():
    print("======================================")
    agregar=input("Añada la bebida deseada: ")
    bebidas.append(agregar)
    agregar=int(input("Agregue el precio: "))
    precios_bebidas.append(agregar)
    agregar=int(input("Agregue el código del producto: "))
    codigos_bebidas.append(agregar)
    print("La bebida ha sido agregada con éxito")
    print("======================================")
    continuar = None
    while continuar != 1 and continuar != 2:
        continuar = int(input("Desea agregar más bebidas? [1]si/[2]no: "))
        if continuar == 2:
            menu_principal()
        while continuar == 1:
            agregar_bebidas()

def eliminar_bebidas():
     print("======================================")
     print(bebidas)
     print(codigos_bebidas)
     eliminar_bebida = None
     while eliminar_bebida not in codigos_bebidas:
        eliminar_bebida=int(input("Digite el código de la bebida para eliminar: "))
     pos_bebidas = codigos_bebidas.index(eliminar_bebida)
     bebidas.pop(pos_bebidas)
     precios_bebidas.pop(pos_bebidas)
     codigos_bebidas.pop(pos_bebidas)
     print("La bebida ha sido eliminada con éxito!")
     print("=======================================")
     continuar = None
     while continuar != 1 and continuar != 2:
        continuar = int(input("Desea quitar más bebidas? [1]si/[2]no: "))
     if continuar == 2:
        menu_principal()
     while continuar==1:
         eliminar_bebidas()




def mantenimiento_de_clientes():
    agregar_o_quitar=None
    while agregar_o_quitar!=1 and agregar_o_quitar!=2:
        agregar_o_quitar=int(input("Desea agregar o quitar clientes?\n"
                               "[1] para agregar\n"
                               "[2] para eliminar\n"
                               "- "))
        if agregar_o_quitar==1:
            agregar_clientes()
        elif agregar_o_quitar==2:
            eliminar_cliente()
        continuar = int(input("Desea agregar o quitar más clientes? [1]si/[2]no: "))
        if continuar == 2:
            menu_principal()
        while continuar == 1:
            mantenimiento_de_comidas()


def agregar_clientes():
    print("======================================")
    agregar=input("Añada al cliente deseado: ")
    clientes.append(agregar)
    agregar=int(input("Agregue el celular del cliente: "))
    celular_cliente.append(agregar)
    agregar=int(input("Agregue la cédula del cliente: "))
    cedula_cliente.append(agregar)
    print("El cliente ha sido agregado con éxito")
    print("======================================")
    continuar=None
    while continuar!=1 and continuar!=2:
        continuar = int(input("Desea agregar más clientes? [1]si/[2]no: "))
        if continuar == 2:
            menu_principal()
        while continuar == 1:
            agregar_clientes()

def eliminar_cliente():
    print("======================================")
    print(clientes)
    print(celular_cliente)
    eliminar_clientes=None
    while eliminar_clientes not in celular_cliente:
        eliminar_clientes=int(input("Digite el celular del cliente para eliminar: "))
    pos_cliente = celular_cliente.index(eliminar_clientes)
    clientes.pop(pos_cliente)
    celular_cliente.pop(pos_cliente)
    cedula_cliente.pop(pos_cliente)
    print("El cliente ha sido eliminado con éxito!")
    print("=======================================")
    continuar = None
    while continuar != 1 and continuar != 2:
        continuar = int(input("Desea quitar más clientes? [1]si/[2]no: "))
        if continuar == 2:
            menu_principal()
        while continuar == 1:
            eliminar_cliente()




Ganancia_Total=[]
Ventas_Totales=[]
def facturar_comidas_y_bebidas():
    continuar = 1
    contador=0
    acumulador_total=0
    while continuar==1:
        print(clientes)
        print(celular_cliente)
        elegir_cliente=None
        while elegir_cliente not in celular_cliente:
            elegir_cliente=int(input("Marque el número del celular del cliente\n"
                                     "para facturar sus compras\n"
                                     "- "))
        pos_compra= celular_cliente.index(elegir_cliente)
        print("===========================================")
        print(comidas)
        print(codigos_comidas)
        print(bebidas)
        print(codigos_bebidas)
        print("===========================================")
        elegir_comida=None
        while elegir_comida not in codigos_comidas:
            elegir_comida =int(input("Elija la comida del cliente por el código: "))
        pos_comida=codigos_comidas.index(elegir_comida)
        elegir_bebida=None
        while elegir_bebida not in codigos_bebidas:
            elegir_bebida=int(input("Elija la bebida del cliente por el código: "))
        pos_bebida=codigos_bebidas.index(elegir_bebida)
        acumulador_clientes = precios_bebidas[pos_bebida]+precios_comidas[pos_comida]
        print("=============================================")
        print(today.day,"/",today.month,"/",today.year,"-",today.hour,":",today.minute,":",today.second,"HORAS")
        print("Factura de Cliente:                          ")
        print(clientes[pos_compra]                           )
        print(comidas[pos_comida],":",precios_comidas[pos_comida],"colones")
        print(bebidas[pos_bebida],":",precios_bebidas[pos_bebida],"colones")
        print("MONTO A PAGAR:",precios_bebidas[pos_bebida]+precios_comidas[pos_comida],"colones")
        print("============================================")
        continuar = None
        while continuar != 1 and continuar != 2:
            continuar = int(input("Desea seguir facturando? [1]si/[2]no: "))
            contador+=1
        acumulador_total=acumulador_total+acumulador_clientes
    Ventas_Totales.append(contador)
    Ganancia_Total.append(acumulador_total)
    print("Esta es la cantidad total: ", acumulador_total)
    print("========================================")
    menu_principal()
    return acumulador_total





def cierre_de_cajas():
    print("==========================================================================")
    print("=================Las ventas y ganancias totales son:======================")
    print("==================",Ventas_Totales,"Ventas en total====================================")
    print("==================",Ganancia_Total, "Ganancia en total===============================")
    print("=========================Gracias por su trabajo===========================")
    print("==========================================================================")
    print("Gracias por elegirnos")
    continuar=None
    while continuar!=1 and continuar!=2:
        continuar=input("Desea pasar al día siguiente o salir del sistema?\n"
              "[1] Para pasar al día siguiente\n"
              "[2] Para salir del sistema\n"
              "- ")
        if continuar=="1":
            Ventas_Totales.clear()
            Ganancia_Total.clear()
            print("=============================")
            print("        Buenos Días          ")
            print("=============================")
            menu_principal()
        elif continuar=="2":
            exit()
menu_principal()
