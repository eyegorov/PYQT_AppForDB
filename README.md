```gherkin
Оконное приложение AppForDB разработано c помощью фреймфорка Pyside2.

Дает возможность подключиться к БД, вывести минимальный набор данных в отдельное представление.

Приложение может быть переработано для подключения к другой БД, с добавлением более функциональных методов для взаимодейстивя с БД.

```

```gherkin
Для запуска приложения необходимо выполнить следующие действия:
```
````cython
1.git clone  # сделать URL на проект, либо скачать архив и заустить как отдельный проект;
2 Инициализировать виртуальное окружение;
3 pip install -r requireents.txt # развернуть зависимости;
4. AppForBD.py - исполнительный файл для запуска приложения.
5. GetInfo_form.py - адаптированная под Python форма приложения
6. После запуска исполнительного файла AppForBD.py откроется окно приложения для поиска информации
7. Данные в поля окон "Город отправления" и "Город прибытия" вносятся латискими буквами A-Z
8 В методе def initTableViewModel(self) предусмотрен тестовый вывод информации от запроса в консоль, в случае, 
  если запрос в базе данных нет соответсвующей информации в консоль выведется пустой список []




