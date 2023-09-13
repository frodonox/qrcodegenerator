import qrcode
qr = qrcode.QRCode(
    version=40 ,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.youtube.com/')
qr.make(fit=True)

img=qr.make_image(back_color=(255, 50, 235),fill_color= (55, 95, 80))
img.save('hola.png')


