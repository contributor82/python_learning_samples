"""Module for File operations """
import glob
import codecs
import os
import struct
import shutil


class FileOperations:
    """File operations class """
    file_handle: object | None
    file_data: str | bytes # type: ignore

    def open_file(self, file_name : str, opening_mode: str) -> None:
        """ Open file method """
        # Opening a file explicitely for reading purpose
        try:
            with open(file_name, opening_mode, encoding="UTF-8") as handle:
                self.file_handle = handle
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)


    def close_file(self) -> None:
        """Closing file explicitely"""
        if not self.file_handle is None and self.file_handle.closed is False: # type: ignore
            self.file_handle.close() # type: ignore


    def read_file(self, file_name: str) -> None:
        """ Reading file data method """
        try:
            # with will take care of file to be closed after use.
            with open(file_name,'r', encoding="UTF-8") as self.file_handle:
                self.file_data = self.file_handle.read() # type: ignore
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)


    def read_binarydata_from_file(self, file_name: str) -> None:
        """ Reading binary data from file method """
        try:
            with open(file_name,'rb') as handle:
                self.file_data: bytes = handle.read(8)
                binary_data_one , binary_data_two, binary_data_three = struct.unpack(">hhl",
                                                                                     self.file_data)
                print("Binary data from file: ", binary_data_one, binary_data_two,
                      binary_data_three)
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)


    def write_file(self, file_name: str) -> None:
        """ Write operation currently causing an error. DO NOT USE. """
        # # w+ Opens a disk file for updating(reading and writing)
        try:
            with open(file_name,'w+', encoding='utf-8') as handle:
                self.file_handle = handle
                data: str = "This is a file write operation."
                self.file_handle.write(data)
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)


    def append_file(self, file_name: str) -> None:
        """Appending file contents method"""
        # # a Opens a file to append the contents to the end of the file.
        try:
            with open(file_name,'a+', encoding='utf-8') as self.file_handle:
                data: str = "Appending file contents. "
                self.file_handle.write(data)
                self.close_file()
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)


    def delete_file(self, file_name: str) -> None:
        """ Deleting file method """
        try:
            if os.access(file_name, os.F_OK):
                os.remove(file_name)
                print(file_name, " deleted successfully. ")
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)
        except FileExistsError as file_exists_error:
            print(file_exists_error)
        except OSError as os_error:
            print(os_error)


    def rename_file(self, oldfile_name : str, newfile_name: str) -> None:
        """ Renaming file method - causing Access is denied error DO NOT USE """
        try:
            if os.access(oldfile_name, os.F_OK):
                os.rename(oldfile_name, newfile_name)
                print("File has been renamed successfully. ")
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)
        except OSError as os_error:
            print(os_error)


    def file_copy(self, source_file_name : str, dest_file_name: str) -> None:
        """ File copy method """
        try:
            result: str = shutil.copyfile(source_file_name, dest_file_name)
            print(result)
        except shutil.SameFileError as same_file_error:
            print(same_file_error)
        except shutil.SpecialFileError as special_file_error:
            print(special_file_error)


    def file_wildcards(self) -> None:
        """ File wild cards method """
        files_list: list[str] = glob.glob('*.py')
        print(files_list)


    def display_file_data(self) -> str | bytes | None:
        """ Returning retrieved file data method """
        return self.file_data


    def convert_between_file_encoding(self, file_name: str) -> None:
        """ Convert between file encoding method """
        # Causing "can't concat str to bytes error even though
        # reading data & called bytes for the conversion. " DO NOT USE
        # file_handle causing conversion error TextIOWrapper to codecs._Stream
        try:
            with open(file_name, 'r', encoding="latin-1" ) as self.file_handle:
                newfile_handle =  codecs.StreamRecoder(self.file_handle, # type: ignore
                                                       codecs.getencoder('utf-8'),
                                                       codecs.getdecoder('utf-8'),
                                                       codecs.getreader('latin-1'),
                                                       codecs.getwriter('latin-1'),
                                                       errors="strict")
                data = newfile_handle.read().decode(
                    encoding="iso-8859-1").encode(
                    encoding="utf-8")
                print(data)

        except OSError as os_error:
            print(os_error)


    # def convert_latin_data(self):
    #     try:
    #         bytesObj = bytes("¿Cómo estás?", encoding="latin-1")
    #         result = codecs.decode(bytesObj, encoding="iso-8859-1",errors="strict").encode(
    # encoding="utf-8")
    #         bytesObjNew = bytes(result.__str__(),encoding="utf-8")
    #         result1 = codecs.decode(bytesObjNew,encoding="latin-1")

    #         print(result, " ", result1)
    #     except Exception as ex:
    #         print(ex)

if __name__ == '__main__':
    try:
        # Creating file operation class object.
        file_instance = FileOperations()

        binary_data_file_name: str = "C:\\Data\\binarydata.txt"
        file_instance.read_binarydata_from_file(binary_data_file_name)

        old_file_name: str = "C:\\Data\\tempfile.txt"
        new_file_name: str = "C:\\Data\\tempfile_one.txt"

        file_instance.rename_file(old_file_name, new_file_name )

        latin_data_file_name: str = 'C:\\Data\\latindata.txt'
        # file_instance.convert_between_file_encoding(latin_data_file_name)
        # file_instance.convert_latin_data()

        file_instance.display_file_data()

        txt_file_name: str = 'C:\\Data\\textfile.txt'
        # Calling file wildcards method
        file_instance.file_wildcards()

        # Calling file read method
        file_instance.read_file(txt_file_name)

        # Calling file data and storing returned data in a variable.
        file_contents: str | bytes | None = file_instance.display_file_data()

        # Printing returned data.
        print("Reading current file data: ", file_contents)

        # Calling write file operation
        file_instance.write_file(txt_file_name)

        # Calling read file after write operation
        file_instance.read_file(txt_file_name)

        # Calling file display data
        file_contents = file_instance.display_file_data()

        # Printing file contents after reading.
        print("Reading after writing file contents: ", file_contents)

        # Calling file append
        file_instance.append_file(txt_file_name)

        # Calling read file after append  operation
        file_instance.read_file(txt_file_name)

        # Calling file display data
        file_contents  = file_instance.display_file_data()

        # Printing file contents after reading.
        print("Reading after appending file contents: ", file_contents)

        # Calling file close explicitely if file has not been closed.
        file_instance.close_file()

        source_file : str = "C:\\Data\\sourcefile.txt"
        dest_file : str = "C:\\Data\\destinationfile.txt"
        file_instance.file_copy(source_file,  dest_file)

        del_file_name: str = "C:\\Data\\delfile.txt"
        file_instance.delete_file(del_file_name)
    except IOError as io_error:
        print(io_error)
