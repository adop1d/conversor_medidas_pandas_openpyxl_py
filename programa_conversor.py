import pandas as pd

def centimetros_a_pulgadas(cm):
    return cm / 2.54

df=pd.read_excel("mobiles_medidas.xlsx")

df["Pulgadas"] = df["Centimetros"].apply(centimetros_a_pulgadas)
df.to_excel("mobiles_medidas_convertidas.xlsx", index=False)

print("Archivo creado exitosamente: mobiles_medidas_convertidas.xlsx")