from playwright.sync_api import sync_playwright

def buscar_ultima_revision():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # 1. Cargar la sesión previamente guardada
        context = browser.new_context(storage_state="sesion.json")
        page = context.new_page()

        # 2. Navegar a la página del catálogo o panel
        page.goto("file:///D:/Desktop/prueba%20scraper/pagina%20scrap%20test.html#dashboard")

        # 3. Escribir en el buscador la consulta deseada
        # Reemplaza 'input#search' por el selector real del buscador del sitio
        selector_buscador = "input[id='search-input']"
        page.fill(selector_buscador, "Cisco Catalyst 9300")
        page.press(selector_buscador, "Enter")

        # 4. Esperar a que carguen los resultados
        # Reemplaza '.resultado-item' por la clase CSS de cada producto o ítem en la lista
        page.wait_for_selector(".resultado-item")

        # 5. Obtener todos los elementos coincidentes
        items = page.query_selector_all(".resultado-item")
        
        resultados = []
        for item in items:
            # Extraer modelo/nombre y la versión o revisión
            nombre = item.query_selector(".nombre").inner_text() if item.query_selector(".nombre") else ""
            revision = item.query_selector(".revision").inner_text() if item.query_selector(".revision") else ""
            
            resultados.append({
                "nombre": nombre.strip(),
                "revision": revision.strip()
            })

        # 6. Filtrar o tomar el primer resultado (si el sitio ya los ordena por más reciente)
        if resultados:
            # Si requieres ordenamiento por lógica propia:
            # resultados.sort(key=lambda x: x['revision'], reverse=True)
            
            ultima_revision = resultados[0]
            print(f"Última revisión encontrada:")
            print(f"Producto: {ultima_revision['nombre']}")
            print(f"Revisión/Versión: {ultima_revision['revision']}")
        else:
            print("No se encontraron resultados para la búsqueda.")

        browser.close()

if __name__ == "__main__":
    buscar_ultima_revision()