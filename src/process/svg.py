from PIL import Image
import cv2
import numpy as np


def detect_walls(
  input,
  output,
  threshold_value=100,
  thickness_reduction_iterations=5,
  thickness_increase_iterations=3,
  debug=False,
):
  # Read image
  image = cv2.imread(input)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Convert image to binary | Threshold value is used to discard light strokes (doors, furniture)
  _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
  if debug:
    cv2.imshow(f"[DEBUG] Binary Image | Threshold Value = {threshold_value}", binary_image)

  # Reduce the thickness of walls -> Then increase it to remove redundant objects
  kernel = np.ones((3, 3), np.uint8)
  reduced_thickness = cv2.dilate(binary_image, kernel, iterations=thickness_reduction_iterations)
  increased_thickness = cv2.erode(reduced_thickness, kernel, iterations=thickness_increase_iterations)
  cv2.imwrite(output, increased_thickness)


def generate_wall_svg(input, output, scale=2):
  # Open the binary image
  with Image.open(input) as img:
    # Create SVG header
    svg_header = f'<svg width="{img.width*scale}" height="{img.height*scale}" xmlns="http://www.w3.org/2000/svg">\n'

    # Start SVG path
    svg_path = '<path d="'

    # Iterate over each pixel in the image
    for y in range(img.height):
      for x in range(img.width):
        # Check pixel color (assuming black and white image)
        if img.getpixel((x, y)) == 0:
          # If pixel is black, draw a rectangle at that position
          svg_path += f"M{x*scale},{y*scale}h{scale}v{scale}h-{scale}z"

    # Close SVG path and SVG header
    svg_path += '" />\n'
    svg_footer = "</svg>\n"

    # Write SVG to file
    with open(output, "w") as f:
      f.write(svg_header + svg_path + svg_footer)
