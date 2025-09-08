import pandas as pd

#Dataframe

data={
    "Piezas" : ["Patas", "Ruedas", "Tablero" ,"Puertas", "Tornillos"],
    "Centimetros" : [40, 15, 80, 10, 50],
}

df = pd.DataFrame(data)
df.to_excel("mobiles_medidas.xlsx", index=False)
