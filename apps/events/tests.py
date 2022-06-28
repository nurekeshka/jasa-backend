from apps.events.constants import organization_types
from apps.events.models import Organization
from django.core.exceptions import ValidationError
from django.test import TestCase



class OrganizationModelTests(TestCase):
    valid_organization_name = 'Nazarbayev Intellectual School in Physics Mathematics Direction - Almaty'
    valid_organization_description = 'Accelerated socio-economic development of Kazakhstan in the early 21st century has caused an urgent need for professionals with a high level of technical, managerial and leadership competencies, so in 2008 year at the initiative of the First President of the Republic of Kazakhstan, Leader of the Nation Nursultan Nazarbayev, a project of creation the Intellectual schools had been launched.'

    invalid_organization_type = 'Hello, world!'

    def test_organization_type_validation_valid(self):
        Organization.objects.create(name=self.valid_organization_name, type=organization_types[1][0], description=self.valid_organization_description).full_clean()


    def test_organization_type_validation_invalid(self):
        with self.assertRaises(ValidationError):
            Organization.objects.create(name=self.valid_organization_name, type=self.invalid_organization_type, description=self.valid_organization_description).full_clean()
