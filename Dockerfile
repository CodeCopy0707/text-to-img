# 🐍 Base Image
FROM python:3.9

# 📂 Set Working Directory
WORKDIR /app

# 📥 Copy Requirements File
COPY requirements.txt requirements.txt

# 🏗 Install Dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 📂 Copy Python Script
COPY colab_automation.py colab_automation.py

# 🚀 Run the Script
CMD ["python", "colab_automation.py"]
