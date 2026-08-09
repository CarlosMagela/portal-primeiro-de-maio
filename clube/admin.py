from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Clube,
    Categoria,
    Noticia,
    Galeria,
    Foto,
    Conquista,
    HallDaFama,
    Patrocinador,
)


# ==========================================================
# CLUBE
# ==========================================================

@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):

    list_display = (
        "escudo_admin",
        "nome",
        "sigla",
        "fundacao",
        "telefone",
        "ativo",
    )

    list_filter = (
        "ativo",
    )

    search_fields = (
        "nome",
        "sigla",
    )

    fieldsets = (

        ("Informações", {
            "fields": (
                "nome",
                "sigla",
                "fundacao",
                "historia",
            )
        }),

        ("Imagens", {
            "fields": (
                "escudo",
                "banner",
            )
        }),

        ("Contato", {
            "fields": (
                "telefone",
                "whatsapp",
                "email",
                "endereco",
            )
        }),

        ("Redes Sociais", {
            "fields": (
                "facebook",
                "instagram",
                "youtube",
            )
        }),

        ("Status", {
            "fields": (
                "ativo",
            )
        }),

    )

    def escudo_admin(self, obj):

        if obj.escudo:

            return format_html(
                '<img src="{}" width="55" style="border-radius:6px;">',
                obj.escudo.url
            )

        return "-"

    escudo_admin.short_description = "Escudo"


# ==========================================================
# CATEGORIA
# ==========================================================

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "slug",
        "ativo",
    )

    list_filter = (
        "ativo",
    )

    search_fields = (
        "nome",
    )

    ordering = (
        "nome",
    )

    prepopulated_fields = {
        "slug": ("nome",)
    }


