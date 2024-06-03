import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Generate a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.example.com')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("/Users/tom/desktop/qr-code/qrcodeNew.png")

# Decode the QR code
img = Image.open("/Users/tom/desktop/qr-code/qrcodeNew.png")
result = decode(img)

for qr_code in result:
    print(f'Data: {qr_code.data.decode("utf-8")}')