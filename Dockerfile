# 🐍 Base Image
FROM python:3.9

# 🏗 Install Dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 📂 Copy Python Script & Requirements
COPY colab_automation.py /app/colab_automation.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app

# 🛠 Install Chrome & WebDriver
RUN apt-get update && apt-get install -y wget unzip curl && \
    wget -qO- https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > /tmp/chrome.deb && \
    apt-get install -y /tmp/chrome.deb && \
    rm /tmp/chrome.deb && \
    curl -sS -o /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip && \
    chmod +x /usr/local/bin/chromedriver

# 🌍 Set Chrome Path for Selenium
ENV PATH="/usr/local/bin:$PATH"

# 🚀 Run the Script
CMD ["python", "colab_automation.py"]
