
# Multi threading in python

import threading, zipfile
import time

# async zip class
class AsyncZip(threading.Thread): 
    in_file: str 
    out_file: str

    def __init__(self, in_file : str, out_file: str) -> None:
        threading.Thread.__init__(self)
        self.in_file = in_file
        self.out_file = out_file
    
    def thread_task(self, name : str, num: int) -> None: 
        for i in range(num): 
            print(name, i)

    def exec_thread(self, num: int) -> None: 
        for i in range(num): 
            T = threading.Thread(target=self.thread_task, args=(str(i), i))
            T.start()
        
        time.sleep(10)
    
    def run(self) -> None: 
        try: 
            # checking given file is a zip file 
            if zipfile.is_zipfile(self.out_file): 
                print(self.out_file, " is a zipfile")
            
            # Reading files from zip file.
            zip_file_instance = zipfile.ZipFile(self.out_file, 'r',zipfile.ZIP_DEFLATED)

            # Prints file name list present in archive folder. 
            print("Files present in zip file: ", zip_file_instance.namelist())
            
            # Zip File extraction
            for file_zip_info in zip_file_instance.filelist: 
                zip_file_instance.extract(file_zip_info, path="\\Data\\mydata_archive")
            
            print('Finished background zip of: ', self.in_file)
        except OSError as osError: 
            print("Operating System Error: ", osError)
        except Exception as ex:
            print("Exception: ", ex)
    

if __name__ == '__main__': 
    background = AsyncZip("C:\\Data\\mydata.txt", "C:\\Data\\mydata_archive.zip")
    background.start()
    print(" The main program continues to run in foreground. ")

    background.join()
    print('Main program waited until the background was done. ')

