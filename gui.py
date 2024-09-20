import threading
from tkinter import Tk, Label, Entry, Button, Listbox, END, SINGLE, simpledialog, messagebox
from twitter_monitor import monitor_twitter_user, add_label, favorite_user, update_listbox

# Function to handle the "Add User" button click
def add_user(twitter_users, listbox, user_entry):
    user_input = user_entry.get()
    if user_input:
        threading.Thread(target=monitor_twitter_user, args=(user_input, twitter_users, listbox)).start()
        user_entry.delete(0, END)

# Main script with GUI
def main():
    twitter_users = {}

    # Set up the GUI
    root = Tk()
    root.title("Twitter Media Monitor")

    Label(root, text="Enter Twitter User or URL:").pack()
    user_entry = Entry(root, width=50)
    user_entry.pack()

    add_button = Button(root, text="Add User", command=lambda: add_user(twitter_users, listbox, user_entry))
    add_button.pack()

    listbox = Listbox(root, width=50, height=10, selectmode=SINGLE)
    listbox.pack()

    label_button = Button(root, text="Add Label", command=lambda: add_label(twitter_users, listbox))
    label_button.pack()

    favorite_button = Button(root, text="Favorite User", command=lambda: favorite_user(twitter_users, listbox))
    favorite_button.pack()

    root.mainloop()
