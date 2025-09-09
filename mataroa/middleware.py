class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()#.split(':')[0]  # remove port if present
        parts = host.split('.')
        
        # basic subdomain logic: only treat as subdomain if 3+ parts
        if len(parts) >= 4:
            request.subdomain = parts[0]
            print(f"Subdomain detected: {request.subdomain}")

        response = self.get_response(request)
        return response
