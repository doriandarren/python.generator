from django.db import models
from django.conf import settings
from django.utils import timezone

# Para usar en los Objeto:
# objects → solo devuelve registros no eliminados
# all_objects → devuelve todos, incluidos los soft deleted
# delete() → hace soft delete automáticamente
# hard_delete() → borra físicamente de la base de datos
# restore() → recupera un registro borrado lógicamente
# is_deleted → te dice si está eliminado
#
# Ejemplos de Usos:
# example = Example.objects.get(id=1)
# example.delete()                                        # Esto no lo elimina físicamente, solo pone deleted_at
# example.restore()                                       # Restaurar
# example.hard_delete()                                   # Eliminar fisicamente
#
# Consultas
# Example.objects.all()                                   # Solo activos
# Example.all_objects.all()                               # Todos
# Example.all_objects.filter(deleted_at__isnull=False)    # Solo eliminados


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class AllObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created"
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated"
    )

    objects = ActiveManager()
    all_objects = AllObjectsManager()

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    def soft_delete(self, user=None):
        self.deleted_at = timezone.now()
        if user:
            self.updated_by = user
        self.save(update_fields=["deleted_at", "updated_by", "updated_at"])

    def restore(self, user=None):
        self.deleted_at = None
        if user:
            self.updated_by = user
        self.save(update_fields=["deleted_at", "updated_by", "updated_at"])

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at", "updated_at"])

    def hard_delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)