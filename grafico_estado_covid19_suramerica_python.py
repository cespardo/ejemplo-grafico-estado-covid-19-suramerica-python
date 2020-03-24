import math
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

plt.figure('Muertes covid-19 SA')

confirmados = [277, 77, 981, 363, 1629, 27, 746, 266, 158, 22, 19, 5, 20, 51]
plt.plot(confirmados)   # Dibuja el gráfico
plt.show()

#Creo la lista 2 con 8 datos
muertes = [3, 0, 18, 5, 25, 0, 2, 4, 0, 1, 1, 0, 0, 0]
plt.plot(muertes)   # No dibuja datos de lista2
plt.show()

recuperados = [3, 15, 3, 1, 2, 0, 11, 27, 0, 0, 0, 0, 6, 0]
plt.plot(recuperados)   # No dibuja datos de lista2
plt.show()

activos = [271, 62, 960, 357, 1602, 27, 733, 235, 158, 27, 18, 5, 14, 51]
plt.plot(activos)   # No dibuja datos de lista2
plt.show()

#Leyendas
plt.xlabel("Países")   # Inserta el título del eje X 
plt.ylabel("Cantidad de personas")   # Inserta el título del eje Y
plt.title("Estado del COVID-19 en países de Sur América")   # Establece nuevo título pero no muestra en gráfico
plt.plot(confirmados, marker='x', linestyle=':', color='b', label = "Confirmados") #Asigna una leyenda a los datos de la lista 1
plt.plot(muertes, marker='*', linestyle='--', color='r', label = "Muertes")
plt.plot(recuperados, marker='h', linestyle=':', color='g', label = "Recuperados")
plt.plot(activos, marker='', linestyle=':', color='m', label = "Activos")

plt.legend(loc = "upper right") #Permite que las leyendas se muestren

indice = np.arange(14)   # Declara un array
plt.xticks(indice, ("COL", "VEN", "ECU", "PER", "BRA", "BOL", "CHI", "ARG", "URU", "PAR", "GUY", "SUR", "GFR", "TYT"))   


#Activar cuadrícula
plt.grid(color='k',linestyle='--',linewidth=1)  # Activa cuadrícula del gráfico pero no se muestra

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

fig = go.Figure(data=[go.Table(header=dict(values=['País', 'Confirmados', 'Muertes', 'Recuperados', 'Activos']),
                 cells=dict(values=[['COL', 'VEN', 'ECU', 'PER', 'BRA', 'BOL', 'CHI', 'ARG', 'URU', 'PAR', 'GUY', 'SUR', 'GFR', 'TYT'], confirmados, muertes, recuperados, activos]))
                     ])
fig.show()

#Activo el modo interactivo de dibujo
plt.show()
