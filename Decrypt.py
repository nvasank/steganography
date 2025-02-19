import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import stepic
import base64
from cryptography.fernet import Fernet

# Function to select an image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)

# Function to decrypt the message with a password
def decrypt_message():
    image_path = entry_image_path.get()
    password = entry_password.get()

    if not image_path or not password:
        messagebox.showerror("Error", "Please select an image and enter the password!")
        return

    try:
        img = Image.open(image_path)
        encrypted_message = stepic.decode(img)

        key_derived = base64.urlsafe_b64encode(password.ljust(32).encode()[:32])  # Derive key from password
        cipher = Fernet(key_derived)

        try:
            decrypted_message = cipher.decrypt(encrypted_message).decode()
            messagebox.showinfo("Hidden Message", f"Extracted Message:\n{decrypted_message}")
        except:
            messagebox.showerror("Error", "Incorrect password!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Decrypt")
root.geometry("400x250")

# Labels and Inputs
tk.Label(root, text="Select Image:").pack()
entry_image_path = tk.Entry(root, width=40)
entry_image_path.pack()
tk.Button(root, text="Browse", command=select_image).pack()

tk.Label(root, text="Enter Password:").pack()
entry_password = tk.Entry(root, width=40, show="*")  # Hide password input
entry_password.pack()

tk.Button(root, text="Decrypt Message", command=decrypt_message).pack()

root.mainloop()
