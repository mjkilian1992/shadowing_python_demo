from django.forms import ModelForm
from django.views.generic import FormView, TemplateView

from . import models as customer_models
from .domain.customer import CustomerCreate
from .infra.customer_repository import DjangoCustomerRepository


class SignUpForm(ModelForm):
    class Meta:
        model = customer_models.Customer
        fields = ["first_name", "last_name", "email"]


# Create your views here.
class SignUp(FormView):
    form_class = SignUpForm
    template_name = "customer/signup.html"
    success_url = "/customer/thanks/"

    def form_valid(self, form):
        repository = DjangoCustomerRepository()
        repository.create(
            CustomerCreate(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
            )
        )
        return super().form_valid(form)


class Thanks(TemplateView):
    template_name = "customer/thanks.html"
