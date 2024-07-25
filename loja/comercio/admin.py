from django.contrib import admin
from .models import Produto

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "qntd")

admin.site.register(Produto, ProdutoAdmin)
