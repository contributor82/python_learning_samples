import csv

class CSVFileOperations: 

    def read_csv(self, fileName: str) -> None: 
        try: 
            with open(fileName, newline='') as csvFile: 
                csvReader = csv.reader(csvFile, delimiter=' ', quotechar='|')
                for row in csvReader: 
                    print (row)
        except Exception as ex:
            print(ex)

    def read_csv_to_dict(self, fileName: str) -> None: 
        try: 
            with open(fileName, newline='') as csvFile: 
                csvDictReader = csv.DictReader(csvFile)
                for row in csvDictReader: 
                    print (row['baby_name'], row['baby_age'], row['baby_weight_pound'])
        except Exception as ex: 
            print(ex)

    def write_csv(self, fileName: str, fruitsData : list[list[str | int]]) -> None: 
        try: 
            with open(fileName, "a", newline='') as csvFile: 
                csvWriter = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

                for fruitsRow in fruitsData: 
                    csvWriter.writerow(fruitsRow)
        except Exception as ex: 
            print(ex)


if __name__ == '__main__': 
    csvFileOpsInstance = CSVFileOperations()

    csvFileName: str = "C:\\Data\\Fruits.csv"
    csvFileOpsInstance.read_csv(csvFileName)

    fruits_data = [["Strawberry", 5, 5], ["Blueberry", 5, 10] ]
    csvFileOpsInstance.write_csv(csvFileName, fruits_data)

    csvFileOpsInstance.read_csv(csvFileName)

    csvFileName = "C:\\Data\\Babynames.csv"
    csvFileOpsInstance.read_csv_to_dict(csvFileName)