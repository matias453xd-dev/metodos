#Sin usar pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Matplotlib
plt.plot(x, y, label='Valores')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico con listas')
plt.legend()
plt.show()

# Seaborn
sns.scatterplot(x=x, y=y)
plt.title('Gráfico de dispersión con listas')
plt.show()
