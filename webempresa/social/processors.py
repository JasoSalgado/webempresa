"""Social processors."""

# Django modules
from .models import Link

# Context ctx
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx
    
