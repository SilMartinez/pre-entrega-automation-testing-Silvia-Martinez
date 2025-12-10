import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import login, get_credentials
from utils.data_loader import load_csv_login_data


@pytest.mark.ui
@pytest.mark.parametrize(
    "username,password,should_pass", load_csv_login_data("logins.csv")
)
def test_login_data_driven(driver, username, password, should_pass, logger):

    logger.info(
        f"Ejecutando login con usuario={username}, should_pass={should_pass}"
    )
    login(driver, username, password)

    if should_pass:
        title = driver.find_element(By.CLASS_NAME, "title").text
        assert "Products" in title
    else:
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert error.is_displayed()
        assert "Epic sadface" in error.text


@pytest.mark.ui
def test_catalogo_muestra_titulo_y_primer_item(driver, logger):

    username, password = get_credentials()
    login(driver, username, password)

    logger.info("Verificando catálogo de productos")

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" in title

    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0, "No se encontraron productos en el catálogo"

    first_item = items[0]
    name = first_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = first_item.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert name.strip() != ""
    assert price.startswith("$")


@pytest.mark.ui
def test_carrito_agrega_y_muestra_productos(driver, logger):

    username, password = get_credentials()
    login(driver, username, password)

    logger.info("Agregando productos al carrito")

    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) >= 2, "Se necesitan al menos 2 productos para este test"

    for item in items[:2]:
        add_button = item.find_element(By.TAG_NAME, "button")
        add_button.click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "2"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 2