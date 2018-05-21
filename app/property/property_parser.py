from bs4 import BeautifulSoup

from .property_data import PropertyData
from app.exceptions import ParsingException

__all__ = ['PropertyParser']

class PropertyParser(object):

    @classmethod
    def parse(cls, string):
        soup = BeautifulSoup(string, 'html.parser')
        name = cls.__get_name(soup)
        property_type = cls.__get_property_type(soup)
        no_of_bedrooms = cls.__get_no_of_bedrooms(string)
        no_of_bathrooms = cls.__get_no_of_bathrooms(string)
        anemities = cls.__get_anemities(soup)
        return PropertyData(
            name,
            property_type,
            no_of_bedrooms,
            no_of_bathrooms,
            anemities
        )

    @classmethod
    def __get_name(cls, soup):
        h1_elements = soup.find_all('h1')

        try:
            for element in h1_elements:
                conditions = (
                    element.parent.name == 'span',
                    element.parent.parent.name == 'span',
                    element.parent.parent['dir'] == 'ltr',
                    element.parent.parent.parent['itemprop'] == 'name'
                )

                if all(conditions):
                    return element.text
        except Exception as e:
            raise ParsingException('{}:{}'.format(e.__class__.__name__,e))
        raise ParsingException('Failed to find property name')

    @classmethod
    def __get_property_type(cls, soup):
        span_elements = soup.find_all('span')

        try:
            for element in span_elements:
                conditions = (
                    element.has_attr('style'),
                    element.parent.name == 'span',
                    element.parent.parent.name == 'span',
                    element.parent.parent.parent.name == 'div',
                    element.parent.parent.parent.parent.name == 'a',
                    element.parent.parent.parent.parent.has_attr('class')
                )

                if all(conditions):
                    return element.text
        except Exception as e:
            raise ParsingException('{}:{}'.format(e.__class__.__name__,e))
        raise ParsingException('Failed to find property name')

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
    def __get_anemities(cls, soup):
        pass

