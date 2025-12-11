from django.utils.translation import ugettext_lazy as _
from rest_framework import status


NO_POLICY = {
    "message": _("You don't have policy."),
    "status_code": 403
}


def get_perm(request):
    if request.data.get('status') == 'return':
        perm = "articles.can_change_return"
    elif request.data.get('status') == 'waiting_accept':
        perm = "articles.can_change_waiting_accept"
    elif request.data.get('status') == 'accepted':
        perm = "articles.can_change_accepted"
    elif request.data.get('status') == 'published':
        perm = "articles.can_change_published"
    elif request.data.get('take_down'):
        perm = "can_change_take_down"
    else:
        perm = "articles.can_change_draft"
    return perm


def validate_permission_status_article(request, perm):
    status_art = request.data.get('status')
    manager = request.user.get_role_name()
    if not request.user.has_perm(perm):
        return False, NO_POLICY, status.HTTP_403_FORBIDDEN
    else:
        if status_art == 'accepted' or status_art == 'published' or status_art == 'take_down':
            if 'Manager' not in manager:
                return False, NO_POLICY, status.HTTP_403_FORBIDDEN
        return True, request.user.partner, status.HTTP_200_OK


def validate_permission(request, perm):
    if not request.user.has_perm(perm):
        return False, NO_POLICY, status.HTTP_403_FORBIDDEN
    return True, request.user.partner, status.HTTP_200_OK
