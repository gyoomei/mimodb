#!/usr/bin/env python3
"""Take 5 screenshots of MiMoDB at 1920x1080."""
import asyncio, nodriver as uc, os

URL = "https://gyoomei.github.io/mimodb/index.html"
OUT = os.path.expanduser("~/mimodb/screenshots")
os.makedirs(OUT, exist_ok=True)

async def main():
    browser = await uc.start(headless=True, browser_args=["--no-sandbox", "--disable-gpu"])
    page = await browser.get(URL)
    await page.sleep(4)
    await page.send(uc.cdp.emulation.set_device_metrics_override(
        width=1920, height=1080, device_scale_factor=1, mobile=False
    ))
    await page.sleep(1)

    # 1. Hero + sidebar + data (full view)
    await page.evaluate("window.scrollTo(0, 0)")
    await page.sleep(0.5)
    await page.save_screenshot(os.path.join(OUT, "01_hero_explorer.png"))
    print("✓ 1: Hero + Explorer")

    # 2. Scroll to query + results
    await page.evaluate("window.scrollTo(0, 300)")
    await page.sleep(0.5)
    await page.save_screenshot(os.path.join(OUT, "02_query_results.png"))
    print("✓ 2: Query + Results")

    # Click on "orders" collection
    await page.evaluate("selectCollection('orders')")
    await page.sleep(1)
    await page.evaluate("window.scrollTo(0, 300)")
    await page.sleep(0.5)
    await page.save_screenshot(os.path.join(OUT, "03_orders_collection.png"))
    print("✓ 3: Orders collection")

    # Open chat panel
    await page.evaluate("toggleChat()")
    await page.sleep(1)
    await page.save_screenshot(os.path.join(OUT, "04_chat_widget.png"))
    print("✓ 4: Chat widget")

    # Close chat, switch to light theme
    await page.evaluate("toggleChat()")
    await page.sleep(0.5)
    await page.evaluate("toggleTheme()")
    await page.sleep(1)
    await page.evaluate("window.scrollTo(0, 0)")
    await page.sleep(0.5)
    await page.save_screenshot(os.path.join(OUT, "05_light_theme.png"))
    print("✓ 5: Light theme")

    browser.stop()
    print(f"\n✅ Done! Screenshots in {OUT}/")

asyncio.run(main())
