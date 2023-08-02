
# Multi threading in python

import threading, zipfile
import time

# async zip class
class AsyncZip(threading.Thread): 
    infile: str 
    outfile: str

    def __init__(self, inFile : str, outFile: str) -> None:
        threading.Thread.__init__(self)
        self.infile = inFile
        self.outfile = outFile
    
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
            if zipfile.is_zipfile(self.outfile): 
                print(self.outfile, " is a zipfile")
            
            # Reading files from zip file.
            zipFileObj = zipfile.ZipFile(self.outfile, 'r',zipfile.ZIP_DEFLATED)

            # Prints file name list present in archive folder. 
            print("Files present in zip file: ", zipFileObj.namelist())
            
            # Zip File extraction
            for fileZipInfo in zipFileObj.filelist: 
                zipFileObj.extract(fileZipInfo, path="\\Data\\mydata_archive")
            
            print('Finished background zip of: ', self.infile)
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

