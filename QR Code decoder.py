from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/hp/OneDrive/Documents/QR Code/myQRCode.png')
message = decode(img)
print(message)