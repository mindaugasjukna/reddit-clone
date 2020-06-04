
from django.template.response import TemplateResponse


def index(request):
    context = {}
    return TemplateResponse(request, "languagefilter_middleware/index.html", context=context)
