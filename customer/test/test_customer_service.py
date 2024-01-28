from unittest.mock import create_autospec

import pytest

from customer.domain.customer import CustomerCreate
from customer.infra.customer_event_service import CustomerEventService
from customer.infra.customer_repository import CustomerRepository
from customer.service_layer.customer import CustomerService


@pytest.fixture
def customer_repository():
    return create_autospec(CustomerRepository, instance=True)


@pytest.fixture
def customer_event_service():
    return create_autospec(CustomerEventService, instance=True)


@pytest.fixture
def customer_service(
    customer_repository,
    customer_event_service,
) -> CustomerService:
    return CustomerService(
        customer_repository=customer_repository,
        customer_event_service=customer_event_service,
    )


class TestCustomerService:
    def test_create(
        self,
        customer_service,
        customer_repository,
        customer_event_service,
    ):
        customer_service.create_customer(
            first_name="Test",
            last_name="Customer",
            email="test@fake.com",
        )

        customer_repository.create.assert_called_once_with(
            CustomerCreate(
                first_name="Test", last_name="Customer", email="test@fake.com"
            )
        )

        customer_event_service.create_customer.assert_called_once_with(
            CustomerCreate(
                first_name="Test", last_name="Customer", email="test@fake.com"
            )
        )
