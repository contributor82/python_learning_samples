import csv

class CSVFileOperations: 

    # Reading CSV file and printing its row contents
    def read_csv(self, file_name: str) -> None: 
        try: 
            with open(file_name) as csv_file: 
                csv_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
                for row in csv_reader: 
                    print (row)
        except Exception as ex:
            print(ex)

    # Reading CSV file in a dictonary and printing contents 
    def read_csv_to_dict(self, file_name: str) -> None: 
        try: 
            with open(file_name) as csv_file: 
                csv_dict_reader = csv.DictReader(csv_file)
                for row in csv_dict_reader: 
                    print (row['baby_name'], row['baby_age'], row['baby_weight_pound'])
        except Exception as ex: 
            print(ex)

    # Writing CSV file contents
    def write_csv(self, file_name: str, fruits_data : list[list[str | int]]) -> None: 
        try: 
            with open(file_name, "a") as csv_file: 
                csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

                for fruits_row in fruits_data: 
                    csv_writer.writerow(fruits_row)
        except Exception as ex: 
            print(ex)


if __name__ == '__main__': 
    csv_file_ops_instance = CSVFileOperations()

    csv_file_name: str = "C:\\Data\\Fruits.csv"
    csv_file_ops_instance.read_csv(csv_file_name)

    fruits_data: list[list[str | int]] = [["Strawberry", 5, 5], ["Blueberry", 5, 10] ]
    csv_file_ops_instance.write_csv(csv_file_name, fruits_data)

    csv_file_ops_instance.read_csv(csv_file_name)

    csv_file_name = "C:\\Data\\Babynames.csv"
    csv_file_ops_instance.read_csv_to_dict(csv_file_name)