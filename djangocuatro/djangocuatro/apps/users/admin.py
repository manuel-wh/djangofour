# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from djangocuatro.apps.users.models import User, TipoPersona, TipoUsuario, ClientStatus


# Register your models here.
admin.site.register(User)
admin.site.register(TipoUsuario)
admin.site.register(TipoPersona)
admin.site.register(ClientStatus)