# ==========================================================
# NOTÍCIAS
# ==========================================================

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):

    list_display = (
        "imagem_admin",
        "titulo",
        "categoria",
        "destaque",
        "publicado",
        "criado_em",
    )

    list_filter = (
        "categoria",
        "destaque",
        "publicado",
    )

    search_fields = (
        "titulo",
        "resumo",
        "conteudo",
    )

    ordering = (
        "-criado_em",
    )

    list_per_page = 20

    prepopulated_fields = {
        "slug": ("titulo",)
    }

    fieldsets = (

        ("Informações", {
            "fields": (
                "categoria",
                "titulo",
                "slug",
            )
        }),

        ("Conteúdo", {
            "fields": (
                "resumo",
                "conteudo",
            )
        }),

        ("Imagem", {
            "fields": (
                "imagem",
            )
        }),

        ("Publicação", {
            "fields": (
                "destaque",
                "publicado",
                "ativo",
            )
        }),

    )

    def imagem_admin(self, obj):

        if obj.imagem:

            return format_html(
                '<img src="{}" width="90" style="border-radius:8px;">',
                obj.imagem.url
            )

        return "-"

    imagem_admin.short_description = "Imagem"

    # ==========================================================
    # GALERIAS
    # ==========================================================

    @admin.register(Galeria)
    class GaleriaAdmin(admin.ModelAdmin):

        list_display = (
            "capa_admin",
            "titulo",
            "destaque",
            "ativo",
            "criado_em",
        )

        list_filter = (
            "destaque",
            "ativo",
        )

        search_fields = (
            "titulo",
            "descricao",
        )

        ordering = (
            "-criado_em",
        )

        list_per_page = 20

        prepopulated_fields = {
            "slug": ("titulo",)
        }

        fieldsets = (

            ("Informações", {
                "fields": (
                    "titulo",
                    "slug",
                    "descricao",
                )
            }),

            ("Imagem", {
                "fields": (
                    "capa",
                )
            }),

            ("Publicação", {
                "fields": (
                    "destaque",
                    "ativo",
                )
            }),

        )

        def capa_admin(self, obj):
            if obj.capa:
                return format_html(
                    '<img src="{}" width="90" style="border-radius:8px;">',
                    obj.capa.url
                )

            return "-"

        capa_admin.short_description = "Capa"

    # ==========================================================
    # FOTOS
    # ==========================================================

    @admin.register(Foto)
    class FotoAdmin(admin.ModelAdmin):

        list_display = (
            "imagem_admin",
            "titulo",
            "galeria",
            "ordem",
            "ativo",
        )

        list_filter = (
            "galeria",
            "ativo",
        )

        search_fields = (
            "titulo",
            "legenda",
        )

        ordering = (
            "galeria",
            "ordem",
        )

        list_per_page = 30

        fieldsets = (

            ("Galeria", {
                "fields": (
                    "galeria",
                    "ordem",
                )
            }),

            ("Foto", {
                "fields": (
                    "imagem",
                    "titulo",
                    "legenda",
                )
            }),

            ("Status", {
                "fields": (
                    "ativo",
                )
            }),

        )

        def imagem_admin(self, obj):
            if obj.imagem:
                return format_html(
                    '<img src="{}" width="90" style="border-radius:8px;">',
                    obj.imagem.url
                )

            return "-"

        imagem_admin.short_description = "Foto"

    # ==========================================================
    # CONQUISTAS
    # ==========================================================

    @admin.register(Conquista)
    class ConquistaAdmin(admin.ModelAdmin):

        list_display = (
            "imagem_admin",
            "titulo",
            "campeonato",
            "ano",
            "destaque",
            "ativo",
        )

        list_filter = (
            "ano",
            "destaque",
            "ativo",
        )

        search_fields = (
            "titulo",
            "campeonato",
            "descricao",
        )

        ordering = (
            "-ano",
        )

        list_per_page = 20

        fieldsets = (

            ("Conquista", {
                "fields": (
                    "titulo",
                    "campeonato",
                    "ano",
                    "descricao",
                )
            }),

            ("Imagem", {
                "fields": (
                    "imagem",
                )
            }),

            ("Exibição", {
                "fields": (
                    "destaque",
                    "ativo",
                )
            }),

        )

        def imagem_admin(self, obj):
            if obj.imagem:
                return format_html(
                    '<img src="{}" width="80" style="border-radius:8px;">',
                    obj.imagem.url
                )

            return "-"

        imagem_admin.short_description = "Imagem"

    # ==========================================================
    # HALL DA FAMA
    # ==========================================================

    @admin.register(HallDaFama)
    class HallDaFamaAdmin(admin.ModelAdmin):

        list_display = (
            "foto_admin",
            "nome",
            "funcao",
            "periodo",
            "destaque",
            "ativo",
        )

        list_filter = (
            "funcao",
            "destaque",
            "ativo",
        )

        search_fields = (
            "nome",
            "funcao",
            "periodo",
            "biografia",
            "conquistas",
        )

        ordering = (
            "nome",
        )

        list_per_page = 20

        fieldsets = (

            ("Personalidade", {
                "fields": (
                    "nome",
                    "funcao",
                    "periodo",
                )
            }),

            ("História", {
                "fields": (
                    "biografia",
                    "conquistas",
                )
            }),

            ("Foto", {
                "fields": (
                    "foto",
                )
            }),

            ("Exibição", {
                "fields": (
                    "destaque",
                    "ativo",
                )
            }),

        )

        def foto_admin(self, obj):
            if obj.foto:
                return format_html(
                    '<img src="{}" width="70" style="border-radius:50%;">',
                    obj.foto.url
                )

            return "-"

        foto_admin.short_description = "Foto"

    # ==========================================================
    # PATROCINADORES
    # ==========================================================

    @admin.register(Patrocinador)
    class PatrocinadorAdmin(admin.ModelAdmin):

        list_display = (
            "logo_admin",
            "nome",
            "ordem",
            "ativo_site",
            "ativo",
        )

        list_filter = (
            "ativo_site",
            "ativo",
        )

        search_fields = (
            "nome",
            "descricao",
        )

        ordering = (
            "ordem",
            "nome",
        )

        list_per_page = 20

        fieldsets = (

            ("Patrocinador", {
                "fields": (
                    "nome",
                    "descricao",
                )
            }),

            ("Logo e Site", {
                "fields": (
                    "logo",
                    "site",
                )
            }),

            ("Exibição", {
                "fields": (
                    "ordem",
                    "ativo_site",
                    "ativo",
                )
            }),

        )

        def logo_admin(self, obj):
            if obj.logo:
                return format_html(
                    '<img src="{}" width="100" style="object-fit:contain;">',
                    obj.logo.url
                )

            return "-"

        logo_admin.short_description = "Logo"