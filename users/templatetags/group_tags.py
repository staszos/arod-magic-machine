# myapp/templatetags/group_tags.py
from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='in_group')
def in_group(user, group_name):
    """
    Check if a user is in a specific group.
    Usage: {% if user|in_group:"GroupName" %} ... {% endif %}
    """
    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False  # Or handle the case where the group doesn't exist.
    return group in user.groups.all()  # .all() is needed with django 4 and up