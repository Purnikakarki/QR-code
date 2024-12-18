import qrcode

#data to be encoded in the QR code
data=9765221130

#create a QR code instance
qr = qrcode.QRCode(
    version=1, #controls the sizw of QR code(1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L, #control error corrections
    box_size=10,
    border=4,
    )

#ADD DATA TO QR CODE
qr.add_data(data)
qr.make(fit=True)

#create an image from QR code
img = qr.make_image(fill='black',back_color='white')

#save the image
img.save("qrcode_example.png")

#display the image
img.show()