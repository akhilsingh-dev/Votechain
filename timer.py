import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets

DURATION_INT = 60


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.setGeometry(QtCore.QRect(50,50,350,100))
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        self.pages_qsw = QtWidgets.QStackedWidget()
        vbox.addWidget(self.pages_qsw)
        self.time_passed_qll = QtWidgets.QLabel()
        vbox.addWidget(self.time_passed_qll)

        self.widget_one = QtWidgets.QLabel("Time left to Vote: ")
        self.pages_qsw.addWidget(self.widget_one)
        
        self.timer_start()
        self.update_gui()
        self.show()

    def timer_start(self):
        self.time_left_int = DURATION_INT

        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)

        self.update_gui()

    def timer_timeout(self):
        self.time_left_int -= 1
        if self.time_left_int == 0:
            sys.exit()

        self.update_gui()

    def update_gui(self):
        self.time_passed_qll.setText(str(self.time_left_int))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MyMainWindow()
    sys.exit(app.exec_())