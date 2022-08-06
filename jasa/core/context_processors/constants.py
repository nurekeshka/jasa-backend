def constants(request):
    """Add constants to context"""
    return {
        'DOMAIN': request.get_host(),
        'EVENT_DESC_LENGTH': 25,
    }