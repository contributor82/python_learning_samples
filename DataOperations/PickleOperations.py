# Using pickle for object serialization and deserialization

import pickle

class SampleClass: 
    sampleStr:str = 'Sample class'

class ObjectSerializeDeserialize: 
    pickledBytes: bytes
    unpickledObj : any

    def serialize_object(self, objToBeSerialized: SampleClass) -> None: 
        self.pickledBytes =  pickle.dumps(objToBeSerialized)

    def pickle_data_to_file(self, data: any, fileName: str) -> None: 
       with open(fileName, 'wb') as fileHandle: 
          pickle.dump(data, fileHandle, pickle.HIGHEST_PROTOCOL)  

    def unpickled_data_from_file(self, fileName: str) -> None: 
       with open(fileName, 'rb') as fileHandle: 
          data = pickle.loads(fileHandle)

          print("Unpickled file data : ", data)

    def display_serialized_object_stream(self) -> None: 
        print ("Serialized object Stream using pickle : ", self.pickledBytes)


    def deserialize_object(self) ->  None: 
        self.unpickledObj = pickle.loads(self.pickledBytes)

    
if __name__ == '__main__': 
   osdInstance =  ObjectSerializeDeserialize()
   osdInstance.serialize_object(SampleClass)
   osdInstance.display_serialized_object_stream()

   osdInstance.deserialize_object()
   if osdInstance.unpickledObj is SampleClass : 
    print(osdInstance.unpickledObj.sampleStr)

    dataToBePickled = {
           'NumSeries': [1, 2.0, 3+4j],
           'ByteSeries': ("character string", b"byte string"),
           'BooleanSeries': {None, True, False}
    }
    osdInstance.pickle_data_to_file(dataToBePickled, "C:\\Data\\Serial.pickle")    

    osdInstance.unpickled_data_from_file("C:\\Data\\Serial.pickle")    

