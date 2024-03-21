import qrcode

# Define coords
latitude = xx.xxxxxx
longitude = xx.xxxxxx

url = f"http://www.openfiremap.de/?zoom=16&lat={latitude}&lon={longitude}&layers=B0000TT"

# Create QR-Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Save QR-Code 
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")

print("QR-Code created.")
