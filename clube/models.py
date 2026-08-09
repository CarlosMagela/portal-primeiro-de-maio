import uuid

from django.db import models
from django.utils.text import slugify


# ==========================================================
# MODEL BASE
# ==========================================================

class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


# ==========================================================
# CLUBE
# ==========================================================

class Clube(BaseModel):

    nome = models.CharField(
        max_length=150,
        verbose_name="Nome do Clube"
    )

    sigla = models.CharField(
        max_length=20,
        blank=True
    )

    fundacao = models.PositiveIntegerField(
        verbose_name="Ano de Fundação"
    )

    escudo = models.ImageField(
        upload_to="clube/",
        blank=True,
        null=True
    )

    banner = models.ImageField(
        upload_to="clube/",
        blank=True,
        null=True
    )

    historia = models.TextField(blank=True)

    telefone = models.CharField(
        max_length=30,
        blank=True
    )

    whatsapp = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField(blank=True)

    endereco = models.CharField(
        max_length=255,
        blank=True
    )

    facebook = models.URLField(blank=True)

    instagram = models.URLField(blank=True)

    youtube = models.URLField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Clube"
        verbose_name_plural = "Clube"


# ==========================================================
# CATEGORIA
# ==========================================================

class Categoria(BaseModel):

    nome = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.nome)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


# ==========================================================
# NOTÍCIA
# ==========================================================

class Noticia(BaseModel):

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="noticias"
    )

    titulo = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    resumo = models.TextField()

    conteudo = models.TextField()

    imagem = models.ImageField(
        upload_to="noticias/",
        blank=True,
        null=True
    )

    destaque = models.BooleanField(default=False)

    publicado = models.BooleanField(default=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.titulo)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-criado_em"]
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

# ==========================================================
# GALERIA
# ==========================================================

class Galeria(BaseModel):

    titulo = models.CharField(max_length=150)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    descricao = models.TextField(blank=True)

    capa = models.ImageField(
        upload_to="galeria/capas/",
        blank=True,
        null=True
    )

    destaque = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.titulo)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Galeria"
        verbose_name_plural = "Galerias"


# ==========================================================
# FOTO
# ==========================================================

class Foto(BaseModel):

    galeria = models.ForeignKey(
        Galeria,
        on_delete=models.CASCADE,
        related_name="fotos"
    )

    titulo = models.CharField(
        max_length=150,
        blank=True
    )

    imagem = models.ImageField(
        upload_to="galeria/fotos/"
    )

    legenda = models.CharField(
        max_length=255,
        blank=True
    )

    ordem = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.titulo or self.legenda or "Foto"

    class Meta:
        ordering = ["ordem"]
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

# ==========================================================
# CONQUISTA
# ==========================================================

class Conquista(BaseModel):

    titulo = models.CharField(
        max_length=150,
        verbose_name="Título"
    )

    ano = models.PositiveIntegerField(
        verbose_name="Ano"
    )

    campeonato = models.CharField(
        max_length=150,
        verbose_name="Campeonato"
    )

    descricao = models.TextField(
        blank=True,
        verbose_name="Descrição"
    )

    imagem = models.ImageField(
        upload_to="conquistas/",
        blank=True,
        null=True,
        verbose_name="Imagem"
    )

    destaque = models.BooleanField(
        default=False,
        verbose_name="Destaque"
    )

    def __str__(self):
        return f"{self.titulo} - {self.ano}"

    class Meta:
        ordering = ["-ano"]
        verbose_name = "Conquista"
        verbose_name_plural = "Conquistas"

# ==========================================================
# HALL DA FAMA
# ==========================================================

class HallDaFama(BaseModel):

    nome = models.CharField(
        max_length=150,
        verbose_name="Nome"
    )

    foto = models.ImageField(
        upload_to="hall_da_fama/",
        blank=True,
        null=True,
        verbose_name="Foto"
    )

    funcao = models.CharField(
        max_length=100,
        verbose_name="Função"
    )

    periodo = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Período"
    )

    biografia = models.TextField(
        blank=True,
        verbose_name="Biografia"
    )

    conquistas = models.TextField(
        blank=True,
        verbose_name="Principais Conquistas"
    )

    destaque = models.BooleanField(
        default=False,
        verbose_name="Destaque"
    )

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
        verbose_name = "Hall da Fama"
        verbose_name_plural = "Hall da Fama"

# ==========================================================
# PATROCINADOR
# ==========================================================

class Patrocinador(BaseModel):

    nome = models.CharField(
        max_length=150,
        verbose_name="Nome"
    )

    logo = models.ImageField(
        upload_to="patrocinadores/",
        verbose_name="Logo"
    )

    site = models.URLField(
        blank=True,
        verbose_name="Site"
    )

    descricao = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Descrição"
    )

    ordem = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordem"
    )

    ativo_site = models.BooleanField(
        default=True,
        verbose_name="Exibir no site"
    )

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["ordem", "nome"]
        verbose_name = "Patrocinador"
        verbose_name_plural = "Patrocinadores"