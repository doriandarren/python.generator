from gen.react.to_create_project.components.component_eye_off_icon import generate_eye_off_icon
from gen.react.to_create_project.components.component_eye_on_icon import generate_eye_on_icon
from gen.react.to_create_project.components.component_text import generate_text
from .component_cards import generate_cards
from .component_alert import generate_alert
from .component_badges import generate_badges
from .component_button import generate_button
from .component_combobox import generate_combobox
from .component_datatable import generate_datatable
from .component_invoice_icon import generate_invoice_icon
from .component_preloader import generate_preloader
from .component_preloader_button import generate_preloader_button
from .component_preloader_button_css import generate_preloader_button_css
from .component_preloader_main import generate_preloader_main
from .component_preloader_main_css import generate_preloader_main_css
from .component_preloader_svg import generate_preloader_svg
from .component_section import generate_section
from .component_toggle import generate_toggle
from .component_tooltip import generate_tooltip


def generate_components(full_path):
    
    generate_alert(full_path)
    generate_badges(full_path)
    generate_button(full_path)
    generate_cards(full_path)
    generate_combobox(full_path)
    generate_datatable(full_path)
    generate_eye_off_icon(full_path)
    generate_eye_on_icon(full_path)
    generate_invoice_icon(full_path)
    generate_preloader(full_path)
    generate_preloader_button(full_path)
    generate_preloader_button_css(full_path)
    generate_preloader_main(full_path)
    generate_preloader_main_css(full_path)
    generate_preloader_svg(full_path)
    generate_section(full_path)
    generate_text(full_path)
    generate_toggle(full_path)
    generate_tooltip(full_path)
