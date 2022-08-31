from django.contrib import admin

from core.models import Usuario, Categoria, Editora, Livro, Autor

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Autor)
