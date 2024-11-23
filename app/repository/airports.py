class AirportsRepository:
    def __init__(self, db_template):
        super(AirportsRepository, self).__init__()
        self.__db_template = db_template
        self.__model_name = 'airports'

    def get_model_name(self):
        return self.__model_name

    def set_up(self):
        sql_query = (
            f"CREATE TABLE IF NOT EXISTS {self.__model_name} (id {self.__db_template.get_auto_increment_type()}, "
            f"airport VARCHAR, city VARCHAR, country VARCHAR, iata VARCHAR, icao VARCHAR, latitude REAL, "
            f"longitude REAL, elevation integer, utc integer, dst VARCHAR, region VARCHAR)")
        self.__db_template.execute_query(sql_query, [])

    def create(self, airport, city, country, iata, icao, latitude, longitude, elevation, utc, dst, region):
        placeholder = self.__db_template.get_prepared_placeholder()
        sql_query = (f"INSERT INTO {self.__model_name} (airport, city, country, iata, icao, latitude, "
                     f"longitude, elevation, utc, dst, region) "
                     f"VALUES({placeholder},{placeholder},{placeholder},{placeholder},{placeholder},{placeholder},"
                     f"{placeholder},{placeholder},{placeholder},{placeholder},{placeholder})")
        self.__db_template.execute_query(sql_query,
                                         [airport, city, country, iata, icao, latitude, longitude, elevation, utc, dst,
                                          region])

    def update(self, airport, city, country, iata, icao, latitude, longitude, elevation, utc, dst, region, id):
        placeholder = self.__db_template.get_prepared_placeholder()
        sql_query = (
            f"UPDATE {self.__model_name} SET airport={placeholder}, city={placeholder}, country={placeholder}, "
            f"iata={placeholder}, icao={placeholder}, latitude={placeholder}, "
            f"longitude={placeholder}, elevation={placeholder}, utc={placeholder}, dst={placeholder},"
            f" region={placeholder} WHERE ID={placeholder}")
        self.__db_template.execute_query(sql_query, [airport, city, country, iata, icao, latitude, longitude,
                                                     elevation, utc, dst, region, id])

    # todo: add search queries

    def delete(self, id):
        sql_query = f"DELETE FROM {self.__model_name} WHERE ID=?"
        self.__db_template.execute_query(sql_query, [id])
