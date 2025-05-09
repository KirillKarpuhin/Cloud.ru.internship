import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

@pytest.fixture
# фикстура 
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test_example(browser):
    
    browser.get("https://example.com")
    # проверка заголовка страницы
    title_element = browser.find_element(By.TAG_NAME, "title")
    title_text = title_element.get_attribute("textContent")
    assert "Example" in title_text, f"Заголовок '{title_text}' не содержит 'Example'"

    # В требованиях указано: Находит элемент по CSS-селектору, содержащему текст "More information" и кликает по нему. По Css селектору не найти поиск по тексту, поэтому пишу произовльно
    information = browser.find_element(By.CSS_SELECTOR, "button_more_info")
    #information = browser.find_element(By.XPATH, "//button[text()='More information']")
    information.click()

    # ждем загрузку новой страницы
    new_url = EC.url_to_be("https://www.iana.org/help/example-domains")
    WebDriverWait(browser, 10).until(new_url)

    # проверяем соответствие новому URL
    current_url = browser.current_url
    assert current_url == "https://www.iana.org/help/example-domains", f"Ожидаемый URL другой: {current_url}"