import pyodbc
from PySide2 import QtWidgets, QtGui

from ui.GetInfo_form import Ui_Form


class AppForDB(QtWidgets.QMainWindow):
    """Создание конструктора класса приложения"""

    def __init__(self, parent=None):
        super().__init__(parent)  # ссылка на родительский объект с помощью метода super

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.resize(1200, 800)
        self.setWindowTitle("Поиск информации о рейсе")

        self.initUi()
        self.initDB()
        self.initTableViewModel()
        self.ui.pushButton.clicked.connect(self.initTableViewModel)

    def initUi(self):
        self.tableView = QtWidgets.QTableView()

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.tableView)

        self.setLayout(l)

    def initDB(self):
        """Метод для инициализации подключения к базе данных
        :param - server - адрес сервера;
        :param - database - имя базы данных;
        :param - user имя пользователя для авторизации;
        :param - password - пароль к user для авторизации на сервере;
        """
        server = 'vpngw.avalon.ru'
        database = 'DevDB2022_EVGEGO'
        user = 'tsqllogin'
        password = 'Pa$$w0rd'
        self.con = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + server
            + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password)  # инициализация объекта подключения
        self.cursor = self.con.cursor()  # объект курсора осуществления для забросов в БД

        # self.cursor.execute("SELECT * FROM FlySales.RouteDetails") # тест
        # request = self.cursor.fetchall()
        # print(request)

    def initTableViewModel(self):
        """Метод для данных передачи данных, получаемых из запроса от БД в приложение
                """
        sim = QtGui.QStandardItemModel()  # Модель, содержит данные в двумерном представлении
        self.cursor.execute("SELECT StartPoint, FinishPoint FROM FlySales.RouteDetails")
        lst = self.cursor.fetchall()
        for elem in lst:  # Формирование элементов колонок таблицы приложения
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))

        sim.appendRow([item1, item2])
        sim.setHorizontalHeaderLabels(['Город отправления', 'Город прибытия'])  # установка наименования
        # колонок приложения
        self.tableView.setModel(sim)

        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = AppForDB()
    myapp.show()

    app.exec_()
