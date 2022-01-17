import pyqrcode


def qr_code():
    qr = pyqrcode.create(input("Enter data to convert into QR Code: "))
    qr.png("qrcode.png", scale=6)
    print("QR code generated")


if __name__ == "__main__":
    qr_code()
