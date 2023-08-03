import sqlite3

class SQlLiteShell: 
    con : sqlite3.Connection
    cur: sqlite3.Cursor
    is_open_connection: bool
    shell_input: str = ""
    data: list[str]

    def open_connection(self):
       ### Opening memory connection ###

        self.is_open_connection = False
        try:
            self.con = sqlite3.connect(":memory:")
            if isinstance(self.con, sqlite3.Connection): 
                print("Database connection established successfully. ")
                self.con.isolation_level = None
                self.cur = self.con.cursor()
                self.is_open_connection = True

        except ConnectionError as ex:
            print(ex)
            self.is_open_connection = False

        return self.is_open_connection

    def accept_command_line_input(self): 
        ### Accepting SQL as command line input ###

        print("Enter SQL Command : ")
        self.shell_input = ""
        try: 
            while True: 
                line = input()
                if line == "":
                    break
                self.shell_input += line
        
        except Exception as ex: 
            print(ex)

    def exec_sql_statement(self): 
       ### Executing SQL Statement ###

        # if sqlite3.complete_statement(self.shell_input): 
            try:
                self.shell_input = self.shell_input.strip()
                self.cur = self.cur.execute(self.shell_input)

                if self.shell_input.lstrip().upper().startswith("SELECT"):
                    self.data = self.cur.fetchall()

            except sqlite3.Error as sql_error: 
                print(sql_error.args[0])
            except Exception as ex: 
                print(ex)


    def display_sql_output(self): 
        ### Displaying SQL Output ### 

        try: 
            print(self.data)

        except sqlite3.DataError as sql_data_error: 
            print(sql_data_error.args[0])
        except sqlite3.Error as sql_error: 
            print(sql_error.args[0])
        except Exception as ex:
            print(ex.args[0])


    def close_connection(self) -> bool | None:
        ### Closing connection ###

        is_close_connection: bool = False
        try:
            if self.is_open_connection:
                self.con.close()
                print("Database connection closed successfully. ")
                is_close_connection = True

        except Exception as ex:
            print(ex)
            is_close_connection = False

        return is_close_connection


if __name__ == '__main__': 
    input_exit = "Exit"
    sql_lite_instance = SQlLiteShell()

    sql_lite_instance.open_connection()

    while True: 
        print("SQLLite Menu: ")
        print("1. SQL Command : ")
        print("2. Execute Command: ")
        print("3. Display output ")
        print("4. Exit")
        line = input()
        match line:
            case "1": sql_lite_instance.accept_command_line_input()
            case "2": sql_lite_instance.exec_sql_statement()
            case "3": sql_lite_instance.display_sql_output()
            case "4": line = "Exit"

        if line == input_exit: 
            sql_lite_instance.close_connection()
            break


   

   