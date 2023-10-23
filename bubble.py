from PIL import Image, ImageSequence
import imghdr
import os

image_bulle_path = "bubble.png"

def find_image_with_prefix(directory):
    if not os.path.exists(directory):
        return None

    for filename in os.listdir(directory):
        if filename.startswith("image"):
            return os.path.join(directory, filename)

    return None

imagePath = find_image_with_prefix(os.getcwd())

if (imagePath == None):
    print('No image found')
    exit(1)

def is_gif_or_png(image_path):
    print(image_path)
    image_type = imghdr.what(image_path)
    print(image_type)
    if (image_type == 'gif'):
        return 'gif'
    if (image_type == 'png'):
        return 'png'
    if (image_type == 'jpeg'):
        return 'jpeg'
    else:
        return 0
    

if is_gif_or_png(imagePath):
    image = Image.open(f'image.{is_gif_or_png(imagePath)}')
else:
    print(imagePath)
    print("Image is not a PNG or a GIF.")
    exit(1)

image_bubble = Image.open(image_bulle_path)

largeur_image, hauteur_image = image.size
image_bubble = image_bubble.resize((largeur_image, hauteur_image // 4))

if image.is_animated:
    frames = [frame.copy() for frame in ImageSequence.Iterator(image)]
    for i in range(len(frames)):
        frames[i] = frames[i].convert("RGBA")
        frames[i].paste(image_bubble, (0, 0), image_bubble)
        frames[i] = frames[i].convert("RGB")

    frames[0].save("gange.gif", save_all=True, append_images=frames[1:], loop=0, disposal=2)
else:
    image.paste(image_bubble, (0, 0), image_bubble)
    image.save("result.gif")

print("Image saved as 'result.gif'")
