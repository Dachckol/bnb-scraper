import pytest

from unittest.mock import patch

from app.property import PropertyParser
from app.exceptions import ParsingException


class TestPropertyParser(object):

    @patch('app.property.PropertyParser._PropertyParser__get_name')
    @patch('app.property.PropertyParser._PropertyParser__get_property_type')
    @patch('app.property.PropertyParser._PropertyParser__get_no_of_bedrooms')
    @patch('app.property.PropertyParser._PropertyParser__get_no_of_bathrooms')
    @patch('app.property.PropertyParser._PropertyParser__get_anemities')
    def test_that_builds_property_model_correctly(
        self,
        get_anemities,
        get_no_of_bathrooms,
        get_no_of_bedrooms,
        get_property_type,
        get_name
    ):
        get_name.return_value = 'test name'
        get_property_type.return_value = 'test type'
        get_no_of_bedrooms.return_value = 2
        get_no_of_bathrooms.return_value = 3
        get_anemities.return_value = ['test1','test2']

        data = PropertyParser.parse("Some HTML")

        assert data.name == "test name"
        assert data.property_type == 'test type'
        assert data.no_of_bedrooms == 2
        assert data.no_of_bathrooms == 3
        assert len(data.anemities) == 2
        assert data.anemities_contains('test1','test2')


    def test_that_gets_correct_data_when_multi_numbers(self, page_html_multi_values):
        data = PropertyParser.parse(page_html_multi_values)

        assert data.name == 'Property Name'
        assert data.property_type == 'Property Type'
        assert data.no_of_bedrooms == 2
        assert data.no_of_bathrooms == 3
        #assert len(data.anemities) == 2
        #assert 'Anemity 1' in data.anemities
        #assert 'Anemity 2' in data.anemities

    def test_that_gets_correct_data_when_single_numbers(self, page_html_single_values):
        data = PropertyParser.parse(page_html_single_values)

        assert data.name == 'Property Name'
        assert data.property_type == 'Property Type'
        assert data.no_of_bedrooms == 1
        assert data.no_of_bathrooms == 2
        #assert len(data.anemities) == 2
        #assert 'Anemity 1' in data.anemities
        #assert 'Anemity 2' in data.anemities

    @patch('app.property.PropertyParser._PropertyParser__get_name')
    @patch('app.property.PropertyParser._PropertyParser__get_property_type')
    @patch('app.property.PropertyParser._PropertyParser__get_no_of_bathrooms')
    @patch('app.property.PropertyParser._PropertyParser__get_anemities')
    def test_that_throws_error_when_bedrooms_not_found(
        self,
        get_anemities,
        get_no_of_bathrooms,
        get_property_type,
        get_name
    ):
        get_name.return_value = 'test name'
        get_property_type.return_value = 'test type'
        get_no_of_bathrooms.return_value = 3
        get_anemities.return_value = ['test1','test2']

        with pytest.raises(ParsingException):
            PropertyParser.parse('html')

    @patch('app.property.PropertyParser._PropertyParser__get_name')
    @patch('app.property.PropertyParser._PropertyParser__get_property_type')
    @patch('app.property.PropertyParser._PropertyParser__get_no_of_bedrooms')
    @patch('app.property.PropertyParser._PropertyParser__get_anemities')
    def test_that_throws_error_when_bedrooms_not_found(
        self,
        get_anemities,
        get_no_of_bedrooms,
        get_property_type,
        get_name
    ):
        get_name.return_value = 'test name'
        get_property_type.return_value = 'test type'
        get_no_of_bedrooms.return_value = 3
        get_anemities.return_value = ['test1','test2']

        with pytest.raises(ParsingException):
            PropertyParser.parse('html')

    @patch('app.property.PropertyParser._PropertyParser__get_no_of_bedrooms')
    @patch('app.property.PropertyParser._PropertyParser__get_property_type')
    @patch('app.property.PropertyParser._PropertyParser__get_no_of_bathrooms')
    @patch('app.property.PropertyParser._PropertyParser__get_anemities')
    def test_that_throws_error_when_name_not_found(
        self,
        get_anemities,
        get_no_of_bathrooms,
        get_property_type,
        get_no_of_bedrooms
    ):
        get_no_of_bedrooms.return_value = 2
        get_property_type.return_value = 'test type'
        get_no_of_bathrooms.return_value = 3
        get_anemities.return_value = ['test1','test2']

        with pytest.raises(ParsingException):
            data=PropertyParser.parse('html')

    @patch('app.property.PropertyParser._PropertyParser__get_no_of_bedrooms')
    @patch('app.property.PropertyParser._PropertyParser__get_name')
    @patch('app.property.PropertyParser._PropertyParser__get_no_of_bathrooms')
    @patch('app.property.PropertyParser._PropertyParser__get_anemities')
    def test_that_throws_error_when_property_type_not_found(
        self,
        get_anemities,
        get_no_of_bathrooms,
        get_name,
        get_no_of_bedrooms
    ):
        get_no_of_bedrooms.return_value = 2
        get_name.return_value = 'test name'
        get_no_of_bathrooms.return_value = 3
        get_anemities.return_value = ['test1','test2']

        with pytest.raises(ParsingException):
            data=PropertyParser.parse('html')
