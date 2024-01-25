import cv2
import numpy as np
import color


def detect(input: str = "input/fp1.png", output: str = "output/out.png", debug=False):
    image = cv2.imread(input)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold_value = 100  # Discard light strokes (doors, furniture)
    _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Single pixel morphological erosion
    kernel = np.ones((3, 3), np.uint8)
    edges = binary_image - cv2.erode(binary_image, kernel)  # type: ignore

    # Find and draw contours in the dilated image
    im_copy = edges.copy()  # cv2.findContours is destructive
    contours, _ = cv2.findContours(im_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result_image = image.copy()
    if debug is True:
        cv2.drawContours(result_image, contours, -1, color.MAGENTA, 2)

    vertices = []
    for contour in contours:
        epsilon = 0.001 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        vertices.extend(approx)

    for vertex in vertices:
        x, y = vertex.ravel()
        cv2.circle(result_image, (x, y), 3, color.MAGENTA, -1)
        if debug is True:
            cv2.putText(result_image, f"({x}, {y})", (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color.MAGENTA, 2)

    # Overlay
    cv2.imshow("Detected Edges", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save
    cv2.imwrite(output, result_image)


detect()
