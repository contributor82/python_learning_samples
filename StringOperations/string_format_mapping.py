# Here Default class has been created accepting dictionary Key Value pair and returns a pair.
# String formmat_mpa further grabs key and maps with associated value.  

class Default(dict):
    def __missing__(self, key: object):
        return key
    
inputStr = "{name} is from {country}"

print(inputStr.format_map(Default(name="John", country="USA")))

print(Default(one=1))
