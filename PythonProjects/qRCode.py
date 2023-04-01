import qrcode  # pip install qrcode (in Terminal)
import os
import time

print("========================================")
print("    Welcome to my QR Code Generator!    ")
print("========================================")
print()
print("Please enter the text you would like to encode into a QR Code.")
print()
text = input("Text: ").strip()
print()
print("Generating QR Code...")
print()
time.sleep(1)
os.system("clear")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
print("QR Code generated!")
print()
print("Thank you for using my QR Code Generator!")
print()
