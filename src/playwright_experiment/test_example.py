import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://ariel.jp/ja-jp")
        await page.wait_for_load_state("networkidle")
        await page.screenshot(path=f"{os.path.dirname(__file__)}/images/screenshot.png", full_page=True)
        print(await page.title())
        await page.emulate_media(media="screen")
        await page.pdf(path=f"{os.path.dirname(__file__)}/images/page.pdf")
        # print(await page.content())
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())