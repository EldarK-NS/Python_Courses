from tastypie.authentication import APiKeyAuthentication

# Custom authentication logic can be added here


class CustomAuthentication(APiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return super().is_authenticated(request, **kwargs)
