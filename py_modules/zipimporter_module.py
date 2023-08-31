"""Module for zip importer"""
import zipimport


class ZipImporterModule:
    zip_import_instance: zipimport.zipimporter

    def __init__(self, zip_file_path: str) -> None:
        """Initializing zip importer """
        self.zip_import_instance =  zipimport.zipimporter(zip_file_path)

    def import_zip(self) -> None:
        """Import zup file """
        try:
            print(self.zip_import_instance.__dict__)
        except zipimport.ZipImportError as zip_import_error:
            print(zip_import_error)

    def get_zip_file_data(self, file_path:str) -> None:
        """ Get zip file """
        try:
           zip_file_data: bytes = self.zip_import_instance.get_data(file_path)
           print(zip_file_data)
        except FileNotFoundError as zip_file_not_found_error:
            print(zip_file_not_found_error)
        except zipimport.ZipImportError as get_zip_import_error:
            print(get_zip_import_error)
        except OSError as get_zip_os_error:
            print(get_zip_os_error)

if __name__ == '__main__':
    zip_importer_mod_instance = ZipImporterModule('C:\\Data\\mydata_archive.zip')
    zip_importer_mod_instance.import_zip()
    zip_importer_mod_instance.get_zip_file_data('C:\\Data\\change_file_owner.txt')
