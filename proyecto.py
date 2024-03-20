opcion_general = "Si"
total_ventas_del_dia= 0
total_helados_vendidos = 0
total_batidos_vendidos =0 
while opcion_general =="Si":
    print ("Bienvenido al sistema de pago de la POPS®")
    print ( "Pedido del cliente")
    print ("Ingrese el apellido del cliente")
    apellido = input()
    print ("Tiene tarjeta PuraVidaPOPS")
    t = input ()
    print ("Ingrese la cantidad de helados: ")
    ch = int (input ())
    print ("Ingrese el sabor del helado: ")
    sa = input () 
    if sa == "vainilla":
        h = ch * 600
    elif sa == "chocolate":
            h = ch * 700
    elif sa == "caramelo":
            h = ch * 750
    else:
        h = ch * 800
    print ("Ingrese la cantidad de batidos: ")
    ba = int (input ())
    print ("Ingrese la cantidad de futas: ")
    fr = int (input ())
    if fr == 1:
        bati = ba * 1200
    elif fr == 2:
        bati = ba * 1300
    else:
        bati = ba *1400
    print ("La cuenta total del cliente es: ")
    print ( str (h) + " colones por helados" )
    print (str (bati) +  " colones por batidos")
    pre = h + bati
    print ("Total sin descuento:" + str(pre) + " colones")
    if apellido == "Alvarado":
        total = pre * 0.10
    else:
        total = pre * 0
    print ( "Descuento por apellido del día: " + str ( total ))
    if t == "si":
        ut = pre * 0.15
    else:
        ut = pre * 0
    print (( "Descuento por PuraVidaPOPS: " + str ( ut )))
    final = pre - total - ut
    print ("Total a pagar " + str (final) + " colones")

    total_ventas_del_dia += final
    total_helados_vendidos += ch
    total_batidos_vendidos += ba

    opcion_general = input ("Desea atender a otro cliente (Si/No):")

print ("Reporte final del dìa para Heladeria POPS®")
print ("-----------------------")
print ("Total de ventas del dia: " + str (total_ventas_del_dia) + " colones ")
print("Total de helados vendidos: " + str(total_helados_vendidos))
print ("Total de batidos vendidos: " + str ( total_batidos_vendidos))