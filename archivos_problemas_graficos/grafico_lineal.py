import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("metodos\\archivos_problemas_graficos\\pd.csv")
sns.lineplot(x="fechas",y="pedidos",data=df)
plt.show()