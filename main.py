import numpy as np
from PIL import Image

# Load image using PIL
image_path = '/Users/cosminpasat/Downloads/Yodly_error_404_page_design_09706e33-5635-483e-90f7-27781a88d391.png'
image = Image.open(image_path)

# Define desired dimensions and padding color
target_height = image.height
target_width = int(16 / 9 * target_height)

padding_color = (0, 0, 0)  # White color

# Calculate padding values
width, height = image.size
delta_width = target_width - width
delta_height = target_height - height
left_padding = delta_width // 2
top_padding = delta_height // 2
right_padding = delta_width - left_padding
bottom_padding = delta_height - top_padding

# Create a new image with padding
padded_image = Image.new(image.mode, (target_width, target_height), padding_color)
padded_image.paste(image, (left_padding, top_padding))

# Save the padded image to disk
padded_image.save('resized_image.png')