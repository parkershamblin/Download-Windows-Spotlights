# Download Windows Spotlight Images

This script helps you download Windows Spotlight images from your Windows 10 or Windows 11 PC.

## Prerequisites
- Python 3.x installed on your computer.

## Instructions

1. **Clone or Download the Repository**:
    - Clone the repo using `git clone https://github.com/parkershamblin/windows-spotlight-image-downloader` or download the zip file and extract it.

2. **Find Your Username**:
    - Open File Explorer.
    - Navigate to `C:\Users`.
    - Note the name of the folder corresponding to your username (e.g., `JohnDoe`).

3. **Open Command Prompt and Navigate to Directory**:
    - Open a terminal or command prompt.
    - Use the `cd` command to navigate to the directory where you downloaded or cloned the repository. For example:
    
    ```sh
    cd path\to\spotlight-downloader
    ```

4. **Run the Script**:
    - Run the script with Python:

    ```sh
    python main.py
    ```

    - Follow the on-screen instructions to enter your username.

5. **Access Your Images**:
    - The script will copy the Windows Spotlight images to a folder named `Windows Spotlight Images` in your `Downloads` directory.

## Script Details

The script performs the following steps:
1. Prompts you to enter your Windows username.
2. Copies files from the Spotlight assets folder to a designated folder in your Pictures directory.

Here is the script for reference:

```python
import os
import shutil
import time

def get_username():
    username = input("Enter your username: ")
    return username

def copy_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        if os.path.isfile(source_file):
            shutil.copy(source_file, destination_folder)

    print("Files copied successfully.")

if __name__ == "__main__":
    username = get_username()
    source_folder = f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
    destination_folder = f"C:\\Users\\{username}\\Pictures\\Spotlight Images"

    copy_files(source_folder, destination_folder)
