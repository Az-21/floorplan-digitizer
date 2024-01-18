import cv2
from process import color
from process import helper


def detect(cwd: str):
    image = cv2.imread(f"{cwd}\\input\\fp1.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blurred, 100, 150)

    # Size of kernel affects the dilation. Setting it to `None` detects outermost boundary of house
    dilated = cv2.dilate(edges, (1, 1), iterations=1)  # type: ignore

    # Find and draw contours in the dilated image
    contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result_image = image.copy()
    cv2.drawContours(result_image, contours, -1, color.MAGENTA, 2)

    # Overlay
    cv2.imshow("Detected Edges", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save
    # base_name = helper.remove_extension(filename)
    cv2.imwrite(f"{cwd}\\output\\fp1-edge.png", result_image)
