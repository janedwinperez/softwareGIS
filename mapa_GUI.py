import geopandas as gpd
import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
from pandastable import Table, TableModel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import warnings
warnings.filterwarnings("ignore")

"""
#Cargamos la capa tematica
map_data = gpd.read_file("./natalidad.geojson")
#print(map_data.head())

# Control del tamaño de la figura del mapa
fig, ax = plt.subplots(figsize=(10, 10))

# Control del título y los ejes
ax.set_title('Natalidad por Provincias en España, 2018', pad = 20, fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')

# Mostrar el mapa finalizado
map_data.plot(column='NAT2018', cmap='plasma', ax=ax, zorder=5)
plt.show()
"""
#***********************************************************************************************************************
"""
europa_gdf = gpd.read_file("./Europe/Europe.shp")
print(europa_gdf.head())

#Borramos la columna "ORGN_NAME"
europa_gdf = europa_gdf.drop('ORGN_NAME', axis = 1)
print("x"*32)
print(europa_gdf.head())

percapita_df = pd.read_csv("./percapita.csv")
#Se agrega la columna de datos cuantitativos
europa_gdf["percapita"] = percapita_df["percapita"]

#europa_gdf.plot(column = 'percapita', cmap = 'gist_rainbow')
#plt.show()

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111)
#Título del mapa
title = 'PIB Per Capita (USD) de los países de Europa'
#Impresión del título indicando un renglón entre la figura y el #texto
plt.title(title + '\n', fontsize=19)
#Impresión del mapa indicando qué marco(ax) debe tomar de referencia
europa_gdf.plot(column='percapita', cmap = 'gist_rainbow', ax = ax)
#Nombre de los ejes horizontal y vertical
ax.set_xlabel('Longitud', fontsize = 13)
ax.set_ylabel('Latitud', fontsize = 13)
#Definición de los valores mínimo y máximo como límites de la barra #a utilizar
min_p = min(europa_gdf['percapita'])
max_p = max(europa_gdf['percapita'])
#Definición de la barra gráfica
bar = plt.cm.ScalarMappable(cmap='gist_rainbow', 
 norm=plt.Normalize(vmin = min_p , vmax=max_p))
#Se declara una lista donde se guardarán los valores de la barra
bar._A = []
#Declaración de la ubicación y el tamaño de la barra.
cax = plt.axes([0.85, 0.15, 0.03, 0.7]) #[xcoord, ycoord, ancho, largo]
# Impresión de la barra con las variables superiores (bar y cax)
cbar = fig.colorbar(bar, cax=cax)
#Título de la barra
cbar.set_label('PIB Per Capita (USD)', fontsize = 12)
#Guardado del mapa en un archivo jpg indicando su resolución.
#plt.savefig('EuropaPIB.jpg', dpi = 200)
plt.show()
"""
#***********************************************************************************************************************


def show_graphic():
    # Control del tamaño de la figura del mapa
    fig, ax = plt.subplots(figsize=(5, 5))

    # Control del título y los ejes
    ax.set_title('Natalidad por Provincias en España, 2018', pad = 20, fontdict={'fontsize':10, 'color': '#4873ab'})
    ax.set_xlabel('Longitud')
    ax.set_ylabel('Latitud')
    map_data.plot(column='NAT2018', cmap='plasma', ax=ax, zorder=5)

    canvas = FigureCanvasTkAgg(fig, master=marco_1)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)

def otraVentana():
    df = pd.read_csv("../Iris.csv")
    raiz = Tk()
    raiz.title("Tabla de datos")
    raiz.geometry("800x600")

    marco_1 = Frame(raiz, width=400, height=300)
    marco_1.grid(row=0, column=0)
    marco_1.config(bd=10, relief="solid")
    
    table_1 = Table(marco_1, dataframe=df)
    table_1.place(x=0, y=0)
    table_1.show()
    
    raiz.mainloop()

#Cargamos la capa tematica
map_data = gpd.read_file("../natalidad.geojson")

root = Tk()
root.title("Software Oil Accidents")
root.geometry("1200x800")
#Button for graphic
boton_1 = Button(root, text="Show Graphic", command=show_graphic)
boton_1.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

marco_1 = Frame(root)
marco_1.place(relx=0.5, rely=0.05, relwidth=0.45, relheight=0.7)
marco_1.config(bd=10, relief="solid")

boton_2 = Button(root, text="Quit", command=root.destroy)
boton_2.place(relx=0.05, rely=0.5, relwidth=0.1, relheight=0.05)

boton_2 = Button(root, text="Abrir otra ventana", command=otraVentana)
boton_2.place(relx=0.05, rely=0.8, relwidth=0.1, relheight=0.05)

"""
# Control del tamaño de la figura del mapa
fig, ax = plt.subplots(figsize=(5, 5))

# Control del título y los ejes
ax.set_title('Natalidad por Provincias en España, 2018', pad = 20, fontdict={'fontsize':10, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
map_data.plot(column='NAT2018', cmap='plasma', ax=ax, zorder=5)

canvas = FigureCanvasTkAgg(fig, master=marco_1)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0)
"""

root.mainloop()

