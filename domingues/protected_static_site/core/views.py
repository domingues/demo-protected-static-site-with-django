import posixpath
from pathlib import Path

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils._os import safe_join
from django.views import View
from django.views.static import serve


class Profile(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "protected_static_site/profile.html")


class ServeStaticSite(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, path: str = "/") -> HttpResponse | FileResponse:
        document_root = settings.SITE_DIR
        show_indexes = settings.SHOW_INDEXES

        fullpath = Path(safe_join(document_root, posixpath.normpath(path).lstrip("/")))
        if fullpath.is_dir() and (fullpath / "index.html").exists():
            path += "/index.html"

        return serve(
            request, path, document_root=document_root, show_indexes=show_indexes
        )
