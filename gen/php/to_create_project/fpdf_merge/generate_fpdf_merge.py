import os

from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command


def generate_fpdf_merge(full_path):
    install_fpdf_merge(full_path)


def install_fpdf_merge(full_path):
    print_message("Instalando FPDF Merge...", CYAN)
    run_command("composer require setasign/fpdf setasign/fpdi", cwd=full_path)
    print_message("FPDF Merge instalado correctamente.", GREEN)


