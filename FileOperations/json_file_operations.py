import json


class JsonFileOperations:
    ### Class for Json file operations ###

    def load_json_data(self, file_name: str) -> str:
        ### Load json data method ###
        # Added try..catch block to capture an exception if any.

        load_json_result: str
        try:
            with open(file_name, encoding="UTF-8") as file_handle:
                load_json_result = json.load(file_handle)

        except FileNotFoundError as load_json_file_not_found_error:
            load_json_result =  load_json_file_not_found_error.__str__()
        return load_json_result

   
    def update_json_file(self, file_name: str,  data: str | bytes | bytearray) -> str:
        ### Updating Json file with given data ###
        update_json_result: str
        try:
            # File seems opening in write mode but data is not updating and throwing an error
            with open(file_name, "w", encoding="UTF-8") as file_handle:
                # This statement is running but file is not getting updated as expected.
                json.dump(data, file_handle, sort_keys=True, indent=4)
                update_json_result = "File updated"
        except FileNotFoundError as update_json_file_not_found_err:
            update_json_result = update_json_file_not_found_err.__str__()
        return update_json_result

    def repeated_names_json(self, data: str | bytes | bytearray) -> str:
        ### Repeated names json method ###
        loaded_json: str = json.loads(data)
        return loaded_json

if __name__ == '__main__':
    json_file_ops_instance = JsonFileOperations()
    json_file_name: str = "Data\\sample.json"
    print("JSON Data: ", json_file_ops_instance.load_json_data(json_file_name))

    data_to_write = '{ "name": "dummy", "age": 28, gender": "Male" }'
    txt_file_name: str = "Data\\json_to_write.txt"
    result: str = json_file_ops_instance.update_json_file(
        txt_file_name, data_to_write)
    print("JSON File update :", result)

    weird_json = '{ "x": 1, "x": 2, "x": 3  }'

    print("Weird JSON  : ", weird_json)
    print("Processed weird json : ",
          json_file_ops_instance.repeated_names_json(weird_json))

# Command line options to echo json
# echo '{1.2:3.4}' | python -m json.tool
# python -m json.tool "[json_file_path]"
