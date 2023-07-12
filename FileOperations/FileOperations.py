import glob
import codecs

class FileOperations: 
    fileHandle = None
    fileData = None

    # Opening a file explicitely for reading purpose
    def open_file(self, openingMode): 
        try:
            self.fileHandle = open('Data\\textfile.txt', openingMode)
        except OSError as osError: 
            print(osError)
        except Exception as ex: 
            print(ex)

    # Closing file explicitely
    def close_file(self): 
        if self.fileHandle != None and self.fileHandle.closed == False : 
            self.fileHandle.close()
    
    # Reading file data
    def read_file(self): 
        try: 

            # Using with to open file for reading and the file is closed immediately. 
            with open('Data\\textfile.txt','r') as self.fileHandle:
                self.fileData = self.fileHandle.read()
        except OSError as osError: 
            print(osError)
        except Exception as ex: 
            print(ex)
        

    # Write operation currently causing an error. DO NOT USE.
    def write_file(self):
        # # w+ Opens a disk file for updating(reading and writing)
        try: 
            self.fileHandle = open('Data\\textfile.txt','w+', encoding='utf-8')
            data = "This is a file write operation. textfile is getting new string contents. "
            self.fileHandle.write(data)
        except OSError as osError: 
            print(osError)
        except Exception as ex: 
            print(ex)


    def append_file(self):
        # # a Opens a file to append the contents to the end of the file.  
        try: 
            self.fileHandle = open('Data\\textfile.txt','a+', encoding='utf-8')
            data = "Appending file contents. "
            self.fileHandle.write(data) 
            self.close_file()
        except OSError as osError: 
            print(osError)
        except Exception as ex: 
            print(ex)


    # Listing files present when file extension is given.
    def  file_wildcards(self): 
        filesList = glob.glob('*.py')
        print(filesList)

    # Returning data for display purpose
    def display_file_data(self):
        return self.fileData   

    # Causing "can't concat str to bytes error even though reading data & called bytes for the conversion. " DO NOT USE
    def convert_between_file_encoding(self, fileName): 
        try:
            with open(fileName, 'r', encoding="latin-1" ) as self.fileHandle: 
                 
                newFileHandle =  codecs.StreamRecoder(self.fileHandle, codecs.getencoder('utf-8'), codecs.getdecoder('utf-8'), 
                                                       codecs.getreader('latin-1'), codecs.getwriter('latin-1'), errors="strict")
                
                self.fileData = newFileHandle.read().__bytes__()

        except OSError as osError: 
            print(osError)
        except Exception as ex: 
            print(ex)

    # Causing an error - 'utf-8' codec can't decode byte 0xf3 in position 1: invalid continuation byte DO NOT USE
    def convert_latin_data(self): 
        try:
            bytesObj = bytes("¿Cómo estás?", encoding="latin-1")
            result = codecs.decode(bytesObj, encoding="utf-8",errors="strict")
            print(result)
        except Exception as ex: 
            print(ex)

# Creating file operation class object. 
fileObj = FileOperations()

# fileObj.convert_between_file_encoding('Data\\latindata.txt')
fileObj.convert_latin_data()

fileObj.display_file_data()

# Calling file wildcards method
fileObj.file_wildcards()

# Calling file read method 
fileObj.read_file()

# Calling file data and storing returned data in a variable. 
data = fileObj.display_file_data()

# Printing returned data. 
print("Reading current file data: ", data)

# Calling write file operation
fileObj.write_file()

# Calling read file after write operation
fileObj.read_file()

# Calling file display data
data = fileObj.display_file_data()

# Printing file contents after reading. 
print("Reading after writing file contents: ", data)

# Calling file append
fileObj.append_file()

# Calling read file after append  operation
fileObj.read_file()

# Calling file display data
data = fileObj.display_file_data()

# Printing file contents after reading. 
print("Reading after appending file contents: ", data)

# Calling file close explicitely if file has not been closed. 
fileObj.close_file()


