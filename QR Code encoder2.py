import qrcode               #This imports the `qrcode` library for generating QR codes and the `Image` class from the `PIL` (Pillow) library for image manipulation.
from PIL import Image

data_encoded = 'I love coding😍'   #This variable holds the data that will be encoded into the QR code.


# Generate the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data_encoded)
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

# Convert the QR code image to RGB mode
qr_image = qr_image.convert('RGB')

# Create a solid red image of the same size as the QR code image
red_image = Image.new('RGB', qr_image.size, (0, 255, 0))

# Composite the QR code image with the red image
final_image = Image.blend(qr_image, red_image, alpha=0.5)

# Save the final image
final_image.save('C:/Users/hp/OneDrive/Documents/QR Code/myQRCode3.png')
