from playwright.sync_api import sync_playwright

def guardar_sesion():
    with sync_playwright() as p:
        # Abrimos el navegador visible
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navegar a la página de login
        page.goto("file:///D:/Desktop/prueba%20scraper/pagina%20scrap%20test.html#login")

        # Completar credenciales y hacer clic en entrar
        page.fill("input[id='username']", "user")
        page.fill("input[id='password']", "admin")
        page.click("button[type='submit']")

        # Esperar a que redirija al panel principal tras el login
        page.wait_for_url("file:///D:/Desktop/prueba%20scraper/pagina%20scrap%20test.html#dashboard")

        # Guardar las cookies y el almacenamiento local en un archivo JSON
        context.storage_state(path="sesion.json")
        print("¡Sesión guardada con éxito en sesion.json!")
        browser.close()

if __name__ == "__main__":
    guardar_sesion()