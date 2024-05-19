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
    cd "C:\Users\JohnDoe\Documents\GitHub\download_windows_spotlights"
    ```

4. **Run the Script**:
    - Run the script with Python:

    ```sh
    python main.py
    ```

    - Follow the on-screen instructions to enter your username.

5. **Access Your Images**:
    - The script will copy the Windows Spotlight images to a folder named `Windows Spotlight Images` in your `Downloads` directory.
