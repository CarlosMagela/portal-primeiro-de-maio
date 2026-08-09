from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "historia/",
        views.historia,
        name="historia"
    ),

    path(
        "conquistas/",
        views.conquistas,
        name="conquistas"
    ),

    path(
        "hall-da-fama/",
        views.hall_fama,
        name="hall_fama"
    ),

    # ======================================================
    # GALERIA
    # ======================================================

    path(
        "galeria/",
        views.galeria,
        name="galeria"
    ),

    path(
        "galeria/<slug:slug>/",
        views.galeria_detalhe,
        name="galeria_detalhe"
    ),

    # ======================================================
    # OUTRAS PÁGINAS
    # ======================================================

    path(
        "patrocinadores/",
        views.patrocinadores,
        name="patrocinadores"
    ),

    path(
        "socio-torcedor/",
        views.socio_torcedor,
        name="socio_torcedor"
    ),

    path(
        "contato/",
        views.contato,
        name="contato"
    ),

    # ======================================================
    # NOTÍCIAS
    # ======================================================

    path(
        "noticias/",
        views.noticias,
        name="noticias"
    ),

    path(
        "noticias/<slug:slug>/",
        views.noticia_detalhe,
        name="noticia_detalhe"
    ),

]

path(
    "galeria/<slug:slug>/",
    views.galeria_detalhe,
    name="galeria_detalhe",
),