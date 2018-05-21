from app.property.property_data import PropertyData

class TestPropertyData(object):

    @classmethod
    def setup_class(cls):
        cls.property_data = PropertyData(
                    'Property Name',
                    'Flat',
                    2,
                    3,
                    ['kitchen','parking']
        )

    def test_that_anemities_contains_works_with_single_string(self):
        assert self.property_data.anemities_contains('kitchen')
        assert not self.property_data.anemities_contains('nothing')

    def test_that_anemities_contains_works_with_many_strings(self):
        assert self.property_data.anemities_contains('kitchen','parking')
        assert self.property_data.anemities_contains('parking','kitchen')
        assert not self.property_data.anemities_contains('kitchen','not this one')

    def test_that_anemities_contains_returns_false_with_bad_single(self):
        assert not self.property_data.anemities_contains(1)

    def test_that_correctly_assigns_input(self): 
        assert self.property_data.name == 'Property Name'
        assert self.property_data.property_type == 'Flat'
        assert self.property_data.no_of_bedrooms == 2
        assert self.property_data.no_of_bathrooms == 3
        assert self.property_data.anemities_contains('kitchen','parking')
        assert len(self.property_data.anemities) == 2
