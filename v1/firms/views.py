from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Firm, Domain


def index(request):
    current_firm = get_object_or_404(Firm, schema_name=request.tenant)
    current_domain = get_object_or_404(Domain, tenant=current_firm)
    return HttpResponse(f''
                        f'<h1>{request.tenant} index</h1>'
                        f'<p>Firm: {current_firm.name}</p>'
                        f'<p>Domain: {current_domain.domain}</p>'
                        f'<p>Subscription: {current_firm.subscription_is_active}</p>')
