import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Entry, Button, Listbox, END, SINGLE, simpledialog, messagebox
from utils import save_image


# Function to download the latest media image from Twitter
def download_latest_media_image(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)

    try:
        media_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[src*='twimg.com/media']"))
        )
    except:
        print("No media images found or page did not load properly.")
        driver.quit()
        return None

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    media_images = soup.find_all('img', {'src': lambda x: x and 'twimg.com/media' in x})

    driver.quit()

    if media_images:
        return media_images[0]['src']
    else:
        print("No media images found.")
        return None


# Function to monitor a single Twitter user
def monitor_twitter_user(user_input, twitter_users, listbox):
    if user_input.startswith("http://") or user_input.startswith("https://"):
        url = user_input
        twitter_handle = user_input.split("/")[-1]
    else:
        twitter_handle = user_input
        url = f"https://twitter.com/{twitter_handle}"

    save_directory = os.path.expanduser(f"~/Downloads/{twitter_handle}")
    os.makedirs(save_directory, exist_ok=True)

    latest_image_url = download_latest_media_image(url)
    if latest_image_url:
        save_image(latest_image_url, save_directory)
    else:
        print(f"No media images found for {twitter_handle}. Initial download failed.")
        return

    if twitter_handle not in twitter_users:
        twitter_users[twitter_handle] = {"label": "", "favorite": False}
        listbox.insert(END, f"{twitter_handle} ()")

    last_downloaded_image_url = latest_image_url

    while True:
        latest_image_url = download_latest_media_image(url)
        if latest_image_url and latest_image_url != last_downloaded_image_url:
            save_image(latest_image_url, save_directory)
            last_downloaded_image_url = latest_image_url

            if twitter_users[twitter_handle]["favorite"]:
                messagebox.showinfo("New Image Downloaded", f"Downloaded a new {twitter_handle} image.")

        else:
            print(f"No new media images found for {twitter_handle}.")
        time.sleep(3600)


# Function to handle the "Add Label" button click
def add_label(twitter_users, listbox):
    selected_index = listbox.curselection()
    if selected_index:
        selected_entry = listbox.get(selected_index)
        twitter_handle = selected_entry.split(' (')[0]
        new_label = simpledialog.askstring("Input", f"Enter label for {twitter_handle}:")
        if new_label is not None:
            twitter_users[twitter_handle]["label"] = new_label
            update_listbox(listbox, twitter_users)
            print(f"Updated label for {twitter_handle}: {new_label}")
    else:
        messagebox.showinfo("Info", "Please select a Twitter user from the list to add a label.")


# Function to handle the "Favorite User" button click
def favorite_user(twitter_users, listbox):
    selected_index = listbox.curselection()
    if selected_index:
        selected_entry = listbox.get(selected_index)
        twitter_handle = selected_entry.split(' (')[0]
        twitter_users[twitter_handle]["favorite"] = not twitter_users[twitter_handle]["favorite"]
        update_listbox(listbox, twitter_users)
        print(f"Updated favorite status for {twitter_handle}")
    else:
        messagebox.showinfo("Info", "Please select a Twitter user from the list to favorite.")


# Function to update the listbox display
def update_listbox(listbox, twitter_users):
    listbox.delete(0, END)
    for user, info in twitter_users.items():
        star = " ⭐" if info["favorite"] else ""
        label = info["label"]
        listbox.insert(END, f"{user} ({label}){star}")