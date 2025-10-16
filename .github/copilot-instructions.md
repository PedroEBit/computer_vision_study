# Computer Vision Project Guide for AI Agents

This is a computer vision project focused on image and video processing using OpenCV in Python. Here's what you need to know to be productive:

## Project Structure

```
.
├── data/               # Contains input images and videos
├── visao.ipynb        # Main Jupyter notebook for interactive development
└── visao.py          # Python script version (in development)
```

## Core Technologies

- **OpenCV (cv2)**: Primary library for image/video processing
- **Jupyter**: Interactive development environment
- **IPython.display**: For rendering images and videos in notebooks
- **Python 3.11**: Project runtime environment

## Key Workflows

### Image Processing
- Images are loaded using `cv2.imread()` from the `data/` directory
- Common operations:
  - Color space conversion: `cv2.cvtColor()`
  - Image cropping: Using numpy array slicing
  - Image encoding: `cv2.imencode()` for JPEG conversion

### Video Processing
- Videos are handled using `cv2.VideoCapture()` for both files and webcam
- Video files are loaded from `data/` directory
- Webcam capture uses device index 0 (`cv2.VideoCapture(0)`)

### Display Conventions
1. In Notebooks:
   - Images: Display using `IPython.display.Image`
   - Videos: Embedded using HTML5 video player with base64 encoding
2. In Python scripts:
   - Images: `cv2.imshow()` for window display
   - Videos: Real-time display with `cv2.imshow()` + `cv2.waitKey()`

## Development Environment

- VS Code with Docker support is recommended (see `.vscode/extensions.json`)
- Jupyter notebook kernel: "ds-minimal" with Python 3.11.13

## Best Practices

1. Always verify successful resource loading:
   ```python
   if not video.isOpened():
       print("Erro ao abrir o vídeo.")
   ```

2. Release resources when done:
   ```python
   video.release()
   cv2.destroyAllWindows()
   ```

3. Use appropriate error handling for device access (especially for webcam)

## Notes
- Project is bilingual (English/Portuguese) - error messages and comments appear in Portuguese
- Video/image processing is done in memory to avoid filesystem operations
- Standard image format is JPEG for compatibility