import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import stepic
import os
import base64
from cryptography.fernet import Fernet

# Generate a key for encryption (Save this key for decryption)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to select an image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)

# Function to encrypt a message using a password
def encrypt_message():
    image_path = entry_image_path.get()
    message = entry_message.get()
    password = entry_password.get()

    if not image_path or not message or not password:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    try:
        # Encrypt message with the password
        key_derived = base64.urlsafe_b64encode(password.ljust(32).encode()[:32])  # Derive key from password
        cipher = Fernet(key_derived)
        encrypted_message = cipher.encrypt(message.encode())

        img = Image.open(image_path)
        encoded_img = stepic.encode(img, encrypted_message)

        output_path = os.path.splitext(image_path)[0] + "_encoded.png"
        encoded_img.save(output_path, "PNG")

        messagebox.showinfo("Success", f"Encrypted image saved as:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography - Encrypt")
root.geometry("400x300")

# Labels and Inputs
tk.Label(root, text="Select Image:").pack()
entry_image_path = tk.Entry(root, width=40)
entry_image_path.pack()
tk.Button(root, text="Browse", command=select_image).pack()

tk.Label(root, text="Enter Message:").pack()
entry_message = tk.Entry(root, width=40)
entry_message.pack()

tk.Label(root, text="Enter Password:").pack()
entry_password = tk.Entry(root, width=40, show="*")  # Hide password input
entry_password.pack()

tk.Button(root, text="Encrypt & Save", command=encrypt_message).pack()

root.mainloop()
