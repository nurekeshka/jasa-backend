from functools import wraps
from django.http import JsonResponse
from jasa.settings import LOGIN_URL
from django.urls import reverse

def ajax_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        print(request)
        return JsonResponse({
            'status': 'REDIRECT',
            'redirect': reverse(LOGIN_URL),
        })
    return wrapper