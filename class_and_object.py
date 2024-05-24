class city:

    # class attribute
    attr1 = "Italy"
    attr2 = "Turkey"

    # Instance attribute
    def __init__(self, place):
        self.place = place

# Object instantiation
italy = city("Rome")
turkey = city("Cappadocia")

# Accessing class attributes
print("Rome is in {}".format(italy.__class__.attr1))
print("Cappadocia  is in  {}".format(turkey.__class__.attr2))

# Accessing instance attributes
print(" I want to go {}".format(italy.place))
print(" I will go to {}".format(turkey.place),"which is in {}".format(turkey.__class__.attr2))
