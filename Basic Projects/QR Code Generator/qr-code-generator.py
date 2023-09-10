import qrcode

site_to_redirect = input("Copy and paste the address of the site to be redirected: ")

version = int(input("Enter the QR code version (Maks 40): "))
qr_code_size = int(input("What will be the size of the qr code box? (Maks 3): "))

qr = qrcode.QRCode(version, qr_code_size, border = 5)

qr.add_data(site_to_redirect)

qr.make(fit = True)
img = qr.make_image(fill_color = "black", back_color = "white")

file_name = input("Write what the name of the file will be: ")
img.save(f"{file_name}.png")

print("Qr code created and saved.")
