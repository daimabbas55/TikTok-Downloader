
from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Go to the homepage
        page.goto("http://127.0.0.1:5000")
        page.screenshot(path="verification/homepage.png")
        print("Homepage screenshot taken.")

        # 2. Fill in the form and submit
        page.fill('input[name="url"]', "https://www.tiktok.com/@xingxing.themonkey/video/7593563486723116310")
        page.click('button[type="submit"]')

        # 3. Wait for result and screenshot
        page.wait_for_selector('h1', timeout=10000)
        page.screenshot(path="verification/result_page.png")
        print("Result page screenshot taken.")

        browser.close()

if __name__ == "__main__":
    verify_frontend()
