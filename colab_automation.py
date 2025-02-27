import os

# Install required dependencies
os.system("pip install pygit2==1.15.1")

# Change directory to /content (Only for Colab)
os.chdir("/content")

# Clone the Fooocus repository
os.system("git clone https://github.com/lllyasviel/Fooocus.git")

# Change directory to Fooocus
os.chdir("/content/Fooocus")

# Run the entry script with required parameters
os.system("python entry_with_update.py --share --always-high-vram")
