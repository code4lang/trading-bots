import os
from PIL import Image
from instabot import Bot
import glob

cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

def upload_image(username, password, image_path, caption):
    bot = Bot()
    bot.login(username=username, password=password)

    # Load and resize the image
    img = Image.open(image_path)
    img = img.resize((1080, 1080))
    temp_image_path = "temp_image.jpg"
    img.save(temp_image_path)

    # Upload the image with the specified caption
    bot.upload_photo(temp_image_path, caption=caption)

    # Clean up temporary files
    os.remove(temp_image_path)

    bot.logout()

# Input your Instagram credentials
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

# Input the path to the image you want to upload
image_path = input("Enter the path to your image file: ")

# Input the caption for your post
caption = input("Enter your caption: ")

upload_image(username, password, image_path, caption)