# Here Default class has been created accepting dictionary Key Value pair and returns a pair.
# String formmat_mpa further grabs key and maps with associated value.  

class Default(dict):
    def __missing__(self, key):
        return key
    
str = "{name} is from {country}"

print(str.format_map(Default(name="John", country="USA")))

print(Default(one=1))
