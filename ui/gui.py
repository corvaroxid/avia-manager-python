import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow

from airports_modify_modal import Ui_Dialog as Airports_Ui_Dialog
from app.db.templates import SqLiteTemplate, PostgresqlTemplate
from app.repository.airlines import AirlinesRepository
from app.repository.airports import AirportsRepository
from app.repository.routes import RoutesRepository

from flights_modify_modal import Ui_Dialog as Flights_Ui_Dialog
from main_avia_window import Ui_MainWindow


# todo: refactoring. Split methods
class AviaManager(QMainWindow):
    def __init__(self):
        super(AviaManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.template = SqLiteTemplate()
        self.template.create_connection()

        self.airports = AirportsRepository(self.template)
        self.airports.set_up()

        self.airlines = AirlinesRepository(self.template)
        self.airlines.set_up()

        self.routes = RoutesRepository(self.template)
        self.routes.set_up()

        self.refresh_airports_view_data()

        self.ui.btn_new_transaction.clicked.connect(self.open_modify_modal)
        self.ui.btn_edit_transaction.clicked.connect(self.open_modify_modal)
        self.ui.btn_delete_transaction.clicked.connect(self.delete_entity)

        self.ui.rb_airports.clicked.connect(self.refresh_airports_view_data)
        self.ui.rb_flights.clicked.connect(self.refresh_flights_view_data)

    def open_modify_modal(self):
        if self.ui.rb_airports.isChecked():
            self.new_window = QtWidgets.QDialog()
            self.airport_ui_modal = Airports_Ui_Dialog()
            self.airport_ui_modal.setupUi(self.new_window)
            self.new_window.show()
            sender = self.sender()
            print(sender.text())
            if sender.text() == "Create":
                self.airport_ui_modal.btn_new_transaction.clicked.connect(self.add_new_airport)
            else:
                self.airport_ui_modal.btn_new_transaction.clicked.connect(self.edit_airport)
        else:
            self.new_window = QtWidgets.QDialog()
            self.flight_ui_modal = Flights_Ui_Dialog()
            self.flight_ui_modal.setupUi(self.new_window)
            self.new_window.show()
            sender = self.sender()

            if sender.text() == "Create":
                self.flight_ui_modal.btn_new_transaction.clicked.connect(self.add_new_flight)
            else:
                self.flight_ui_modal.btn_new_transaction.clicked.connect(self.edit_flight)

    def add_new_airport(self):
        airport = self.airport_ui_modal.le_name.text()
        city = self.airport_ui_modal.le_city.text()
        country = self.airport_ui_modal.le_country.text()
        iata = self.airport_ui_modal.le_iata.text()
        icao = self.airport_ui_modal.le_icao.text()
        latitude = self.airport_ui_modal.le_latitude.text()
        longitude = self.airport_ui_modal.le_longitude.text()

        self.airports.create(airport, city, country, iata, icao, latitude, longitude, 0, 10, '', '')
        self.refresh_airports_view_data()
        self.new_window.close()

    def edit_airport(self):
        index = self.ui.tableView.selectedIndexes()[0]

        airport = self.airport_ui_modal.le_name.text()
        city = self.airport_ui_modal.le_city.text()
        country = self.airport_ui_modal.le_country.text()
        iata = self.airport_ui_modal.le_iata.text()
        icao = self.airport_ui_modal.le_icao.text()
        latitude = self.airport_ui_modal.le_latitude.text()
        longitude = self.airport_ui_modal.le_longitude.text()

        self.airports.update(airport, city, country, iata, icao, latitude, longitude, 0, 10, '', '', index)
        self.refresh_airports_view_data()
        self.new_window.close()

    def add_new_flight(self):
        airline = self.flight_ui_modal.le_airline.text()
        source = self.flight_ui_modal.le_source.text()
        destination = self.flight_ui_modal.le_destination.text()

        self.routes.create(airline, 0, source, 0, destination, 0, '',
                           0, '', 0, 0, 0, 0, 0)

        self.refresh_flights_view_data()
        self.new_window.close()

    def edit_flight(self):
        index = self.ui.tableView.selectedIndexes()[0]

        airline = self.flight_ui_modal.le_airline.text()
        source = self.flight_ui_modal.le_source.text()
        destination = self.flight_ui_modal.le_destination.text()

        # todo: update logic
        self.new_window.close()

    def delete_entity(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.airports.delete(id)
        self.refresh_airports_view_data()

    def refresh_flights_view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable(self.routes.get_model_name())
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def refresh_airports_view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable(self.airports.get_model_name())
        self.model.select()
        self.ui.tableView.setModel(self.model)


#todo: show search results

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AviaManager()
    window.show()

    sys.exit(app.exec())
