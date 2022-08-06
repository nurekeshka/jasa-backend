from jasa.settings import DOMAIN

def constants(request):
    """Add constants to context"""
    return {
        'DOMAIN': DOMAIN,
        'EVENT_DESC_LENGTH': 50,
        'CURRENT_URL': request.get_full_path(),
    }