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
nibabel
matplotlib

## Usage
```
python nii_to_pdf.py /path/to/image.nii /path/to/output.pdf
```

# Example
I made a pdfs folder in the same directory to make things easier.
```
python nii_to_pdf.py ./MPRAGE.nii ./pdfs/name_for_pdf.pdf
```
## Customizing the Slice Orientation
The script defaults to the middle axial slice, which is: 
```
slice_2d = data[:, :, z]
```
You can edit this line in the script (`nii_to_pdf.py`) to change the orientation:

| Orientation | Code           | Description             |
|-------------|----------------|-------------------------|
| Axial       | `data[:, :, z]` | Top-down head view (default) |
| Coronal     | `data[:, y, :]` | Front view              |
| Sagittal    | `data[x, :, :]` | Side view               |

## Changing Which Slice to Extract
By default, the script selects the middle slice using:
```
z = data.shape[2] // 2
```
To select a specific slice instead:
```
z = 75 # axial slice index
y = 100 # for coronal view
x = 80 # for safittal view
```
## Troubleshooting
- **FileNotFoundError:**
  Make sure the output directory exists.
- **Blank or black image:**
  Try a difference slice index - middle slices may be empty in some acquisitions.
- **Wrong orientation:**
  Try changing `.T` or flipping axes in the `imshow()` call.
