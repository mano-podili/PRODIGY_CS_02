import os
from PIL import Image

def encrypt_image(input_path, output_path):
    """Encrypt an image by swapping red and blue channels."""
    
    # Open the input image
    img = Image.open(input_path)

    # Load the image pixels
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Encrypt the image by swapping red and blue channels
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (b, g, r)

    # Save the encrypted image
    img.save(output_path)
    print(f"Encrypting '{os.path.basename(input_path)}' to '{os.path.basename(output_path)}'...")

def decrypt_image(input_path, output_path):
    """Decrypt an image by swapping red and blue channels back."""

    # Open the input image
    img = Image.open(input_path)

    # Load the image pixels
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Decrypt the image by swapping red and blue channels back
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (b, g, r)

    # Save the decrypted image
    img.save(output_path)
    print(f"Decrypting '{os.path.basename(input_path)}' to '{os.path.basename(output_path)}'...")

# Input image path
input_image = r"F:\Prodigy InfoTech\Prodigy_CS_02\Sample Image.jpg"

# Encrypted image path
encrypted_image = r"F:\Prodigy InfoTech\Prodigy_CS_02\encrypted_image.png"

# Decrypted image path
decrypted_image = r"F:\Prodigy InfoTech\Prodigy_CS_02\decrypted_image.png"

# Encrypt the image
print(f"Encrypting '{os.path.basename(input_image)}'...")
encrypt_image(input_image, encrypted_image)

# Decrypt the image
print(f"Decrypting '{os.path.basename(encrypted_image)}'...")
decrypt_image(encrypted_image, decrypted_image)