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
    """
    Genera el archivo MainLayout.jsx dentro de la carpeta layouts.
    """
    print_message("Generando MainLayout.jsx...", CYAN)

    # Define la ruta del archivo
    layouts_dir = os.path.join(project_path, "src", "layouts")
    file_path = os.path.join(layouts_dir, "MainLayout.jsx")

    # Crear la carpeta layouts si no existe
    create_folder(layouts_dir)

    # Contenido del archivo MainLayout.jsx
    main_layout_content = """import { useState } from "react";

export const MainLayout = ({ children }) => {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <div className="flex flex-col min-h-screen">
      {/* Navbar */}
      <header className="bg-primary-dark text-neutral-light">
        <nav className="container mx-auto flex justify-between items-center p-4">
          {/* Logo */}
          <div className="text-2xl font-bold">
            <a href="/">MyApp</a>
          </div>

          {/* Hamburger Menu (visible solo en pantallas pequeñas) */}
          <button
            className="block md:hidden"
            onClick={() => setMenuOpen(!menuOpen)}
          >
            <span className="text-3xl">&#9776;</span>
          </button>

          {/* Links (visibles en pantallas medianas y grandes) */}
          <ul className="hidden md:flex md:space-x-4">
            <li>
              <a href="/" className="hover:text-primary-light transition">
                Home
              </a>
            </li>
            <li>
              <a href="/about" className="hover:text-primary-light transition">
                About
              </a>
            </li>
            <li>
              <a
                href="/contact"
                className="hover:text-primary-light transition"
              >
                Contact
              </a>
            </li>
          </ul>
        </nav>
      </header>

      {/* Overlay */}
      {menuOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-40"
          onClick={() => setMenuOpen(false)}
        ></div>
      )}

      {/* Side Menu (visible solo en pantallas pequeñas) */}
      <div
        className={`fixed inset-y-0 left-0 z-50 w-64 bg-primary-dark text-neutral-light transform ${
          menuOpen ? "translate-x-0" : "-translate-x-full"
        } transition-transform duration-300 ease-in-out md:hidden`}
      >
        <button
          className="absolute top-4 right-4 text-2xl"
          onClick={() => setMenuOpen(false)}
        >
          &times;
        </button>
        <ul className="flex flex-col space-y-4 p-6">
          <li>
            <a href="/" className="hover:text-primary-light transition">
              Home
            </a>
          </li>
          <li>
            <a href="/about" className="hover:text-primary-light transition">
              About
            </a>
          </li>
          <li>
            <a href="/contact" className="hover:text-primary-light transition">
              Contact
            </a>
          </li>
        </ul>
      </div>

      {/* Main Content */}
      <main className="flex-grow container mx-auto p-6">{children}</main>

      {/* Footer */}
      <footer className="bg-primary-dark text-neutral-light">
        <div className="container mx-auto py-4 flex flex-col md:flex-row justify-between items-center">
          <p>© 2025 MyApp. All rights reserved.</p>
          <div className="flex space-x-4 mt-2 md:mt-0">
            <a href="#" className="hover:text-primary-light transition">
              Twitter
            </a>
            <a href="#" className="hover:text-primary-light transition">
              Facebook
            </a>
            <a href="#" className="hover:text-primary-light transition">
              Instagram
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(main_layout_content)
        print_message(f"Archivo creado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al crear el archivo {file_path}: {e}", CYAN)
