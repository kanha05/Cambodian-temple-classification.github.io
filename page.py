import asyncio
from pyppeteer import launch

async def save_streamlit_app():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://localhost:8501')  # Streamlit app URL
    await page.screenshot({'path': 'streamlit_app.png'})  # Save as PNG
    content = await page.content()  # Get HTML content
    with open('streamlit_app.html', 'w') as f:
        f.write(content)  # Save to an HTML file
    await browser.close()

asyncio.get_event_loop().run_until_complete(save_streamlit_app())
