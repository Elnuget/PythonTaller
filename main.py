import pandas as pd
import matplotlib.pyplot as plt

# 1. CONSEGUIR LOS DATOS
# Indica el nombre de tu archivo.
# Usamos la ruta relativa desde el script
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
nombre_archivo = os.path.join(script_dir, 'datos.csv')

# Lee el archivo CSV.
# 'pd.read_csv' es la función mágica para esto.
try:
    df = pd.read_csv(nombre_archivo)
except FileNotFoundError:
    print(f"¡Error! No se encontró el archivo: {nombre_archivo}")
    exit()

# 2. ORDENAR LOS DATOS
# Ponemos los datos de las columnas en variables simples.
# 'df['Nombre_Columna']' saca toda la lista de esa columna.
tiempo_o_muestra = df['Muestra']
temperaturas = df['Temperatura_C']
humedades = df['Humedad_Porcentaje']

# 3. HACER LOS DIBUJOS (GRÁFICAS)

# --- GRÁFICA DE TEMPERATURA ---
plt.figure(figsize=(10, 5)) # Crea un espacio grande para el dibujo
plt.plot(tiempo_o_muestra, temperaturas, label='Temperatura', color='red')
plt.title('Gráfica de Temperatura a lo largo del tiempo')
plt.xlabel('Número de Muestra')
plt.ylabel('Temperatura (°C)')
plt.grid(True) # Dibuja una cuadrícula para ver mejor
plt.legend()
plt.savefig('grafica_temperatura.png') # ¡Guarda la imagen!
plt.show() # Muestra la gráfica en pantalla

# --- GRÁFICA DE HUMEDAD ---
plt.figure(figsize=(10, 5)) # Crea un espacio para el segundo dibujo
plt.plot(tiempo_o_muestra, humedades, label='Humedad', color='blue')
plt.title('Gráfica de Humedad a lo largo del tiempo')
plt.xlabel('Número de Muestra')
plt.ylabel('Humedad (%)')
plt.grid(True)
plt.legend()
plt.savefig('grafica_humedad.png') # ¡Guarda la segunda imagen!
plt.show()

print("¡Gráficas generadas exitosamente y guardadas como imágenes PNG!")