import qrcode as qr
img = qr.make("https://mail.google.com/mail/u/0/#inbox")
img.save("code.png")