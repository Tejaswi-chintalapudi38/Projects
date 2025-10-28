"""OCR Verification:
This program uses Python + Tesseract OCR to extract Name and Date of Birth from an image"""

import re
import pytesseract
from PIL import Image

# Step-1: Load the image
image_path = "id_card.jpg"

# Step-2: Extract text from image using OCR
text = pytesseract.image_to_string(Image.open(image_path))

# Step-3: Initialize variables
name = None
dob = None

# Step-4: Clean and process text lines
lines = [line.strip() for line in text.splitlines() if line.strip()]

# Step-5: Finding Date of Birth pattern
for line in lines:
    match = re.search(r'(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](19|20)\d{2}', line)
    if match:
        dob = match.group(0)
        break

# Step-6: Finding Name
for i, line in enumerate(lines):
    if dob and dob in line and i > 0:
        possible_name = lines[i - 1]
        if not re.search(r'\d', possible_name):
            name = possible_name
        break

# Step-7: Fallback
if not name:
    for line in lines:
        if re.search(r'[A-Za-z]', line) and not re.search(r'\d', line):
            name = line
            break

# Step-8: Display extracted information
print("Extracted Information...:")
print("Name:", name or "Not Found")
print("DOB :", dob or "Not Found")

