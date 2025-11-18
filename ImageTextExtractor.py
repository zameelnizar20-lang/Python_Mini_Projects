import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open image (use raw string or forward slashes)
img = Image.open(r"C:\Users\Admin\Desktop\Daily Dose\Screenshot 2025-11-18 210246.png")

# Preprocess image
img = img.convert("L")  # grayscale
img = img.filter(ImageFilter.SHARPEN)

# Extract text
text = pytesseract.image_to_string(img)
print(text)
