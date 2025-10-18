from django.urls import path

from blog.views import Home, NoteCreate, NoteDetail, NoteUpdate, NoteDelete
from catalog.apps import CatalogConfig
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path("", Home.as_view(), name="blog_main"),
    path("create_note/", NoteCreate.as_view(), name="create_note"),
    path("detail_note/<int:pk>/", NoteDetail.as_view(), name="detail_note"),
    path("update_note/<int:pk>/", NoteUpdate.as_view(), name="update_note"),
    path("delete_note/<int:pk>/", NoteDelete.as_view(), name="delete_note"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
