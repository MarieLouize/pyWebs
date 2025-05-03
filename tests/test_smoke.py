from playwright.sync_api import sync_playwright

def test_open_google():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        assert "Example" in page.title()
        browser.close()