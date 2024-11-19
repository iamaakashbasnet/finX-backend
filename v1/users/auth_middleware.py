from django.utils.deprecation import MiddlewareMixin


class TenantAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Determine the tenant context (simplified)
        tenant = getattr(request, 'tenant', None)
        request.is_public = (tenant == 'public')

        if request.is_public:
            request.authentication_backend = 'public_backend'
        else:
            request.authentication_backend = 'tenant_backend'
