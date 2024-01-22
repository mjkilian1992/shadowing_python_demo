import abc

from customer import models as customer_models
from customer.domain.customer import CustomerEntity


class CustomerRepository(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, id: str) -> CustomerEntity | None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_email(self, email: str) -> CustomerEntity | None:
        raise NotImplementedError()

    @abc.abstractmethod
    def add(self, customer: CustomerEntity) -> None:
        raise NotImplementedError()


class DjangoCustomerRepository(CustomerRepository):
    def _django_model_to_entity(self, model: customer_models.Customer):
        return CustomerEntity(
            id=model.pk,
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
        )

    def get_by_id(self, id: str) -> CustomerEntity | None:
        try:
            model = customer_models.Customer.objects.get(pk=id)
            return self._django_model_to_entity(model)
        except customer_models.Customer.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> CustomerEntity | None:
        try:
            model = customer_models.Customer.objects.get(email=email)
            return self._django_model_to_entity(model)
        except customer_models.Customer.DoesNotExist:
            return None

    def create(self, customer: CustomerEntity) -> None:
        pass
