from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from navigation import Menu, get_cascade_condition

from .icons import icon_menu_tags
from .permissions import permission_tag_create, permission_tag_view

menu_tags = Menu(
    condition=get_cascade_condition(
        app_label='tags', model_name='Tag',
        object_permission=permission_tag_view,
        view_permission=permission_tag_create,
    ), icon_class=icon_menu_tags, label=_('Tags'), name='tags menu'
)
