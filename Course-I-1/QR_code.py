import pyqrcode

address = 'https://vu.pilco.bg/vuapp/'
url = pyqrcode.create(address)
url.png('vu.png', scale=8)
