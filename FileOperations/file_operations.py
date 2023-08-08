import glob
import codecs
import os
import struct
import shutil


class FileOperations: 
    file_handle: object 
    file_data: str | bytes 

    # Opening a file explicitely for reading purpose
    def open_file(self, file_name : str, opening_mode: str) -> None: 
        try:
            self.file_handle = open(file_name, opening_mode)
        except OSError as os_error: 
            print(os_error)
        except Exception as ex: 
            print(ex)

    # Closing file explicitely
    def close_file(self) -> None: 
        if not self.file_handle is None and self.file_handle.closed is False: 
            self.file_handle.close()
    
    # Reading file data
    def read_file(self, file_name: str) -> None: 
        try: 
            # with will take care of file to be closed after use. 
            with open(file_name,'r') as handle:
                self.file_data = handle.read()
        except OSError as os_error: 
            print(os_error)
        except Exception as ex: 
            print(ex)
    
    # Reading binary data from file
    def read_binarydata_from_file(self, file_name: str) -> None: 
        try: 
            with open(file_name,'rb') as handle:
                self.file_data: bytes = handle.read(8)
                binary_data_one , binary_data_two, binary_data_three = struct.unpack(">hhl", self.file_data)
                print("Binary data from file: ", binary_data_one, binary_data_two, binary_data_three)
        except OSError as os_error: 
            print(os_error)
        except Exception as ex: 
            print(ex)

    # Write operation currently causing an error. DO NOT USE.
    def write_file(self, file_name: str) -> None:
        # # w+ Opens a disk file for updating(reading and writing)
        try: 
            self.file_handle = open(file_name,'w+', encoding='utf-8')
            data: str = "This is a file write operation. textfile is getting new string contents. "
            self.file_handle.write(data)
        except OSError as os_error: 
            print(os_error)
        except Exception as ex: 
            print(ex)

    # Appending file contents
    def append_file(self, file_name: str) -> None:
        # # a Opens a file to append the contents to the end of the file.  
        try: 
            self.file_handle = open(file_name,'a+', encoding='utf-8')
            data: str = "Appending file contents. "
            self.file_handle.write(data) 
            self.close_file()
        except OSError as os_error: 
            print(os_error)
        except Exception as ex: 
            print(ex)

    # Deleting file
    def delete_file(self, file_name: str) -> None: 
        try:
            if os.access(file_name, os.F_OK): 
                os.remove(file_name)
                print(file_name, " deleted successfully. ")
        except FileNotFoundError as file_not_found_error: 
            print(file_not_found_error)
        except OSError as os_error: 
            print(os_error)
        except Exception as ex: 
            print(ex)

    # Renaming file - causing Access is denied error DO NOT USE
    def rename_file(self, oldfile_name : str, newfile_name: str) -> None: 
        try:
            if os.access(oldfile_name, os.F_OK): 
                os.rename(oldfile_name, newfile_name)
                print("File has been renamed successfully. ")
        except FileNotFoundError as file_not_found_error: 
            print(file_not_found_error)
        except OSError as os_error: 
            print(os_error)
        except Exception as ex: 
            print(ex)
    
    def file_copy(self, source_file_name : str, dest_file_name: str) -> None:
        try:
            result: str = shutil.copyfile(source_file_name, dest_file_name)
            print(result)
        except Exception as ex: 
            print(ex)

    # Listing files present when file extension is given.
    def file_wildcards(self) -> None: 
        filesList: list[str] = glob.glob('*.py')
        print(filesList)

    # Returning data for display purpose
    def display_file_data(self) -> str | bytes | None:
        return self.file_data   

    # Causing "can't concat str to bytes error even though reading data & called bytes for the conversion. " DO NOT USE
    def convert_between_file_encoding(self, file_name: str) -> None: 
        try:
            with open(file_name, 'r', encoding="latin-1" ) as self.file_handle: 
                
                newfile_handle =  codecs.StreamRecoder(self.file_handle, codecs.getencoder('utf-8'), codecs.getdecoder('utf-8'), 
                                                       codecs.getreader('latin-1'), codecs.getwriter('latin-1'), errors="strict")
                data = newfile_handle.read().__bytes__().decode(encoding="iso-8859-1").encode(encoding="utf-8")
                print(data)

        except OSError as os_error: 
            print(os_error)
        except Exception as ex: 
            print(ex)

    # def convert_latin_data(self): 
    #     try:
    #         bytesObj = bytes("¿Cómo estás?", encoding="latin-1")
    #         result = codecs.decode(bytesObj, encoding="iso-8859-1",errors="strict").encode(encoding="utf-8")
    #         bytesObjNew = bytes(result.__str__(),encoding="utf-8")
    #         result1 = codecs.decode(bytesObjNew,encoding="latin-1")
            
    #         print(result, " ", result1)
    #     except Exception as ex: 
    #         print(ex)

if __name__ == '__main__': 
    # Creating file operation class object. 
    file_instance = FileOperations()

    binary_data_file_name: str = "C:\\Data\\binarydata.txt"
    file_instance.read_binarydata_from_file(binary_data_file_name)

    oldfile_name: str = "C:\\Data\\tempfile.txt"
    newfile_name: str = "C:\\Data\\tempfile_one.txt"

    file_instance.rename_file(oldfile_name,newfile_name )

    latin_data_file_name: str = 'C:\\Data\\latindata.txt'
    # file_instance.convert_between_file_encoding(latin_data_file_name)
    # file_instance.convert_latin_data()

    file_instance.display_file_data()

    file_name: str = 'C:\\Data\\textfile.txt'
    # Calling file wildcards method
    file_instance.file_wildcards()

    # Calling file read method 
    file_instance.read_file(file_name)

    # Calling file data and storing returned data in a variable. 
    data: str | bytes | None = file_instance.display_file_data()

    # Printing returned data. 
    print("Reading current file data: ", data)

    # Calling write file operation
    file_instance.write_file(file_name)

    # Calling read file after write operation
    file_instance.read_file(file_name)

    # Calling file display data
    data = file_instance.display_file_data()

    # Printing file contents after reading. 
    print("Reading after writing file contents: ", data)

    # Calling file append
    file_instance.append_file(file_name)

    # Calling read file after append  operation
    file_instance.read_file(file_name)

    # Calling file display data
    data  = file_instance.display_file_data()

    # Printing file contents after reading. 
    print("Reading after appending file contents: ", data)

    # Calling file close explicitely if file has not been closed. 
    file_instance.close_file()

    source_file_name : str = "C:\\Data\\sourcefile.txt"
    dest_file_name : str = "C:\\Data\\destinationfile.txt"
    file_instance.file_copy(source_file_name,  dest_file_name)

    del_file_name: str = "C:\\Data\\delfile.txt"
    file_instance.delete_file(del_file_name)


