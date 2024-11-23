class AirlinesRepository:
    def __init__(self, db_template):
        super(AirlinesRepository, self).__init__()
        self.__db_template = db_template
        self.__model_name = 'airlines'

    def get_model_name(self):
        return self.__model_name

    def set_up(self):
        sql_query = (
            f"CREATE TABLE IF NOT EXISTS {self.__model_name} (id {self.__db_template.get_auto_increment_type()}, "
            f"name VARCHAR, alt_name VARCHAR, iata VARCHAR, icao VARCHAR, callsign VARCHAR, country VARCHAR, "
            f"active VARCHAR)")
        self.__db_template.execute_query(sql_query, [])

    def create(self, name, alt_name, iata, icao, callsign, country, active):
        placeholder = self.__db_template.get_prepared_placeholder()
        sql_query = (f"INSERT INTO {self.__model_name} (name, alt_name, iata, icao, callsign, country, active) "
                     f"VALUES({placeholder},{placeholder},{placeholder},{placeholder},{placeholder},{placeholder},"
                     f"{placeholder})")
        self.__db_template.execute_query(sql_query, [name, alt_name, iata, icao, callsign, country, active])

    def update(self, date, category, description, balance, status, id):
        placeholder = self.__db_template.get_prepared_placeholder()
        sql_query = (f"UPDATE {self.__model_name} SET name={placeholder}, alt_name={placeholder}, iata={placeholder}, "
                     f"icao={placeholder}, callsign={placeholder}, country={placeholder}, active={placeholder} "
                     f"WHERE ID={placeholder}")
        self.__db_template.execute_query(sql_query, [date, category, description, balance, status, id])

    # todo: add search queries

    def delete(self, id):
        placeholder = self.__db_template.get_prepared_placeholder()
        sql_query = f"DELETE FROM {self.__model_name} WHERE ID={placeholder}"
        self.__db_template.execute_query(sql_query, [id])
