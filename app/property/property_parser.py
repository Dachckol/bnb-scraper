
from .property_data import PropertyData
from app.exceptions import ParsingException

__all__ = ['PropertyParser']

class PropertyParser(object):

    @classmethod
    def parse(cls, string):
        name = cls.__get_name(string)
        property_type = cls.__get_property_type(string)
        no_of_bedrooms = cls.__get_no_of_bedrooms(string)
        no_of_bathrooms = cls.__get_no_of_bathrooms(string)
        anemities = cls.__get_anemities(string)
        return PropertyData(
            name,
            property_type,
            no_of_bedrooms,
            no_of_bathrooms,
            anemities
        )

    @classmethod
    def __get_name(cls, string):
        return 'name'

    @classmethod
    def __get_property_type(cls, string):
        pass

    @classmethod
    def __get_no_of_bedrooms(cls, string):
        label_index = string.find(' bed')
        if label_index == -1:
            raise ParsingException('Failed to find bedroom number')
        number = int(string[label_index-1])
        return int(number)

    @classmethod
    def __get_no_of_bathrooms(cls, string):
        label_index = string.find(' bath')
        if label_index == -1:
            raise ParsingException('Failed to find bathroom number')
        number = int(string[label_index-1])
        return int(number)

    @classmethod
    def __get_anemities(cls, string):
        pass

