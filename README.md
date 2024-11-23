## Desktop Application example (PySide6) 


### Requirements

Python 3.11

### Install pyside6
~~~
pip install pyside6
~~~

### Convert qt files

~~~
pyside6-rcc ui/qt/res-rs.qrc -o ui/res.py
~~~

~~~
pyside6-uic ui/qt/main_avia_window.ui -o ui/main_avia_window.py
~~~

~~~
pyside6-uic ui/qt/flights_modify_modal.ui -o ui/flights_modify_modal.py
~~~

~~~
pyside6-uic ui/qt/airports_modify_modal.ui -o ui/airports_modify_modal.py
~~~


## Docker

~~~
docker run --name pg-db-16 -e ALLOW_EMPTY_PASSWORD=yes -p 5432:5432 -d bitnami/postgresql:16
~~~