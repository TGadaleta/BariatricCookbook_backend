from django.apps import AppConfig
from django.db.transaction import on_commit


class HealthymealConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'healthymeal'

    def ready(self):
        """Lazy import signals to avoid accessing the database during app initialization."""
        def import_signals():
            import healthymeal.signals

        on_commit(import_signals)  # ✅ Ensures signals are loaded only after DB is ready