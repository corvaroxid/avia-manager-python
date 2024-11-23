class RoutesRepository:
    def __init__(self, db_template):
        super(RoutesRepository, self).__init__()
        self.__db_template = db_template
        self.__model_name = 'routes'

    def get_model_name(self):
        return self.__model_name

    def set_up(self):
        sql_query = (
            f"CREATE TABLE IF NOT EXISTS {self.__model_name} (id {self.__db_template.get_auto_increment_type()}, "
            f"airline VARCHAR, airline_id integer, src_airport VARCHAR, src_airport_id integer, dst_airport VARCHAR, "
            f"dst_airport_id integer, codeshare VARCHAR, stops integer, airplane VARCHAR, airlines_id integer, "
            f"airports_id integer, airports_id1 integer, airports_id2 integer, airports_id3 integer)")
        self.__db_template.execute_query(sql_query, [])

    def create(self, airline, airline_id, src_airport, src_airport_id, dst_airport, dst_airport_id, codeshare, stops,
               airplane, airlines_id, airports_id, airports_id1, airports_id2, airports_id3):
        placeholder = self.__db_template.get_prepared_placeholder()
        sql_query = (f"INSERT INTO {self.__model_name} (airline, airline_id, src_airport, src_airport_id, dst_airport, "
                     f"dst_airport_id, codeshare, stops, airplane, airlines_id, airports_id, airports_id1, "
                     f"airports_id2, airports_id3)"
                     f"VALUES({placeholder},{placeholder},{placeholder},{placeholder},{placeholder},{placeholder},"
                     f"{placeholder},{placeholder},{placeholder},{placeholder},{placeholder},{placeholder},{placeholder},"
                     f"{placeholder})")
        self.__db_template.execute_query(sql_query,
                                         [airline, airline_id, src_airport, src_airport_id, dst_airport, dst_airport_id,
                                          codeshare, stops, airplane, airlines_id, airports_id, airports_id1,
                                          airports_id2, airports_id3])

    # todo: add search queries

    def delete(self, id):
        placeholder = self.__db_template.get_prepared_placeholder()
        sql_query = f"DELETE FROM {self.__model_name} WHERE ID={placeholder}"
        self.__db_template.execute_query(sql_query, [id])
