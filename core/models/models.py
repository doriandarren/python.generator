from django.db import models
from django.conf import settings
from django.utils import timezone


# QuerySet personalizado para controlar eliminaciones masivas
class SoftDeleteQuerySet(models.QuerySet):

    def delete(self):
        # Eliminación lógica de múltiples registros
        return self.update(
            deleted_at=timezone.now(),
            updated_at=timezone.now()
        )

    def hard_delete(self):
        # Eliminación física de múltiples registros
        return super().delete()


# Manager: solo registros activos
class ActiveManager(models.Manager.from_queryset(SoftDeleteQuerySet)):

    def get_queryset(self):
        return super().get_queryset().filter(
            deleted_at__isnull=True
        )


# Manager: todos los registros, incluidos los eliminados
class AllObjectsManager(models.Manager.from_queryset(SoftDeleteQuerySet)):
    pass


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

        self.save(update_fields=[
            "deleted_at", "updated_by", "updated_at"
        ])

    def restore(self, user=None):
        self.deleted_at = None

        if user:
            self.updated_by = user

        self.save(update_fields=[
            "deleted_at", "updated_by", "updated_at"
        ])

    def delete(self, using=None, keep_parents=False):
        self.soft_delete()

    def hard_delete(self, using=None, keep_parents=False):
        return super().delete(
            using=using,
            keep_parents=keep_parents
        )