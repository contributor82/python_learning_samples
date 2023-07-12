
import sqlite3

class DBOperations: 
    con : sqlite3.Connection = None
    cur = None
    data = None

    # Getting an error while opening DB connection
    def open_connection(self): 
      try:
        self.con =  sqlite3.connect('Data source=FUTURE\\SQLSERVER_DEV;Integrated Security=SSPI;Database=Students; User Instance=true; Encrypt=true;Trust Server Certificate=true;')
        if self.con != None: 
            print("Database connection established successfully. ")
            return True
      except sqlite3.DatabaseError as ex: 
         print(ex)
         return False
    
    # Executing DML statements sent as an input 
    def exec_dml_statements(self, dml_statement): 
        try: 
            if self.con != None: 
                self.cur = self.con.cursor()

            if self.cur != None: 
                self.data = self.cur.execute(dml_statement)
        except Exception as ex: 
            print(ex)

    # Displaying data received from DML statement such as SELECT. 
    def display_data(self):
        try:
            if self.data != None: 
                for row in self.data: 
                    print(row)
            else: 
                print("There is a problem in the connection or No records to display. ")
        except Exception as ex: 
                print(ex)
 

dbInstance = DBOperations()
isConnectionSuccess = dbInstance.open_connection()
if isConnectionSuccess == True: 
    dbInstance.exec_dml_statements('SELECT * FROM [dbo].[Students]')
    dbInstance.display_data()
