import pandas as pd
df = pd.read_csv("metodos\\ejercicios1\\archivos.csv")
print(df)
# Convertir un tipo de dato a otro
df["edad"] = df["edad"].astype(str)
# Reemplazar un dato con otro, dalto por maestro
df['apellido'].replace("dalto","maestro",inplace=True)
