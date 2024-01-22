import pytest

from customer import models as customer_models
from customer.domain.customer import CustomerCreate
from customer.infra.customer_repository import DjangoCustomerRepository


@pytest.fixture
def customer_repository():
    return DjangoCustomerRepository()


@pytest.mark.django_db
class TestCustomerDjangoRepository:
    def test_create(self, customer_repository):
        customer_entity = CustomerCreate(
            first_name="Test", last_name="Customer", email="test@fake.com"
        )
        customer_repository.create(customer_entity)

        assert customer_models.Customer.objects.count() == 1
