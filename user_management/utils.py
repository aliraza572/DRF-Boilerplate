from ipware import get_client_ip as get_client_ip_from_ipware
from django.http import HttpRequest

def get_client_ip(request):
    """
    Get the client's IP address from the request object.
    """
    client_ip, _ = get_client_ip_from_ipware(request)
    if client_ip is None:
        # If ipware fails to retrieve the IP, fallback to a default method
        client_ip = _get_client_ip_default(request)
    return client_ip

def _get_client_ip_default(request):
    """
    Fallback method to get the client's IP address using default request attributes.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    return ip