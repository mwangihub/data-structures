from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from ..views import views

urlpatterns = [
    path("", views.NodeView.as_view(), name="node_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
