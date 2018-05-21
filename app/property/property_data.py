
__all__ = [] #data object should only really by returned by the parser

class PropertyData(object):

    def __init__(self,
            name,
            property_type,
            no_of_bedrooms,
            no_of_bathrooms,
            anemities
            ):
        self.name = name
        self.property_type = property_type
        self.no_of_bedrooms = no_of_bedrooms
        self.no_of_bathrooms = no_of_bathrooms
        self.anemities = anemities

    def anemities_contains(self, *args):
        conditions = [a in self.anemities for a in args]
        return all(conditions)
