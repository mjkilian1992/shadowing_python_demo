from customer.domain.customer import CustomerCreate
from customer.infra.customer_event_service import CustomerEventService
from customer.infra.customer_repository import CustomerRepository


class CustomerService:
    def __init__(
        self,
        customer_repository: CustomerRepository,
        customer_event_service: CustomerEventService,
    ):
        self.customer_repository = customer_repository
        self.customer_event_service = customer_event_service

    def create_customer(
        self,
        first_name: str,
        last_name: str,
        email: str,
    ):
        customer_create = CustomerCreate(
            first_name=first_name, last_name=last_name, email=email
        )
        self.customer_repository.create(customer_create)
        self.customer_event_service.create_customer(customer_create)
