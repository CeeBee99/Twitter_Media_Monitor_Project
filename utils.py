import os
import time
import requests

# Function to save the image
def save_image(image_url, save_directory):
    response = requests.get(image_url)
    if response.status_code == 200:
        timestamp = time.strftime("%Y%m%d%H%M%S")
        image_path = os.path.join(save_directory, f'latest_media_image_{timestamp}.jpg')
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully to {image_path}.")
    else:
        print("Failed to download the image.")
