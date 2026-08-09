from django.shortcuts import render, get_object_or_404

from .models import (
    Clube,
    Noticia,
    Conquista,
    HallDaFama,
    Galeria,
    Patrocinador,
)


def home(request):

    clube = Clube.objects.first()

    noticias_destaque = Noticia.objects.filter(
        publicado=True,
        destaque=True,
        ativo=True,
    ).order_by("-criado_em")[:3]

    context = {
        "clube": clube,
        "noticias_destaque": noticias_destaque,
    }

    return render(request, "home.html", context)


def noticias(request):

    clube = Clube.objects.first()

    noticias = Noticia.objects.filter(
        publicado=True,
        ativo=True,
    ).order_by("-criado_em")

    context = {
        "clube": clube,
        "noticias": noticias,
    }

    return render(request, "noticias.html", context)


def noticia_detalhe(request, slug):

    clube = Clube.objects.first()

    noticia = get_object_or_404(
        Noticia,
        slug=slug,
        publicado=True,
        ativo=True,
    )

    context = {
        "clube": clube,
        "noticia": noticia,
    }

    return render(request, "noticia_detalhe.html", context)


def historia(request):

    clube = Clube.objects.first()

    context = {
        "clube": clube,
    }

    return render(request, "historia.html", context)


def conquistas(request):

    clube = Clube.objects.first()

    conquistas = Conquista.objects.filter(
        ativo=True
    ).order_by("-ano")

    context = {
        "clube": clube,
        "conquistas": conquistas,
    }

    return render(request, "conquistas.html", context)


def hall_fama(request):

    clube = Clube.objects.first()

    homenageados = HallDaFama.objects.filter(
        ativo=True
    ).order_by("nome")

    context = {
        "clube": clube,
        "homenageados": homenageados,
    }

    return render(request, "hall_fama.html", context)


def galeria(request):

    clube = Clube.objects.first()

    galerias = Galeria.objects.filter(
        ativo=True
    ).order_by("-criado_em")

    context = {
        "clube": clube,
        "galerias": galerias,
    }

    return render(request, "galeria.html", context)

def galeria_detalhe(request, slug):

    clube = Clube.objects.first()

    galeria = get_object_or_404(
        Galeria,
        slug=slug,
        ativo=True,
    )

    fotos = galeria.fotos.filter(
        ativo=True
    ).order_by(
        "ordem",
        "criado_em",
    )

    context = {
        "clube": clube,
        "galeria": galeria,
        "fotos": fotos,
    }

    return render(
        request,
        "galeria_detalhe.html",
        context,
    )
def patrocinadores(request):

    clube = Clube.objects.first()

    patrocinadores = Patrocinador.objects.filter(
        ativo=True,
        ativo_site=True,
    ).order_by("ordem")

    context = {
        "clube": clube,
        "patrocinadores": patrocinadores,
    }

    return render(request, "patrocinadores.html", context)


def socio_torcedor(request):

    clube = Clube.objects.first()

    context = {
        "clube": clube,
    }

    return render(request, "socio_torcedor.html", context)


def contato(request):

    clube = Clube.objects.first()

    context = {
        "clube": clube,
    }

    return render(request, "contato.html", context)

def galeria_detalhe(request, slug):

    clube = Clube.objects.first()

    galeria = get_object_or_404(
        Galeria,
        slug=slug,
    )

    fotos = galeria.fotos.all().order_by(
        "ordem",
        "criado_em",
    )

    context = {
        "clube": clube,
        "galeria": galeria,
        "fotos": fotos,
    }

    return render(
        request,
        "galeria_detalhe.html",
        context,
    )