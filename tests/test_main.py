from playwright.sync_api import sync_playwright


screenshots_folder = 'output'


def test_zero_water_no_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        page.locator('xpath=//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[4]').screenshot(path=f'./{screenshots_folder}/1.png')
        browser.close()
    
    assert True


def test_zero_exhaust_no_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        page.locator('xpath=//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[2]').screenshot(path=f'./{screenshots_folder}/2.png')
        browser.close()
    
    assert True

def test_zero_energy_no_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        page.locator('xpath=//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[6]').screenshot(path=f'./{screenshots_folder}/3.png')
        browser.close()
    
    assert True


def test_water_with_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state='state.json')
        page = context.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        page.locator('xpath=//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[4]').screenshot(path=f'./{screenshots_folder}/4.png')
        context.storage_state(path="state.json")
        context.close()
        browser.close()

    assert True


def test_exhaust_with_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state='state.json')
        page = context.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        page.locator('xpath=//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[2]').screenshot(path=f'./{screenshots_folder}/5.png')
        context.storage_state(path="state.json")
        context.close()
        browser.close()

    assert True


def test_energy_with_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state='state.json')
        page = context.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        page.locator('xpath=//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[6]').screenshot(path=f'./{screenshots_folder}/6.png')
        context.storage_state(path="state.json")
        context.close()
        browser.close()

    assert True




