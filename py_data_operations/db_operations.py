""" Module for db operations."""
import sqlite3

class DBOperations:
    """ Database operations """

    db_con: sqlite3.Connection
    cur: sqlite3.Cursor
    data: sqlite3.Cursor
    is_con_open: bool

    def db_connect(self, db_path_name: str) -> bool | None:
        """ Function opening DB connection. """
        self.is_con_open = False
        try:
            # DB file will be opened if exists or created new to establish connection
            self.db_con = sqlite3.connect(db_path_name)
            print('Database connection established successfully. ')
            self.is_con_open = True

        except ConnectionError as conn_error:
            print(conn_error)
            self.is_con_open = False

        return self.is_con_open

    def db_disconnect(self) -> bool | None:
        """ Closing connection """
        is_con_close: bool = False
        try:
            if self.is_con_open:
                self.db_con.close()
                print('Database connection closed successfully. ')
                is_con_close = True

        except ConnectionError as conn_error:
            print(conn_error)
            is_con_close = False

        return is_con_close

    def exec_ddl_query(self, ddl_statement: str) -> None:
        """ Execute DDL Statements """
        try:
            if self.is_con_open:
                self.cur = self.db_con.cursor()
                self.data = self.cur.execute(ddl_statement)
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)


    def exec_batch_ddl_query(self, ddl_statement: str) -> None:
        """ Execute Batch DDL Statements """
        try:
            if self.is_con_open:
                self.cur = self.db_con.cursor()
                self.data = self.cur.executescript(ddl_statement)
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)

    def exec_dml_query(self, dml_statement: str,
                            sql_parameters: list[int | str] | None = None) -> None:  # type: ignore
        """ Execcute DML Statements """
        try:
            if self.is_con_open:
                self.cur = self.db_con.cursor()

            if sql_parameters is not None:
                self.data = self.cur.execute(dml_statement, sql_parameters) # type: ignore
            else:
                self.data = self.cur.execute(dml_statement)
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)


    def exec_batch_dml_query(self, dml_statement: str,
                                  sql_params:
                                  list[tuple[int, int, str, int]] | None) -> None: # type: ignore
        """ Executing batch DML statements """
        try:
            if self.is_con_open:
                self.cur = self.db_con.cursor()

            if sql_params is not None:
                self.data = self.cur.executemany(dml_statement, sql_params) # type: ignore
            else:
                self.data = self.cur.execute(dml_statement)
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)

    def display_data(self) -> None:
        """ Displaying data received from DML statement such as SELECT. """
        try:
            print('Table Data: \n')
            records: list[object] = self.data.fetchall()
            for row in records:
                print(row)
            # else:
            #      print(
            #          "There is a problem in the connection or No records available to display. ')
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)

    def display_scalar_data(self) -> None:
        """ Displaying data received from DML statement such as SELECT. """
        try:
            print('Table Data: \n')
            print('Scalar Value: ', self.data.fetchone())
            # else:
            #     print(
            #         "There is a problem in the connection or No records available to display. ')
        except sqlite3.DataError as sql_data_error:
            print(sql_data_error)
        except sqlite3.Error as sql_error:
            print(sql_error)

if __name__ == '__main__':
    db_instance = DBOperations()
    db_path: str = 'C:\\Data\\sample_data.db'
    is_connection_success: bool | None = db_instance.db_connect(
        db_path)
    if is_connection_success:

        db_instance.exec_ddl_query(
            'CREATE TABLE Student(StudentId, Name)')

        parameters: list[int | str] = []
        parameters.append(1)
        parameters.append('Scott')

        db_instance.exec_dml_query(
            'INSERT INTO Student VALUES(?,?)', parameters) # (1, 'Scott')
        parameters.clear()
        parameters.append(2)
        parameters.append('Martin')
        db_instance.exec_dml_query(
            'INSERT INTO Student VALUES(?,?)', parameters)
        db_instance.exec_dml_query('SELECT StudentId, Name FROM Student', None)
        db_instance.display_data()

        db_instance.exec_dml_query(
            'SELECT COUNT(StudentId) as num_of_students FROM Student',  None)
        db_instance.display_scalar_data()

        db_instance.exec_ddl_query(
            'CREATE TABLE Marks(MarksId, StudentId, SubjectName, SubjectMarks)')

        batch_parameters: list[tuple[int, int, str, int]] = [(1, 1, 'Physics', 75),
                                               (2, 1, 'Chemistry', 85),
                                                  (3, 1, 'Maths', 90),
                                                  (4, 1, 'Biology', 78)]
        db_instance.exec_batch_dml_query(' INSERT INTO Marks(MarksId, StudentId, '
                                               + ' SubjectName, SubjectMarks) VALUES(?,?,?,?)',
                                              batch_parameters)

        db_instance.exec_dml_query(
            'SELECT MarksId, StudentId, SubjectName, SubjectMarks FROM Marks', None)
        db_instance.display_data()

        db_instance.exec_batch_ddl_query('''
                                    BEGIN;
                                    CREATE TABLE Person(PersonId, FirstName, LastName, Age);
                                    CREATE TABLE Book(BookId, Title, Author, Published);
                                    CREATE TABLE Publisher(PublisherId, Name, Address);
                                    COMMIT;
                                        ''')
        db_instance.db_disconnect()
