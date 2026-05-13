import requests

def obtener_info_pais():
    print("--- 🌍 Buscador Global de Países 🌍 ---")
    print("Escribe 'salir' para finalizar.\n")

    while True:
        nombre_pais = input("Introduce el nombre de un país: ").strip()

        if nombre_pais.lower() == 'salir':
            print("¡Adiós! Gracias por usar el buscador.")
            break

        url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
        
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            
            datos = respuesta.json()[0] 
            
            # --- Extracción de datos ---
            nombre = datos.get('name', {}).get('common', 'N/A')
            # Extraemos el emoji de la bandera
            bandera = datos.get('flag', '') 
            capital = datos.get('capital', ['N/A'])[0]
            region = datos.get('region', 'N/A')
            subregion = datos.get('subregion', 'N/A')
            
            # Extraer Monedas
            monedas_dict = datos.get('currencies', {})
            monedas_lista = [f"{v.get('name')} ({v.get('symbol')})" for v in monedas_dict.values()]
            texto_monedas = ", ".join(monedas_lista) if monedas_lista else "N/A"

            # Extraer Idiomas
            idiomas = ", ".join(datos.get('languages', {}).values()) or "N/A"

            # --- Mostrar Resultados ---
            print("\n" + "⭐" + "="*45 + "⭐")
            print(f"  {bandera}  PAÍS: {nombre.upper()} ({bandera})")
            print("="*47)
            print(f"  📍  Ubicación: {region} ({subregion})")
            print(f"  🏙️   Capital:   {capital}")
            print(f"  🗣️   Idiomas:   {idiomas}")
            print(f"  💰  Moneda:    {texto_monedas}")
            print("="*47 + "\n")

        except requests.exceptions.HTTPError:
            print(f"❌ No se encontró el país '{nombre_pais}'. Intenta con el nombre en inglés.\n")
        except Exception as e:
            print(f"⚠️ Error inesperado: {e}\n")

if __name__ == "__main__":
    obtener_info_pais()