from PIL import Image

def compress_image(source_image_path, target_image_path, output_image_path):
    # Open images
    source_image = Image.open(source_image_path)
    target_image = Image.open(target_image_path)

    # Resize source image to fit into target image (optional step)
    source_image = source_image.resize(target_image.size)

    # Convert source image to RGB mode
    source_image = source_image.convert("RGB")

    # Get pixel data from images
    source_pixels = source_image.load()
    target_pixels = target_image.load()

    # Embed source image into target image (using LSB)
    for i in range(target_image.size[0]):
        for j in range(target_image.size[1]):
            r, g, b = source_pixels[i, j]
            target_pixels[i, j] = (target_pixels[i, j][0] & 0xFC | r >> 6,
                                   target_pixels[i, j][1] & 0xFC | g >> 6,
                                   target_pixels[i, j][2] & 0xFC | b >> 6)

    # Save the modified target image
    target_image.save(output_image_path)

# Usage
source_image_path = 'C:/Users/porpu/Desktop/Code/CSS423/1.jpg'
target_image_path = 'C:/Users/porpu/Desktop/Code/CSS423/2.jpg'
output_image_path = 'C:/Users/porpu/Desktop/Code/CSS423/3.jpg'

compress_image(source_image_path, target_image_path, output_image_path)
