#!/usr/bin/env python3

import os
import sys
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def convert_single_nifti_to_pdf(nifti_path, output_pdf_path):
    img = nib.load(nifti_path)
    data = img.get_fdata()

    # Use middle axial slice
    z_mid = data.shape[2] // 2
    slice_2d = data[:, :, z_mid]

    # Normalize to 0–255 for visualization
    slice_norm = (slice_2d - np.min(slice_2d)) / (np.max(slice_2d) - np.min(slice_2d))

    # Save as single-page PDF
    with PdfPages(output_pdf_path) as pdf:
        plt.figure(figsize=(6, 6))
        plt.imshow(slice_norm.T, cmap='gray', origin='lower')
        plt.axis('off')
        plt.title(os.path.basename(nifti_path), fontsize=10)
        pdf.savefig(bbox_inches='tight')
        plt.close()

    print(f"Saved PDF: {output_pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nii_to_pdf.py /path/to/file.nii /path/to/output.pdf")
        sys.exit(1)

    input_nii = sys.argv[1]
    output_pdf = sys.argv[2]
    convert_single_nifti_to_pdf(input_nii, output_pdf)

