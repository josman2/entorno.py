import pandas as pd
datoSerie = pd.Series(["logica","Moviles","Base de datos","html"],index=["nota1","nota2","nota3","nota4"], dtype="string")
print(datoSerie)

#creando serie a partir de un diccionario
s = pd.Series({"logica":3.5,"moviles": 1.3, "bases de datos": 5.0})
print(s)


datos = ({"Nombre": "karina", "Apellido": "valencia", "sexo": "femenino"})
datoSerie = pd.Series(datos)
print(datoSerie)
