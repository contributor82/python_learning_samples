# JSON File loading
import json

class JsonFileOperations: 

    # Loading Json file
    def load_json_data(self):
        # Added try..catch block to capture an exception if any.
        try:
            with open("Data\\sample.json") as fileHandle: 
                data = json.load(fileHandle)
                return data
        except Exception as ex:
            return ex.__str__()
    
    # Updating Json file with given data
    def update_json_file(self): 
        try:
            with open("Data\\json_to_write.txt","w", encoding="UTF-8") as fileHandle: # File seems opening in write mode but data is not updating and throwing an error 
                dataToWrite =  {                                     # Error no. 9: Bad file descriptor. 
                                    'name': 'dummy',
                                    'age': 28,
                                    'gender': 'Male'
                               }
                json.dump(dataToWrite,fileHandle, sort_keys=True,indent=4)  # This statement is running but file is not getting updated as expected. 
                return "File updated"
        except Exception as ex:
            return ex.__str__()
    
    def temp_fun(self): 
        x = [1, 'simple', 'list']
        json.dumps(x)
        
dataLoadInstance = JsonFileOperations()
# print("JSON Data: ", dataLoadInstance.load_json_data()) 

# result = dataLoadInstance.update_json_file()
# print(result)

# dataLoadInstance.temp_fun()

x = [1, 'simple', 'list']
json.dumps(x)
        
