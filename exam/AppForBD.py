import pyodbc
from PySide2 import QtWidgets, QtGui

from ui.GetInfo_form import Ui_Form


class AppForDB(QtWidgets.QMainWindow):
    """Создание конструктора класса приложения, для выполнения поискового запроса о авиа рейсах"""

    def __init__(self, parent=None):
        super().__init__(parent)  # ссылка на родительский объект с помощью метода super

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.resize(1200, 800)
        self.setWindowTitle("Поиск информации о рейсе")
        self.ui.lineEdit_2.editingFinished.connect(self.ChangeStartPoint)
        self.ui.lineEdit_4.editingFinished.connect(self.ChangeFinishPoint)

        self.initUi()
        self.initDB()
        self.initTableViewModel()
        self.ChangeStartPoint()
        self.ChangeFinishPoint()

    def initUi(self):
        self.tableView = QtWidgets.QTableView()

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.tableView)

        self.setLayout(l)

    def ChangeStartPoint(self):
        """Метод устанавливает поиск для StartPoint  посредством запроса к БД, где % % - любая строка,
        содержащая 0 и более символов """

        print(f"SELECT StartPoint FROM FlySales.RouteDetails  WHERE StartPoint LIKE %{self.ui.lineEdit_2.text()}%")

    def ChangeFinishPoint(self):
        """Метод устанавливает поиск для FinishPoint  посредством запроса к БД, где % % - любая строка,
               содержащая 0 и более символов """

        print(f"SELECT FinishPoint FROM FlySales.RouteDetails  WHERE StartPoint LIKE %{self.ui.lineEdit_4.text()}%")

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """Метод выводит предупреждающую информацию при попытке закрытия диалогового окна"""
        reply = QtWidgets.QMessageBox.question(self,
                                                   'Поиск информации о рейсах', 'Вы действительно хотите закрыть приложение?',
                                                   QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)

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
        self.cursor.execute('SELECT D.StartPoint, D.FinishPoint, D.TravelTime, D.TotalDistance '
                            'FROM FlySales.RouteDetails AS D')
        lst = self.cursor.fetchall()
        for elem in lst:  # Передача данных в модель, формирование элементов колонок таблицы приложения
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))

        sim.appendRow([item1, item2, item3, item4])
        sim.setHorizontalHeaderLabels(['Город отправления', 'Город прибытия', 'Время пути', 'Протяженность пути'])
        # установка наименования таблицы приложения

        self.tableView.setModel(sim)

        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = AppForDB()
    myapp.show()

    app.exec_()
