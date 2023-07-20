
import sqlite3

class DBOperations: 
    con: sqlite3.Connection = None
    cur: sqlite3.Cursor = None
    data: sqlite3.Cursor = None

    # Opening DB connection
    def open_connection(self) -> bool | None: 
      try:
        # In memory DB connection
        # self.con = sqlite3.connect(":memory:")

        # DB file will be opened if exists or created new to establish connection
        self.con = sqlite3.connect("C:\\Data\\Students.db")
        if self.con != None: 
            print("Database connection established successfully. ")
            return True
      
      except Exception as ex:
         print(ex)
       
    # Closing DB connection
    def close_connection(self) -> bool | None: 
       try:
          if self.con != None: 
                self.con.close()
                print("Database connection closed successfully. ")
                return True

       except Exception as ex:
             print(ex)
             return False

    # Executing DML statements sent as an input 
    def exec_ddl_statements(self, ddl_statement : str) -> None: 
        try: 
            if self.con != None: 
                self.cur = self.con.cursor()

            if self.cur != None: 
                self.data = self.cur.execute(ddl_statement)

        except Exception as ex: 
            print(ex)
    
    # Executing DML statements sent as an input 
    def exec_dml_statements(self, dml_statement : str, sql_parameters: any  = None) -> None: 
        try: 
            if self.con != None: 
                self.cur = self.con.cursor()

            if self.cur != None and sql_parameters != None: 
                self.data = self.cur.execute(dml_statement, sql_parameters)
            else: 
                self.data = self.cur.execute(dml_statement)

        except Exception as ex: 
            print(ex)



    # Displaying data received from DML statement such as SELECT. 
    def display_data(self) -> None:
        try:
            print("Table Data: \n")
            if self.data != None: 
                for row in self.data: 
                    print(row)
            else: 
                print("There is a problem in the connection or No records available to display. ")
        except Exception as ex: 
                print(ex)
 

if __name__ == '__main__': 
    dbInstance = DBOperations()
    isConnectionSuccess = dbInstance.open_connection()
    if isConnectionSuccess == True: 
        dbInstance.exec_ddl_statements('CREATE TABLE Student(StudentId, Name)')
        dbInstance.exec_dml_statements("INSERT INTO Student VALUES(?,?)",(1,"Scott"))
        dbInstance.exec_dml_statements("SELECT StudentId, Name FROM Student")
        dbInstance.display_data()
        dbInstance.close_connection()
