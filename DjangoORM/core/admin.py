from django.contrib import admin

from core.models import Chassi, Carro, Montadora

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero', )


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'chassi', 'preco', 'preco')


@admin.register(Montadora)
class MontadoraAdmon(admin.ModelAdmin):
    list_display = ('nome', )
