import os
import shutil
import time


def get_username():
    print("Please enter your username.")
    print("To find your username, open File Explorer, and navigate to 'C:\\Users'.")
    print("Your username is the name of the folder you see inside 'C:\\Users'.")
    print("For example, if you see 'C:\\Users\\JohnDoe', your username is 'JohnDoe'.")
    username = input("Enter your username: ")
    return username


def copy_files(source_folder, destination_folder):
    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print(f"\nWindows Spotlight folder not found!")
        print("Please verify your username inside 'C:\\Users'.\n")
        time.sleep(2)
        return False

    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over all the files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename + ".jpg")

        # Check if it's a file (not a directory) and if it already exists in the destination
        if os.path.isfile(source_path):
            if not os.path.exists(destination_path):  # Only copy if the file doesn't exist
                shutil.copy(source_path, destination_path)
                print(f"Copied: {destination_path}")
            else:
                print(f"Skipped: {destination_path} (already exists)")
        else:
            print(f"Skipped: {filename} (not a file)")

    return True


if __name__ == "__main__":
    username = get_username()
    source_folder = f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
    destination_folder = f"C:\\Users\\{username}\\Downloads\\Windows Spotlight Images"

    if not copy_files(source_folder, destination_folder):
        print("Failed to copy files. Please check your username and try again.")
