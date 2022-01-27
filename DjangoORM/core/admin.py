from django.contrib import admin

from core.models import Chassi, Carro, Montadora


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero', )


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motoristas')

    def get_motoristas(self, obj):
        return ', '.join([m.username for m in obj.motoristas.all()])

    get_motoristas.short_description = 'Motoristas'


@admin.register(Montadora)
class MontadoraAdmon(admin.ModelAdmin):
    list_display = ('nome', )
