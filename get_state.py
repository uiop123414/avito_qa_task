from playwright.sync_api import sync_playwright
from time import sleep

def set_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state='state.json')

        page = context.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')

        sleep(60)

        context.storage_state(path="state.json")
        context.close()
        browser.close()

    assert True