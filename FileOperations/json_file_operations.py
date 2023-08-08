import json


class JsonFileOperations:
    ### Class for Json file operations ###

    # Loading Json file
    def load_json_data(self, file_name: str) -> str:
        # Added try..catch block to capture an exception if any.

        result: str
        try:
            with open(file_name) as file_handle:
                result = json.load(file_handle)

        except Exception as ex:
            result = ex.__str__()
        return result

    # Updating Json file with given data
    def update_json_file(self, file_name: str,  data: str | bytes | bytearray) -> str:
        result: str
        try:
            # File seems opening in write mode but data is not updating and throwing an error
            with open(file_name, "w", encoding="UTF-8") as file_handle:
                # This statement is running but file is not getting updated as expected.
                json.dump(data, file_handle, sort_keys=True, indent=4)
                result = "File updated"
        except Exception as ex:
            result = ex.__str__()
        return result

    def repeated_names_json(self, data: str | bytes | bytearray) -> str:
        loadedJson = json.loads(data)
        return loadedJson

if __name__ == '__main__':
    json_file_ops_instance = JsonFileOperations()
    file_name: str = "Data\\sample.json"
    print("JSON Data: ", json_file_ops_instance.load_json_data(file_name))

    data_to_write = '{ "name": "dummy", "age": 28, gender": "Male" }'
    file_name = "Data\\json_to_write.txt"
    result: str = json_file_ops_instance.update_json_file(
        file_name, data_to_write)
    print("JSON File update :", result)

    weird_json = '{ "x": 1, "x": 2, "x": 3  }'

    print("Weird JSON  : ", weird_json)
    print("Processed weird json : ",
          json_file_ops_instance.repeated_names_json(weird_json))


# Command line options to echo json
# echo '{1.2:3.4}' | python -m json.tool
# python -m json.tool "[json_file_path]"
