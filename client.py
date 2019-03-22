from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Form
import socket
import select
import sys
import re
"""
def run(host, port):
	sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	receiver.connect((host, port))
	sender.sendto(b'M1', (host, port))
	input = [mdreceiver]
	running = 1
	while running:
		rfd, wfr, efd = select.select(input, [], [])
		import msvcrt
		if msvcrt.kbhit(): ready_to_read.append(sys.stdin)
		
		for s in rfd:
			if s == receiver:
				data, addr = receiver.recvfrom(1024)
				print(data)
			elif s == sys.stdin:
				sender.sendto(sys.stdin.readline(),(host,port))
	sender.close()
	receiver.close()

if __name__ == "__main__":
	run('localhost',5005)




"""
class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        # Set up the user interface from Designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect signals
        self.ui.pushButton.clicked.connect(self.send)
  		
		
		# Set params
        self.ui.textEdit.setReadOnly(True)
        self.ui.textEdit.setFontPointSize(16)
        


		
    def send(self):
        self.ui.textEdit.append(self.ui.lineEdit.text())
        
	
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
