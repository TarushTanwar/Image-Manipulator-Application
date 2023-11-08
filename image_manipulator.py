from PIL import Image

def open_image(file_path):
    try:
        image = Image.open(file_path)
        return image
    except Exception as e:
        print("Error opening the image:", str(e))
        return None

def save_image(image, file_path):
    try:
        image.save(file_path)
        print("Image saved successfully.")
    except Exception as e:
        print("Error saving the image:", str(e))

def grayscale_image(image):
    try:
        grayscale = image.convert('L')
        return grayscale
    except Exception as e:
        print("Error converting the image to grayscale:", str(e))
        return None

def main():
    file_path = 'image.jpg'
    image = open_image(file_path)

    if image:
        grayscale = grayscale_image(image)

        if grayscale:
            save_image(grayscale, 'grayscale_image.jpg')

if __name__ == "__main__":
    main()
