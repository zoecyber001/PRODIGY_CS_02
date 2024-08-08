import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def encrypt_image(image_path, output_path):
    """
    Encrypts an image by inverting its RGB values.

    image_path: Path to the input image.
    output_path: Path to save the encrypted image.
    """
    try:
        img = Image.open(image_path)  # Open the image file
        pixels = img.load()  # Load pixel data

        # Iterate over each pixel
        for i in range(img.size[0]):  # Width
            for j in range(img.size[1]):  # Height
                r, g, b = pixels[i, j]  # Get the RGB values
                # Encrypt by inverting the RGB values
                pixels[i, j] = (255 - r, 255 - g, 255 - b)
        
        img.save(output_path)  # Save the encrypted image
        messagebox.showinfo("Success", f"Image encrypted and saved as {output_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def decrypt_image(image_path, output_path):
    """
    Decrypts an image by re-inverting its RGB values.

    """
    try:
        # Decrypting is the same as encrypting since it's just inversion
        encrypt_image(image_path, output_path)
        messagebox.showinfo("Success", f"Image decrypted and saved as {output_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def choose_image():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
    )
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)

def save_image():
    file_path = filedialog.asksaveasfilename(
        title="Save processed image",
        defaultextension=".jpg",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
    )
    if file_path:
        entry_output_path.delete(0, tk.END)
        entry_output_path.insert(0, file_path)

def process_image():
    image_path = entry_image_path.get()
    output_path = entry_output_path.get()
    action = var_action.get()

    if not image_path or not output_path:
        messagebox.showerror("Error", "Please provide both input and output paths.")
        return

    if action == "encrypt":
        encrypt_image(image_path, output_path)
    elif action == "decrypt":
        decrypt_image(image_path, output_path)
    else:
        messagebox.showerror("Error", "Please select an action (Encrypt or Decrypt).")

# GUI setup
root = tk.Tk()
root.title("Image Encryptor/Decryptor")

# Image path input
tk.Label(root, text="Image Path:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_image_path = tk.Entry(root, width=50)
entry_image_path.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=choose_image).grid(row=0, column=2, padx=10, pady=10)

# Output path input
tk.Label(root, text="Output Path:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_output_path = tk.Entry(root, width=50)
entry_output_path.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=save_image).grid(row=1, column=2, padx=10, pady=10)

# Action selection (Encrypt/Decrypt)
var_action = tk.StringVar(value="encrypt")
tk.Label(root, text="Action:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
tk.Radiobutton(root, text="Encrypt", variable=var_action, value="encrypt").grid(row=2, column=1, padx=10, pady=10, sticky="w")
tk.Radiobutton(root, text="Decrypt", variable=var_action, value="decrypt").grid(row=2, column=1, padx=10, pady=10)

# Process button
tk.Button(root, text="Process", command=process_image).grid(row=3, column=1, padx=10, pady=20)

# Start the GUI loop
root.mainloop()
