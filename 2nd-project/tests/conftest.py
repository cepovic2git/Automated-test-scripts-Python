import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element())
    request.cls.driver = driver
    yield
    driver.quit()