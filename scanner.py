import cv2
import numpy as np


def reorder_points(points):
    points = points.reshape((4, 2))

    new_points = np.zeros((4, 2), dtype=np.float32)

    # Top-left
    new_points[0] = points[np.argmin(points.sum(axis=1))]

    # Bottom-right
    new_points[2] = points[np.argmax(points.sum(axis=1))]

    # Top-right
    new_points[1] = points[np.argmin(np.diff(points, axis=1))]

    # Bottom-left
    new_points[3] = points[np.argmax(np.diff(points, axis=1))]

    return new_points


def scan_document(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found.")
        return

    original = image.copy()

    # Resize image
    height, width = image.shape[:2]

    max_width = 800

    if width > max_width:
        ratio = max_width / width
        image = cv2.resize(
            image,
            (int(width * ratio), int(height * ratio))
        )

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blur, 75, 200)

    # Find contours
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Sort contours by area
    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    )

    document = None

    # Find four-sided contour
    for contour in contours:

        perimeter = cv2.arcLength(contour, True)

        approx = cv2.approxPolyDP(
            contour,
            0.02 * perimeter,
            True
        )

        if len(approx) == 4:
            document = approx
            break

    if document is None:
        print("Could not find a document.")
        return

    # Get document corners
    points = reorder_points(document)

    top_left = points[0]
    top_right = points[1]
    bottom_right = points[2]
    bottom_left = points[3]

    width_top = np.linalg.norm(top_right - top_left)
    width_bottom = np.linalg.norm(bottom_right - bottom_left)

    max_width = int(max(width_top, width_bottom))

    height_left = np.linalg.norm(bottom_left - top_left)
    height_right = np.linalg.norm(bottom_right - top_right)

    max_height = int(max(height_left, height_right))

    # Destination points
    destination = np.array(
        [
            [0, 0],
            [max_width - 1, 0],
            [max_width - 1, max_height - 1],
            [0, max_height - 1]
        ],
        dtype=np.float32
    )

    # Perspective transformation
    matrix = cv2.getPerspectiveTransform(
        points,
        destination
    )

    scanned = cv2.warpPerspective(
        image,
        matrix,
        (max_width, max_height)
    )

    # Convert scanned document to grayscale
    scanned_gray = cv2.cvtColor(
        scanned,
        cv2.COLOR_BGR2GRAY
    )

    # Improve document appearance
    scanned_result = cv2.adaptiveThreshold(
        scanned_gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Save result
    output_path = "output/scanned_document.jpg"

    cv2.imwrite(
        output_path,
        scanned_result
    )

    print("Document scanned successfully!")
    print("Output saved at:", output_path)


if __name__ == "__main__":

    image_path = "input/document.jpg"

    scan_document(image_path)