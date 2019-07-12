import pyqrcode
url = pyqrcode.create('http://13.235.20.91')
url.svg('uca-url.svg', scale=8)
print(url.terminal(quiet_zone=1))
