"""Module for Pickle operations """
# Using pickle for object serialization and de-serialization
# The pickle module is not secure, only unpickle data you trust - Python docs.

import pickle

class SampleClass:
    """ Sample class """
    sample_str: str = 'Sample class'

class ObjectPickleUnpickle:
    """# Object serialize de-serialize using pickle """

    pickled_bytes: bytes
    unpickled_instance: pickle.Unpickler

    def pickle_object(self, instance_to_serialize: SampleClass) -> None:
        """ Function to serialize object using pickle """

        self.pickled_bytes = pickle.dumps(instance_to_serialize)

    def pickle_data_to_file(self, pickle_data: object, file_name: str) -> None:
        """ Function to pickle data to file """
        try:
            with open(file_name, 'wb') as file_handle:
                pickle.dump(pickle_data, file_handle, pickle.HIGHEST_PROTOCOL)
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)
        except pickle.PicklingError as pickling_error:
            print(pickling_error)

    def unpickled_data_from_file(self, file_name: str) -> None:
        """ Function to unpickle object """
        try:
            with open(file_name, 'rb') as file_handle:
                data = pickle.loads(file_handle) # type: ignore
                print("Unpickled file data : ", data)
        except IOError as io_error:
            print(io_error)
        except pickle.PickleError as pickle_error:
            print(pickle_error)

    def display_pickled_object_stream(self) -> None:
        """ Function to display pickle serialized object stream """
        print("Serialized object Stream using pickle : ", self.pickled_bytes)

    def unpickle_object(self) -> None:
        """ Function to display pickle serialized object stream """
        self.unpickled_instance = pickle.loads(self.pickled_bytes)


if __name__ == '__main__':
    opu_Instance = ObjectPickleUnpickle()
    opu_Instance.pickle_object(SampleClass)  # type: ignore
    opu_Instance.display_pickled_object_stream()

    opu_Instance.unpickle_object()
    if opu_Instance.unpickled_instance is SampleClass:
        print(opu_Instance.unpickled_instance.sample_str)

        data_to_pickle = {
            'NumSeries': [1, 2.0, 3+4j],
            'ByteSeries': ("character string", b"byte string"),
            'BooleanSeries': {None, True, False}
        }

        # Data can be of any format for pickling
        pickle_file_name: str = "C:\\Data\\Serial.pickle"
        opu_Instance.pickle_data_to_file(data_to_pickle, pickle_file_name)
        opu_Instance.unpickled_data_from_file(pickle_file_name)
