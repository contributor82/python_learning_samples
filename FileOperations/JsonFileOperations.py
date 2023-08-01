# JSON File loading
import json

class JsonFileOperations: 

    # Loading Json file
    def load_json_data(self) -> any :
        # Added try..catch block to capture an exception if any.
        try:
            with open("Data\\sample.json") as fileHandle: 
                data = json.load(fileHandle)
                return data
        except Exception as ex:
            return ex.__str__()
    
    # Updating Json file with given data
    def update_json_file(self, data: str | bytes | bytearray) -> str: 
        try:
            with open("Data\\json_to_write.txt","w", encoding="UTF-8") as fileHandle: # File seems opening in write mode but data is not updating and throwing an error 
                json.dump(data,fileHandle, sort_keys=True,indent=4)  # This statement is running but file is not getting updated as expected. 
                return "File updated"
        except Exception as ex:
            return ex.__str__()
        
    def repeated_names_json(self, data: str | bytes | bytearray) -> any: 
        loadedJson = json.loads(data)
        return loadedJson
    
    
    def temp_fun(self): 
        x = [1, 'simple', 'list']
        json.dumps(x)
        

if __name__ == '__main__': 
    dataLoadInstance = JsonFileOperations()
    print("JSON Data: ", dataLoadInstance.load_json_data()) 

    dataToWrite = '{ "name": "dummy", "age": 28, gender": "Male" }'
    
    result = dataLoadInstance.update_json_file(dataToWrite)
    print("JSON File update :", result)
    
    dataLoadInstance.temp_fun()

    x = [1, 'simple', 'list']
    json.dumps(x)

    weird_json = '{ "x": 1, "x": 2, "x": 3  }'

    print("Weird JSON  : ", weird_json)
    print("Processed weird json : ",  dataLoadInstance.repeated_names_json(weird_json))

        
# Command line options to echo json
# echo '{1.2:3.4}' | python -m json.tool
# python -m json.tool "[json_file_path]"