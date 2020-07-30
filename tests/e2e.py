from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_score_service(url):
    driver = webdriver.Chrome()

    driver.get(url)
    score = driver.find_element_by_id("score").text

    return True if 1 <= int(score) <= 1000 else False


def main_function():
    result = test_score_service('http://127.0.0.1:5000/')

    return 0 if result is True else -1


if __name__ == "__main__":
    main_function()
