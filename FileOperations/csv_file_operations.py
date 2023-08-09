import csv


class CSVFileOperations:
    ### CSV file operations class ###

    def read_csv(self, file_name: str) -> None:
        ### read CSV file ###
        try:
            with open(file_name, encoding="UTF-8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
                for row in csv_reader:
                    print(row)
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)


    def read_csv_to_dict(self, file_name: str) -> None:
        ### Read csv file to dictionary ###
        try:
            with open(file_name, encoding='UTF-8') as csv_file:
                csv_dict_reader = csv.DictReader(csv_file)
                for row in csv_dict_reader:
                    print(row['baby_name'], row['baby_age'],
                          row['baby_weight_pound'])
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)


    def write_csv(self, file_name: str, fruits_data: list[list[str | int]]) -> None:
        ### Writing CSV file contents ###
        try:
            with open(file_name, "a", encoding='UTF-8') as csv_file:
                csv_writer = csv.writer(
                    csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

                for fruits_row in fruits_data:
                    csv_writer.writerow(fruits_row)
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)


if __name__ == '__main__':
    csv_file_ops_instance = CSVFileOperations()

    fruits_csv_file_name: str = "C:\\Data\\Fruits.csv"
    csv_file_ops_instance.read_csv(fruits_csv_file_name)

    sample_fruits_data: list[list[str | int]] = [
        ["Strawberry", 5, 5], ["Blueberry", 5, 10]]
    csv_file_ops_instance.write_csv(fruits_csv_file_name, sample_fruits_data)

    csv_file_ops_instance.read_csv(fruits_csv_file_name)

    babynames_csv_file_name: str = "C:\\Data\\Babynames.csv"
    csv_file_ops_instance.read_csv_to_dict(babynames_csv_file_name)
