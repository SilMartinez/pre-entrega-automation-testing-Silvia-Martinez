Proyecto de Automatización QA – SauceDemo y API Reqres

El propósito de este proyecto es automatizar pruebas funcionales sobre el sitio SauceDemo utilizando Selenium WebDriver y Pytest, junto con pruebas de API REST empleando Requests, JSON, CSV y Faker.

El objetivo principal es validar el correcto funcionamiento de funcionalidades clave del sitio, así como demostrar un enfoque integral de automatización cubriendo UI + API.

Pruebas UI – SauceDemo

Inicio de sesión (Login)
Validación del acceso con credenciales válidas e inválidas (data-driven con CSV), verificando mensajes de error y redirección al inventario.

Catálogo de productos
Validación del título de la página, presencia de productos y datos del primer ítem (nombre y precio).

Carrito de compras
Agregado de productos, verificación del contador del carrito y validación de los ítems dentro del mismo.

Además se aplican buenas prácticas de automatización:

Esperas explícitas (WebDriverWait)
Independencia entre casos de prueba
Ejecución compatible con CI/CD (modo headless)
Screenshots automáticos en fallos
Logging centralizado
Pruebas API – Reqres.in

Incluyen validaciones de los siguientes métodos HTTP:
GET → obtención de lista de usuarios
POST → creación de usuarios:
Con Faker (datos generados dinámicamente)
Con JSON externo (payload parametrizable)
PUT → actualización completa
PATCH → actualización parcial
DELETE → eliminación de usuario

Las pruebas de API están correctamente implementadas, pero en mi entorno las llamadas externas a reqres.in están bloqueadas (HTTP 403). Por eso incorporé un mecanismo que detecta esa condición y marca los tests como SKIPPED, evitando que una limitación de red genere falsos fallos en la suite. Este enfoque se utiliza en entornos CI/CD reales donde las APIs externas no siempre están disponibles.

Tecnologías Utilizadas

Python	Lenguaje principal del proyecto
Pytest	Framework para ejecutar y estructurar pruebas
Selenium WebDriver	Automatización UI
Requests	Consumo de APIs REST
Faker	Generación de datos dinámicos
CSV / JSON	Datos externos para pruebas data-driven
Git y GitHub	Control de versiones
Pytest-HTML	Reporte en formato HTML

Instalación de dependencias
1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>

2. (Opcional) Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows

3. Instalar dependencias
pip install -r requirements.txt

Ejecución de las pruebas
Ejecutar todas las pruebas (UI + API) con reporte HTML
pytest -v --html=reports/reporte.html

El reporte se genera automáticamente en la carpeta reports/, incluyendo:

Tests ejecutados
Resultados
Logs
Capturas de pantalla en caso de error

Variables de entorno opcionales

Las pruebas de UI permiten configurar credenciales externas:

Variable	Función
SAUCE_USER	Usuario para iniciar sesión
SAUCE_PWD	Contraseña

Ejemplo:

SAUCE_USER=standard_user SAUCE_PWD=secret_sauce pytest -v --html=reports/reporte.html

Estructura del proyecto
.
├─ utils/
│  ├─ helpers.py               # Configuración del driver, login y screenshots
│  └─ data_loader.py           # Lectura de CSV y JSON
│
├─ tests/
│  ├─ test_saucedemo.py        # Pruebas UI (login, catálogo, carrito)
│  └─ test_api_reqres.py       # Pruebas API (GET, POST, PUT, PATCH, DELETE)
│
├─ data/
│  ├─ logins.csv               # Dataset para pruebas de login
│  └─ api_payloads.json        # Payloads para creación de usuarios en API
│
├─ reports/                    # Reportes HTML y screenshots automáticos
├─ logs/                       # Registro de ejecución
│
├─ conftest.py                 # Fixtures globales, logging y captura de fallos
├─ pytest.ini                  # Configuración general de Pytest y markers
├─ requirements.txt            # Dependencias del proyecto
└─ README.md                   # Documentación del proyecto