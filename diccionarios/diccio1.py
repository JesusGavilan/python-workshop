#inicializando
mi_diccionario = {"nexus5": "android kitkat", "iphone5c": "iOS 7", "nokia 920":"WP8"}
print mi_diccionario
#update
mi_diccionario.update({"geeksphone keon":"firefox OS"})
mi_diccionario.update({"Blackberry Z30":"Blackberry 10.2"})
print mi_diccionario
#obtner value pasando key
value =  mi_diccionario.get("iphone5c")
print value
#tamany
print len(mi_diccionario)
#eliminar valor
del mi_diccionario["Blackberry Z30"]
print mi_diccionario
#true if exists
print "nexus5" in mi_diccionario
#true if does not exists
print "bq" not in mi_diccionario
