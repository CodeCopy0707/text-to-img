import time
import requests
from google.colab import auth
from googleapiclient.discovery import build

# 🔐 Authenticate Google Account
print("🔐 Authenticating Google Account...")
auth.authenticate_user()

# 📂 Access Google Drive
print("📂 Accessing Google Drive & Colab Notebooks...")
drive_service = build('drive', 'v3')

# 📌 Define Notebook Details
notebook_url = "https://colab.research.google.com/github/lllyasviel/Fooocus/blob/main/fooocus_colab.ipynb"
execution_endpoint = "https://colab.research.google.com/execute"

# ▶️ Run the Colab Notebook
print(f"▶️ Running Notebook: {notebook_url}")
session = requests.Session()
response = session.post(execution_endpoint, json={"notebook": notebook_url})

if response.status_code == 200:
    print("✅ Notebook Execution Started Successfully!")
else:
    print("❌ Failed to Start Notebook Execution!")
    print(response.text)
    exit()

# ⏳ Wait for Notebook Execution
time.sleep(30)

# 🔍 Extract Generated URLs (Local & Public)
print("🔍 Fetching Generated Links...")

colab_output = session.get(notebook_url).text  # Fetch the executed notebook's output
localhost_url = "Not Found"
public_url = "Not Found"

if "http://127.0.0.1" in colab_output:
    localhost_url = colab_output.split("http://127.0.0.1")[1].split()[0]
    localhost_url = "http://127.0.0.1" + localhost_url

if "gradio.live" in colab_output:
    public_url = colab_output.split("gradio.live")[0].split()[-1]

# ✅ Print Results
print(f"\n✅ **Localhost URL:** {localhost_url}")
print(f"✅ **Public URL:** {public_url}")
