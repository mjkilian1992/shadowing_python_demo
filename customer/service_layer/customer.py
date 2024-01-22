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
        pass
