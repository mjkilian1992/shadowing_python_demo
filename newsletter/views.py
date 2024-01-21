from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "newsletter/index.html"


class ArticlesView(TemplateView):
    template_name = "newsletter/articles.html"
