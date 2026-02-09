# MirrorImages

A Python module to create mirror (horizontally flipped) images, supporting both single files and entire directories.

## Features

- 🖼️ **Single File Processing** — Mirror individual images
- 📁 **Batch Processing** — Mirror all images in a folder
- 🔧 **Multiple Formats** — Supports JPEG, PNG, JPG, BMP

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Pillow (PIL)

## Installation

```bash
pip install opencv-python pillow
```

## Usage

```python
from mirror import Mirror

# Initialize
m = Mirror()

# Mirror a single image
m.mirror_file('/path/to/image.jpg')

# Mirror all images in a folder
m.mirror_folder('/path/to/folder/')
```

## Supported Extensions

- `.jpeg`
- `.jpg`
- `.png`
- `.bmp`

## Output

Mirrored images are saved in the same directory with a modified filename.

## How It Works

1. Loads image using PIL/OpenCV
2. Applies horizontal flip transformation
3. Saves the mirrored version alongside the original

## License

MIT

---

## CI Status

All PRs are checked for:
- ✅ Syntax (Python, JS, TS, YAML, JSON, Dockerfile, Shell)
- ✅ Secrets (No hardcoded credentials)
- ✅ Security (High-severity vulnerabilities)

