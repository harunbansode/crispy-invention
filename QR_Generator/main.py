import qrcode


def generate_QR(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='green', back_color='white')
    img.save('qrproject.png')


url = input('Enter URL: ')
generate_QR(url)
print('Done...')
