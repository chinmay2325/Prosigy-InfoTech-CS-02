from PIL import Image

def encrypt_image(img_path, key):
    img = Image.open(img_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save("encrypted.png")
    print("Image encrypted and saved as 'encrypted.png'")

def decrypt_image(img_path, key):
    img = Image.open(img_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save("decrypted.png")
    print("Image decrypted and saved as 'decrypted.png'")

key = int(input("Enter encryption key: "))
encrypt_image("input.png", key)
decrypt_image("encrypted.png", key)
