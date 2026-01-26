from tastypie.authentication import ApiKeyAuthentication

# Custom authentication logic can be added here


class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return super().is_authenticated(request, **kwargs)
