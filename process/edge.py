import cv2
import numpy as np
from . import color


def detect(
    input,
    output,
    threshold_value=100,
    thickness_reduction_iterations=5,
    debug=False,
    debug_vertex_position=False,
):
    # Read image
    image = cv2.imread(input)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert image to binary | Threshold value is used to discard light strokes (doors, furniture)
    _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    if debug:
        cv2.imshow(f"[DEBUG] Binary Image | Threshold Value = {threshold_value}", binary_image)

    # Reduce the thickness of walls
    kernel = np.ones((3, 3), np.uint8)
    reduced_thickness = cv2.dilate(binary_image, kernel, iterations=thickness_reduction_iterations)
    if debug:
        cv2.imshow(f"[DEBUG] Reduced Thickness | Iterations = {thickness_reduction_iterations}", reduced_thickness)

    # Single pixel morphological erosion (edge detection)
    kernel = np.ones((3, 3), np.uint8)
    edges = reduced_thickness - cv2.erode(reduced_thickness, kernel)  # type: ignore

    # Find and draw contours in the dilated image
    im_copy = edges.copy()  # cv2.findContours is destructive
    contours, _ = cv2.findContours(im_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result_image = image.copy()

    # Find vertices of the image
    vertices = []
    for contour in contours:
        epsilon = 0.001 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        vertices.extend(approx)

    # Plot vertices of the image on the original, unmodified image
    for vertex in vertices:
        x, y = vertex.ravel()
        if debug:
            cv2.circle(result_image, (x, y), 3, color.MAGENTA, -1)
        if debug and debug_vertex_position is True:
            cv2.putText(result_image, f"({x}, {y})", (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color.MAGENTA, 2)

    # Overlay
    cv2.imshow("Detected Edges", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save
    cv2.imwrite(output, result_image)
