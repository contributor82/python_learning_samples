
# Multi threading in python

import threading, zipfile

# YET TO BE DONE - Threading seems working but file operations not completing as expected. 
class AsyncZip(threading.Thread): 
    infile = None
    outfile = None

    def __init__(self, inFile, outFile):
        threading.Thread.__init__(self)
        self.infile = inFile
        self.outfile = outFile
    
    def run(self): 
        try: 
            # checking given file is a zip file 
            if zipfile.is_zipfile(self.outfile): 
                print(self.outfile, " is a zipfile")
            
            # Reading files from zip file.
            zipFileObj = zipfile.ZipFile(self.outfile, 'r',zipfile.ZIP_DEFLATED)

            # Prints file name list present in archive folder. 
            print("Files present in zip file: ", zipFileObj.namelist())
            
            # Gives bad file descriptor error even though file is present at the given path. 
            for fileZipInfo in zipFileObj.filelist: 
                zipFileObj.extract(fileZipInfo, path="Data\\")
            
            zipFileObj.extract(self.infile)
            
            print('Finished background zip of: ', self.infile)
        except Exception as ex:
            print("Exception: ", ex)


background = AsyncZip("Data\\mydata.txt", "Data\\mydata_archive.zip")
background.start()
print(" The main program continues to run in foreground. ")

background.join()
print('Main program waited until the background was done. ')

