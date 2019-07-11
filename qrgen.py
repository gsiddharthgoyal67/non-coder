import pyqrcode
url = pyqrcode.create('http://uca.edu')
url.svg('uca-url.svg', scale=8)
print(url.terminal(quiet_zone=1))
