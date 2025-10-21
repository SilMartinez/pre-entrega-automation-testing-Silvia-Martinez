Proyecto de Automatización QA – SauceDemo

El propósito de este proyecto es automatizar pruebas funcionales sobre el sitio SauceDemo utilizando Selenium WebDriver y Pytest.

El objetivo principal es validar el correcto funcionamiento de las funcionalidades clave del sitio, abarcando los siguientes puntos:

- Inicio de sesión (Login): acceso con credenciales válidas y verificación de redirección a la página de inventario.

- Catálogo de productos: validación del título, presencia de productos y datos del primer ítem (nombre y precio).

- Carrito de compras: agregado de productos, verificación del contador y validación de que los ítems agregados se visualicen correctamente.

El desarrollo de las pruebas se basa en buenas prácticas de automatización, priorizando el uso de esperas explícitas en lugar de pausas fijas, independencia entre casos de prueba y compatibilidad con entornos de integración continua (CI/CD) mediante ejecución en modo headless.

Tecnologías utilizadas

Python: lenguaje principal de desarrollo.
Pytest: framework para la estructura, ejecución y reporte de pruebas.
Selenium WebDriver: herramienta para la automatización de interacción con el navegador.
Git y GitHub: control de versiones y colaboración del código fuente.

Instrucciones de instalación de dependencias

Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>

(Opcional) Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate     # En Linux/Mac
venv\Scripts\activate        # En Windows


Instalar las dependencias del proyecto:

pip install -r requirements.txt


Ejecución de las pruebas

Para ejecutar las pruebas con Pytest y generar un reporte en formato HTML, utilizar el siguiente comando:
pytest -v --html=reports/reporte.html


El reporte se genera automáticamente en la carpeta reports/, mostrando el detalle de cada caso de prueba, su resultado y (en caso de error) las capturas de pantalla correspondientes.

Variables de entorno opcionales:
SAUCE_USER → define el usuario para iniciar sesión.
SAUCE_PWD → define la contraseña del usuario.

Ejemplo de ejecución completa:

SAUCE_USER=standard_user SAUCE_PWD=secret_sauce pytest -v --html=reports/reporte.html

📁 Estructura del proyecto
.
├─ utils/
│  └─ helpers.py               # Configuración del driver y login
├─ tests/
│  └─ test_saucedemo.py        # Casos de prueba automatizados
├─ reports/                    # Carpeta donde se guardan los reportes HTML y screenshots
├─ pytest.ini                  # Configuración general de Pytest
└─ README.md                   # Documentación del proyecto