from django.contrib import admin
from django.urls import path, include
from core.views import Cadastrar, home, carinho, cadastrar_cliente, cadastrar_produto, listar_produto, editar_produto, excluir_produto, exibir_produto
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('', home, name='url_home'),
    path('cadastrar/', Cadastrar.as_view(), name='url_cadastrar'),
    path('carrinho/', carinho, name='url_carrinho'),
    path('cadastrar_cliente/', cadastrar_cliente, name='url_cadastrar_cliente'),
    path('cadastrar_produto/', cadastrar_produto, name='url_cadastrar_produto'),
    path('listar_produto/', listar_produto, name='url_listar_produto'),
    path('editar_produto/<int:id>/', editar_produto, name='url_editar_produto'),
    path('excluir_produto/<int:id>/', excluir_produto, name='url_excluir_produto'),
    path('exibir_produto/<int:id>/', exibir_produto, name='url_exibir_produto')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
