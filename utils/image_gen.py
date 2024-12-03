import requests
from tqdm import tqdm
import os 

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def download_image(prompt,part):
    """Downloads an image from the Pollinations AI API based on the given prompt.

    Args:
        prompt (str): The prompt to generate the image.

    Returns:
        None
    """

    url = f"https://image.pollinations.ai/prompt/{prompt}"

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  
        create_folder_if_not_exists('./outputs/images')
        with open(f"./outputs/images/part{part}.jpg", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

def image_main():
    part = 0 
    file = open("./outputs/line_by_line.txt")
    data = file.read().split("\n")
    for text in tqdm(data):
        if text == "":
            break 
        download_image(text,part)
        part += 1

if __name__ == '__main__':
    image_main()