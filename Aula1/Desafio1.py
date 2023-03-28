from pandas import *
import matplotlib.pyplot as plt

bogota_data = read_csv(r"C:\Users\luis_\Escritorio\InmersionDatos\Aula1\DB\inmuebles_bogota.csv")

barrios_bogota = bogota_data.groupby('Barrio')

area_promedio = barrios_bogota.mean()['Área']

area_promedio_desc = area_promedio.sort_values(ascending=False)

area_promedio_desc.head(10).plot(kind='bar')
plt.show()


Areas_inmuebles_bogota = bogota_data['Área']
AreaMinima = Areas_inmuebles_bogota.min()
AreaMaxima = Areas_inmuebles_bogota.max()
AreaPromedio = Areas_inmuebles_bogota.mean()
AreaMediana = Areas_inmuebles_bogota.median()


print("El area minima de los inmuebles es: ", AreaMinima)
print("El area maxima de los inmuebles es: ", AreaMaxima)
print("El area promedio de los inmuebles es: ", AreaPromedio)
print("El area mediana de los inmuebles es: ", AreaMediana)