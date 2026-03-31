import os
import pdfkit

from django.conf import settings
from django.template.loader import render_to_string


class PdfService:

    def __init__(
        self,
        template_html="pdfs/test_pdf.html",
        wkhtmltopdf_path=None,
        footer_text="EMPRESA",
    ):
        self.template_html = template_html
        self.footer_text = footer_text
        self.app_env = getattr(settings, "APP_ENV", "local")
        self.wkhtmltopdf_path = wkhtmltopdf_path or self._detect_wkhtmltopdf_path()

    def _detect_wkhtmltopdf_path(self):
        paths = {
            "local": "/usr/local/bin/wkhtmltopdf",
            "staging": "/usr/bin/wkhtmltopdf",
            "production": "/usr/bin/wkhtmltopdf",
        }

        path = paths.get(self.app_env)

        if not path:
            raise ValueError(f"APP_ENV no válido: {self.app_env}")

        if not os.path.exists(path):
            raise FileNotFoundError(
                f"No se encontró wkhtmltopdf en la ruta configurada: {path}"
            )

        return path

    def _get_config(self):
        return pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)

    def _get_options(self):
        return {
            "encoding": "UTF-8",
            "page-size": "A4",
            "margin-top": "15mm",
            "margin-right": "10mm",
            "margin-bottom": "20mm",
            "margin-left": "10mm",
            "footer-font-size": "9",
            "footer-spacing": "5",
            "footer-left": self.footer_text,
            "footer-right": "Página [page] de [topage]",
            "enable-local-file-access": "",
        }

    def _render_html(self, context=None):
        if context is None:
            context = {}

        return render_to_string(self.template_html, context)

    def get_binary(self, context=None):
        html_string = self._render_html(context)

        pdf_binary = pdfkit.from_string(
            html_string,
            False,
            configuration=self._get_config(),
            options=self._get_options(),
        )

        return pdf_binary

    def save(self, filename, context=None, folder="pdfs"):
        html_string = self._render_html(context)

        folder_path = os.path.join(settings.MEDIA_ROOT, folder)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, filename)

        pdfkit.from_string(
            html_string,
            file_path,
            configuration=self._get_config(),
            options=self._get_options(),
        )

        return file_path