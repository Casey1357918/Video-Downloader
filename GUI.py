import tkinter as tk
from downloader import download
from PIL import Image, ImageTk
from tkinter import messagebox



def add_url():
    url = url_entry.get() 
    if url:  
        url_listbox.insert(tk.END, url)  
        url_entry.delete(0, tk.END)  


def start_download():
    urls = url_listbox.get(0, tk.END)
    download_path = path_entry.get()

    if content!=download_path:
        with open('default_location.txt', 'w') as file:
            file.write(download_path)
        

    for url in urls:
        try:
            download(url, download_path)
        except Exception as e:
            messagebox.showerror("Download Error", f"An error occurred:\n{e}")

    url_listbox.delete(0, tk.END)
    messagebox.showinfo("Download Complete", "All videos have been downloaded successfully.")




root = tk.Tk()
root.title("Video Downloader")


tk.Label(root, text="Video URL's: (Add one at a time)").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()


add_button = tk.Button(root, text="Add URL", command=add_url)
add_button.pack(pady=5)

url_listbox = tk.Listbox(root, width=50, height=10)
url_listbox.pack(pady=10)


tk.Label(root, text="Save Path: (If not filled out, will default to downloads folder)").pack()
path_entry = tk.Entry(root, width=50)
path_entry.pack()


with open('default_location.txt', 'r') as file:
    content = file.read()
path_entry.insert(0 , content)


tk.Button(root, text="Download", command=start_download).pack()

try:
    icon = Image.open("icon.png")
    photo = ImageTk.PhotoImage(icon)
    root.wm_iconphoto(False, photo)
except FileNotFoundError:
    print("Icon file not found. Using default icon.")


root.mainloop()
