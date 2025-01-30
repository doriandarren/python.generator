import os
from .utils import print_message, GREEN, CYAN

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print_message(f"Carpeta creada: {path}", GREEN)
    else:
        print_message(f"Carpeta ya existe: {path}", CYAN)



def generate_layouts(project_path):
    generate_header_layouts(project_path)
    generate_footer_layouts(project_path)



def generate_header_layouts(project_path):
    """
    Genera el archivo HeaderLayout.jsx dentro de la carpeta layouts.
    """
    print_message("Generando HeaderLayout.jsx...", CYAN)

    # Define la ruta del archivo
    layouts_dir = os.path.join(project_path, "src", "layouts", "components")
    file_path = os.path.join(layouts_dir, "HeaderLayout.jsx")

    # Crear la carpeta layouts si no existe
    create_folder(layouts_dir)

    # Contenido del archivo MainLayout.jsx
    main_layout_content = """import { Link, NavLink } from "react-router";
import classNames from "classnames";
import logo from '../../assets/images/logo.svg';


export const HeaderLayout = () => {

    const navLinks = [
        { to: "/", label: "Inicio" },
        { to: "/about", label: "Quienes somos" },
        { to: "/contact", label: "Contacto" },
    ];

    return (
        <>
            <div className="navbar__container">
                <div className="navbar__bar">

                    <div className="navbar__logo">
                        <Link to="/">
                            <img src={logo} alt="logo nucleus" />
                        </Link>
                    </div>

                    <nav className="navigation">
                        {navLinks.map(({ to, label }) => (
                          <li key={to} className="navigation__item">
                              <NavLink
                                to={to}
                                className={({ isActive }) =>
                                  classNames("navigation__link", {
                                    "navigation__link--active": isActive,
                                  })
                                }
                              >
                                {label}
                              </NavLink>
                          </li>
                        ))}
                        
                    </nav>

                </div>
            </div>
        </>
    )
}
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(main_layout_content)
        print_message(f"Archivo creado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al crear el archivo {file_path}: {e}", CYAN)


def generate_footer_layouts(project_path):
    """
    Genera el archivo FooterLayout.jsx dentro de la carpeta layouts.
    """
    print_message("Generando FooterLayout.jsx...", CYAN)

    # Define la ruta del archivo
    layouts_dir = os.path.join(project_path, "src", "layouts", "components")
    file_path = os.path.join(layouts_dir, "FooterLayout.jsx")

    # Crear la carpeta layouts si no existe
    create_folder(layouts_dir)

    # Contenido del archivo Layout.jsx
    main_layout_content = """import logoBlanco from '../../assets/images/logo-blanco.svg';

export const FooterLayout = () => {
  return (
    <footer className="footer">
        <div className="footer__container">
            <div className="footer__grid">

                <div className="footer__logo">
                    <img src={logoBlanco} alt="logo blanco" />
                </div>
                
            </div>
        </div>
    </footer> 
  )
}
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(main_layout_content)
        print_message(f"Archivo creado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al crear el archivo {file_path}: {e}", CYAN)
