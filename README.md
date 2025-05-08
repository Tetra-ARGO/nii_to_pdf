# NIfTI to PDF Converter

This script converts a `.nii` or `.nii.gz` NIfTI file into a single-page grayscale PDF showing a 2D slice of the image. It's designed for quickly generating shareable views of MRI data, such as MPRAGE scans, for clinical or research use.

---

## Features

- Supports 3D NIfTI files (`.nii` and `.nii.gz`)
- Extracts and renders a single 2D slice
- Saves a high-quality single-page PDF
- Ideal for sharing structural MRI images

---

## Requirements

Install dependencies using the provided `requirements.txt`:

```bash
python -m venv venv
source venv/bin/activate
python install -r requirements.txt
```

`requirements.txt` includes:
