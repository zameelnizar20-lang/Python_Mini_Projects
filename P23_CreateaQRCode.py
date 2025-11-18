# ----------------------------------------
# QR Code Generator (Simple Version)
# ----------------------------------------

import qrcode  # Import the QR code library

# Step 1: Get input from the user
data = input("Enter the text or URL to generate QR code: ")

# Step 2: Generate QR code
qr_img = qrcode.make(data)

# Step 3: Save the QR code as an image
qr_img.save("my_qr.png")

print("✅ QR Code successfully generated and saved as 'my_qr.png'!")
