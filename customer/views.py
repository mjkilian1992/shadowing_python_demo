from django.forms import ModelForm
from django.views.generic import FormView, TemplateView

from . import models as customer_models


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
        print(f"FORM DATA: {form.cleaned_data}")
        return super().form_valid(form)


class Thanks(TemplateView):
    template_name = "customer/thanks.html"
