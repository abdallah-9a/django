from datetime import timedelta
from django.utils.timezone import now

class LastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.user.is_authenticated:
            profile = request.user
            if not profile.last_seen or (now() - profile.last_seen) > timedelta(minutes=1):
                profile.last_seen = now()
                profile.save(update_fields=['last_seen'])
        response = self.get_response(request)
        return response