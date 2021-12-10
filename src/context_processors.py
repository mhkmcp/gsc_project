from .models import Notice


def get_notice(request):
    notices = Notice.objects.filter(is_active=True).order_by("-id")
    return {"notices": notices}
