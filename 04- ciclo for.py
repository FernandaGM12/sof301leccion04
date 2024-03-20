lista_etapas_lavado = ["llenado", "lavado", "enjuage", "Drenado", "Listo"]
for variable in lista_etapas_lavado:
    print (variable)
    if variable == "llenado" or variable == "listo":
        print ("puedo abrir la tapa")
    else:
        print ("no puede abrir la tapa, espere: ")
    print ("---------")
