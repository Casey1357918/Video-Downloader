
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from downloader import download
import os


DEFAULT_LOCATION_FILE = 'default_location.txt'


def add_url():
    url = url_entry.get().strip()

    if url:
        url_listbox.insert(tk.END, url)
        url_entry.delete(0, tk.END)


def start_download():
    urls = url_listbox.get(0, tk.END)
    download_path = path_entry.get().strip()

    if not urls:
        messagebox.showwarning("No URLs", "Please add at least one video URL.")
        return

    try:
        with open(DEFAULT_LOCATION_FILE, 'w') as file:
            file.write(download_path)
    except Exception as e:
        messagebox.showerror("File Error", f"Could not save download location:\n{e}")
        return

    successful = 0
    failed = 0

    for url in urls:
        try:
            download(url, download_path)
            successful += 1

        except Exception as e:
            failed += 1
            messagebox.showerror(
                "Download Error",
                f"Failed to download:\n{url}\n\nError:\n{e}"
            )

    url_listbox.delete(0, tk.END)

    messagebox.showinfo(
        "Download Results",
        f"Successful: {successful}\nFailed: {failed}"
    )


root = tk.Tk()
root.title("Video Downloader")


tk.Label(root, text="Video URL's: (Add one at a time)").pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Button(root, text="Add URL", command=add_url).pack(pady=5)

url_listbox = tk.Listbox(root, width=50, height=10)
url_listbox.pack(pady=10)


tk.Label(
    root,
    text="Save Path: (If empty, defaults to your Downloads folder)"
).pack()

path_entry = tk.Entry(root, width=50)
path_entry.pack()


try:
    with open(DEFAULT_LOCATION_FILE, 'r') as file:
        content = file.read().strip()
except FileNotFoundError:
    content = ""

path_entry.insert(0, content)


tk.Button(root, text="Download", command=start_download).pack(pady=5)


try:
    icon = Image.open("icon.png")
    photo = ImageTk.PhotoImage(icon)
    root.wm_iconphoto(False, photo)
except FileNotFoundError:
    print("Icon file not found. Using default icon.")


root.mainloop()
