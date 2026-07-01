import pandas as pd

# Función generada por Gemini 
def convertir_letra_a_switch(letra):
    """
    Convierte una letra limpia ('A', 'B'...) a su formato 'S1', 'S2'...
    Si el valor ya es un string modificado o un número, lo deja igual.
    """
    if pd.isna(letra):
        return letra
    
    letra_str = str(letra).strip().upper()
    
    # Comprobamos que sea una única letra de la A a la Z
    if len(letra_str) == 1 and 'A' <= letra_str <= 'Z':
        int_nodo = ord(letra_str) - ord('A') + 1
        return f"S{int_nodo}"
    
    return letra  

# Script para modificar el CSV de Abilene_v2.csv a Abilene_v3.csv. Generado por Gemini.

archivo_entrada = 'Abilene_v2.csv'  # Archivo original 
archivo_salida = 'Abilene_v3.csv'   

df = pd.read_csv(archivo_entrada)

print("Columnas detectadas en el dataset:", df.columns.tolist())

# Identificar la columna del nodo TA
columna_ta = 'Nodo_TA' 

if columna_ta in df.columns:
    # Aplicar la conversión a toda la columna 
    df[columna_ta] = df[columna_ta].apply(convertir_letra_a_switch)
    
    df.to_csv(archivo_salida, index=False)      # Guardar el archivo
    print(f"¡Éxito absoluto! El archivo '{archivo_salida}' ha sido actualizado al formato S1, S2, etc.")
else:
    print(f"❌ Error: No se encontró la columna '{columna_ta}'. Mira el print de arriba y ajusta el nombre.")