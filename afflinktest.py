import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from pytrends.request import TrendReq

options = Options()
options.add_argument("--headless")# Set up the Chrome WebDriver
driver = webdriver.Edge(service=Service(executable_path='/workspaces/trading-bots/msedgedriver.exe'),options=options)  # Replace with the actual path to your chromedriver

# Define your Amazon Associate tag
associate_tag = 'your_associate_tag_here'

# Fetch trending search terms from Google Trends (adjust country as needed)
pytrends = TrendReq(hl='en-US', tz=360)
trending_searches = pytrends.trending_searches(pn='united_states')[:5]
print("trending: ",trending_searches)

# Visit each product page, extract details, and create banners
for search_term in trending_searches:
    # Search Amazon for the trending product
    amazon_search_url = f'https://www.amazon.com/s?k={search_term.replace(" ", "+")}'
    driver.get(amazon_search_url)
    time.sleep(2)  # Wait for the page to load (adjust as needed)

    # Extract product details (customize this part based on Amazon's HTML structure)
    try:
        product_title = driver.find_element_by_css_selector('.a-size-medium').text
        product_image_url = driver.find_element_by_css_selector('.s-image').get_attribute('src')
        product_price = driver.find_element_by_css_selector('.a-price .a-offscreen').text
    except Exception as e:
        print(f"Error extracting details for '{search_term}': {e}")
        continue

    # Generate affiliate link
    affiliate_link = f'https://www.amazon.com/dp/{driver.current_url.split("/")[-1]}?tag={associate_tag}'

    # Create banner HTML code (customize as per your design)
    banner_html = f"""
    <a href="{affiliate_link}" target="_blank">
        <img src="{product_image_url}" alt="{product_title}" width="300" height="200">
        <p>{product_title}</p>
        <p>Price: {product_price}</p>
    </a>
    """

    # Now you can inject the banner HTML into your Chrome extension or web page

# Close the WebDriver
driver.quit()
