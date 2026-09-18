# SmartDoc Scanner

## Computer Vision Based Document Scanner

SmartDoc Scanner is a simple computer vision application that detects a document from an input photograph and converts it into a flattened scanned image.

The project uses OpenCV techniques such as grayscale conversion, Gaussian blur, Canny edge detection, contour detection, and perspective transformation.

## Features

* Reads a document photograph
* Detects document edges
* Finds the document boundary
* Identifies the four document corners
* Corrects perspective distortion
* Converts the result into a clean scanned image
* Saves the final result automatically

## Technologies Used

* Python
* OpenCV
* NumPy

## Project Structure

```text
SmartDoc-Scanner/
│
├── scanner.py
├── requirements.txt
├── README.md
│
├── input/
│   └── document.jpg
│
└── output/
```

## How It Works

The project follows these steps:

1. The input image is loaded.
2. The image is resized when necessary.
3. The image is converted to grayscale.
4. Gaussian blur is applied to reduce noise.
5. Canny edge detection is used to identify edges.
6. Contours are detected from the edge image.
7. The largest suitable four-sided contour is selected as the document.
8. The four corners of the document are identified.
9. Perspective transformation is applied.
10. The transformed document is converted into a clean black-and-white scanned image.
11. The final image is saved inside the `output` directory.

## Requirements

Python 3.x is required.

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project directory:

```bash
cd SmartDoc-Scanner
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Input Image

Place the document image inside:

```text
input/document.jpg
```

For better results, use an image where the complete document is visible and the document boundary is clearly distinguishable from the background.

## Running the Project

Run the following command from the project root:

```bash
python scanner.py
```

If the document is detected successfully, the program displays:

```text
Document scanned successfully!
Output saved at: output/scanned_document.jpg
```

The processed document can then be found at:

```text
output/scanned_document.jpg
```

## Computer Vision Concepts Used

### Grayscale Conversion

The original color image is converted into grayscale to simplify image processing.

### Gaussian Blur

Blur is applied to reduce small amounts of noise before detecting edges.

### Canny Edge Detection

Canny edge detection identifies strong boundaries in the image.

### Contour Detection

Contours are used to identify possible document boundaries.

### Perspective Transformation

A photograph of a document may contain perspective distortion. Perspective transformation maps the detected document corners to a rectangular shape.

### Thresholding

Adaptive thresholding converts the transformed document into a cleaner black-and-white representation.

## Limitations

The current implementation may have difficulty when:

* The document boundary is not clearly visible.
* The image contains heavy shadows.
* The document is partially hidden.
* The background and document have similar colors.
* The photograph is very blurry.
* More than one large rectangular object is present.

## Future Improvements

Possible improvements include:

* Automatic shadow removal
* Better document detection
* Support for multiple documents
* Mobile application integration
* OCR for extracting document text
* PDF generation
* Improved handling of low-light images
* Deep-learning based document detection

## Conclusion

SmartDoc Scanner demonstrates how fundamental computer vision techniques can be combined to create a practical document-scanning application. The project provides an introduction to edge detection, contours, geometric transformations, and image preprocessing using OpenCV.
