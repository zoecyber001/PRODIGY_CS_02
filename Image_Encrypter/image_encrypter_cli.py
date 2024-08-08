from PIL import Image

def encrypt_image(image_path, output_path):
    """
    Encrypts an image by inverting its RGB values.

    :param image_path: Path to the input image.
    :param output_path: Path to save the encrypted image.
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
        print(f"Image encrypted and saved as {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(image_path, output_path):
    """
    Decrypts an image by re-inverting its RGB values.

    image_path: Path to the encrypted image.
    output_path: Path to save the decrypted image.
    """
    try:
        # Decrypting is the same as encrypting since it's just inversion
        encrypt_image(image_path, output_path)
        print(f"Image decrypted and saved as {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the Image Encryptor/Decryptor")

    # Get the image path from the user
    image_path = input("Enter the path to the image: ")

    # Get the user's choice for encryption or decryption
    action = input("Do you want to (e)ncrypt or (d)ecrypt the image? ").lower()

    # Get the output path from the user
    output_path = input("Enter the name with path to save the processed image: ")

    if action == 'e':
        encrypt_image(image_path, output_path)
    elif action == 'd':
        decrypt_image(image_path, output_path)
    else:
        print("Invalid action. Please choose 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
