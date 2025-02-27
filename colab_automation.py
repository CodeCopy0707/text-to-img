from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# 🚀 Launch Browser
print("🚀 Launching browser...")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 🌐 Open Google Colab Notebook
print("🌐 Opening Google Colab Fooocus notebook...")
driver.get("https://colab.research.google.com/github/lllyasviel/Fooocus/blob/main/fooocus_colab.ipynb#scrollTo=_vkOYRuWLgQi")
time.sleep(5)  # Wait for page to load

# ▶️ Run All (Ctrl + F9)
print("▶️ Clicking 'Run All'...")
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + "F9")
time.sleep(5)

# ⚠️ Click 'Run Anyway' if warning appears
try:
    run_anyway_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Run anyway')]")
    if run_anyway_button:
        print("✅ Clicking 'Run Anyway'...")
        run_anyway_button.click()
except:
    print("❌ 'Run Anyway' button not found, proceeding...")

print("✅ Execution started!")

# Wait for URLs to appear in output
time.sleep(20)

print("🔍 Searching for Local & Public URLs...")

# Extract logs from Colab output
output_text = driver.page_source
localhost_match = re.search(r'http://127\.0\.0\.1:\d+', output_text)
public_match = re.search(r'https?:\/\/[^\s]+gradio\.live[^\s]*', output_text)

localhost_url = localhost_match.group(0) if localhost_match else "Not found"
public_url = public_match.group(0) if public_match else "Not found"

print(f"\n✅ **Localhost URL:** {localhost_url}")
print(f"✅ **Public URL:** {public_url}\n")

# 🔄 Keep Running
while True:
    time.sleep(10)
