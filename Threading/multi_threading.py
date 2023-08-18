"""Module for multi threading in python"""

import threading
import zipfile
import time

class AsyncZip(threading.Thread):
    """Async zip class"""

    in_file: str
    out_file: str
    extraction_path: str

    def __init__(self, in_file : str, out_file: str, extract_to: str) -> None:
        """Initializing thread, in & out file """
        threading.Thread.__init__(self)
        self.in_file = in_file
        self.out_file = out_file
        self.extraction_path = extract_to

    def thread_task(self, task_name : str, num_range: int) -> None:
        """ Printing thread task method """
        for i in range(num_range):
            print(task_name, i)

    def exec_thread(self, num_range: int) -> None:
        """Executing thread method """
        for i in range(num_range):
            thread = threading.Thread(target=self.thread_task, args=(str(i), i))
            thread.start()
        time.sleep(10)

    def run(self) -> None:
        try:
            # checking given file is a zip file
            if zipfile.is_zipfile(self.out_file):
                print(self.out_file, " is a zipfile")

            # Reading files from zip file.
            with zipfile.ZipFile(self.out_file, 'r',zipfile.ZIP_DEFLATED) as zip_file_instance:

                # Prints file name list present in archive folder.
                print("Files present in zip file: ", zip_file_instance.namelist())

                # Zip File extraction
                for file_zip_info in zip_file_instance.filelist:
                    zip_file_instance.extract(file_zip_info, path=self.extraction_path)

                print('Finished background zip of: ', self.in_file)
        except OSError as os_error:
            print("Operating System Error: ", os_error)
        except zipfile.error as zip_file_error:
            print("Exception: ", zip_file_error.args[0])


if __name__ == '__main__':
    try:
        txt_file_path: str = "C:\\Data\\mydata.txt"
        zip_file_path: str = "C:\\Data\\mydata_archive.zip"
        zip_files_extraction_path : str = "\\Data\\mydata_archive"
        background = AsyncZip(txt_file_path, zip_file_path, zip_files_extraction_path)
        background.start()
        print(" The main program continues to run in foreground. ")
        background.join()
        print('Main program waited until the background was done. ')
    except threading.ThreadError as thread_error:
        print(thread_error)
    except TypeError as type_error:
        print(type_error)
