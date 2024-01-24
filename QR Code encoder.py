import qrcode
from PIL import Image

data_encoded = 'This is my first made QR Code'
img = qrcode.make(data_encoded)
img.save('C:/Users/hp/OneDrive/Documents/QR Code/myQRCode.png')


qr = qrcode.QRCode(version = 1, box_size =10, border = 5 )
qr.add_data(data_encoded)
qr.make(fit = True)
img = qr.make_image(fill_color = 'red', back_color = 'white' )
img.save('C:/Users/hp/OneDrive/Documents/QR Code/myQRCode1.png')