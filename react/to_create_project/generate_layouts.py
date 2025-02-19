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
    generate_public_header_layouts(project_path)
    generate_public_footer_layouts(project_path)

    generate_private_session_layouts(project_path)



def generate_public_header_layouts(project_path):
    """
    Genera el archivo dentro de la carpeta layouts.
    """
    print_message("Generando HeaderLayout.jsx...", CYAN)

    # Define la ruta del archivo
    layouts_dir = os.path.join(project_path, "src", "layouts", "public")
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
            <header className="header__container">
                <div className="header__bar">

                    <div className="header__logo">
                        <Link to="/">
                            <img src={logo} alt="logo nucleus" />
                        </Link>
                    </div>

                    <nav className="navbar">
                        {navLinks.map(({ to, label }) => (
                          <li 
                            key={to} 
                            className="navbar__item"
                          >
                              <NavLink
                                to={to}
                                className={({ isActive }) =>
                                  classNames("navbar__link", {
                                    "navbar__link--active": isActive,
                                  })
                                }
                              >
                                {label}
                              </NavLink>
                          </li>
                        ))}
                        
                        <li>
                          <NavLink to="/auth/login" className="btn btn-primary">Login</NavLink>
                        </li>
                        
                    </nav>

                </div>
            </header>
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


def generate_public_footer_layouts(project_path):
    """
    Genera el archivo dentro de la carpeta layouts.
    """
    print_message("Generando FooterLayout.jsx...", CYAN)

    # Define la ruta del archivo
    layouts_dir = os.path.join(project_path, "src", "layouts", "public")
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



def generate_private_session_layouts(project_path):
    """
    Genera el archivo dentro de la carpeta layouts.
    """
    print_message("Generando SessionLayout.jsx...", CYAN)

    # Define la ruta del archivo
    layouts_dir = os.path.join(project_path, "src", "layouts", "private")
    file_path = os.path.join(layouts_dir, "SessionLayout.jsx")

    # Crear la carpeta layouts si no existe
    create_folder(layouts_dir)

    # Contenido del archivo
    main_layout_content = """"use client";

import { useState } from "react";
import {
  Dialog,
  DialogBackdrop,
  DialogPanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  TransitionChild,
} from "@headlessui/react";
import {
  Bars3Icon,
  BellIcon,
  CalendarIcon,
  ChartPieIcon,
  Cog6ToothIcon,
  DocumentDuplicateIcon,
  FolderIcon,
  HomeIcon,
  UsersIcon,
  XMarkIcon,
} from "@heroicons/react/24/outline";
import {
  ChevronDownIcon,
  MagnifyingGlassIcon,
} from "@heroicons/react/20/solid";
import { useLocation } from "react-router";

const navigation = [
  { name: "Dashboard", href: "/admin/dashboard", icon: HomeIcon, current: false },
  { name: "Team", href: "/admin/team", icon: UsersIcon, current: true },
];



const userNavigation = [
  { name: "Your profile", href: "#" },
  { name: "Sign out", href: "#" },
];

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

export const SessionLayout = ({ children }) => {

  const [sidebarOpen, setSidebarOpen] = useState(false);

  const location = useLocation();

  const updatedNavigation = navigation.map((item) => ({
    ...item,
    current: location.pathname === item.href, // Marca como activo si la ruta coincide
  }));


  return (
    <>
      <div>
        <Dialog
          open={sidebarOpen}
          onClose={setSidebarOpen}
          className="relative z-50 lg:hidden"
        >
          <DialogBackdrop
            transition
            className="fixed inset-0 bg-gray-900/80 transition-opacity duration-300 ease-linear data-closed:opacity-0"
          />

          <div className="fixed inset-0 flex">
            <DialogPanel
              transition
              className="relative mr-16 flex w-full max-w-xs flex-1 transform transition duration-300 ease-in-out data-closed:-translate-x-full"
            >
              <TransitionChild>
                <div className="absolute top-0 left-full flex w-16 justify-center pt-5 duration-300 ease-in-out data-closed:opacity-0">
                  <button
                    type="button"
                    onClick={() => setSidebarOpen(false)}
                    className="-m-2.5 p-2.5"
                  >
                    <span className="sr-only">Close sidebar</span>
                    <XMarkIcon
                      aria-hidden="true"
                      className="size-6 text-white"
                    />
                  </button>
                </div>
              </TransitionChild>
              {/* Sidebar component, swap this element with another sidebar if you like */}
              <div className="flex grow flex-col gap-y-5 overflow-y-auto bg-gray-900 px-6 pb-4 ring-1 ring-white/10">
                <div className="flex h-16 shrink-0 items-center">
                  <img
                    alt="Your Company"
                    src="https://tailwindui.com/plus-assets/img/logos/mark.svg?color=indigo&shade=500"
                    className="h-8 w-auto"
                  />
                  <span className="text-white text-2xl ml-3 font-bold"> ERP - Globalfleet </span>
                </div>
                <nav className="flex flex-1 flex-col">
                  <ul role="list" className="flex flex-1 flex-col gap-y-7">
                    <li>
                      <ul role="list" className="-mx-2 space-y-1">
                        {updatedNavigation.map((item) => (
                          <li key={item.name}>
                            <a
                              href={item.href}
                              className={classNames(
                                item.current
                                  ? "bg-gray-800 text-white"
                                  : "text-gray-400 hover:bg-gray-800 hover:text-white",
                                "group flex gap-x-3 rounded-md p-2 text-sm/6 font-semibold"
                              )}
                            >
                              <item.icon
                                aria-hidden="true"
                                className="size-6 shrink-0"
                              />
                              {item.name}
                            </a>
                          </li>
                        ))}
                      </ul>
                    </li>

                  </ul>
                </nav>
              </div>
            </DialogPanel>
          </div>
        </Dialog>

        {/* Static sidebar for desktop */}
        <div className="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-72 lg:flex-col">
          {/* Sidebar component, swap this element with another sidebar if you like */}
          <div className="flex grow flex-col gap-y-5 overflow-y-auto bg-gray-900 px-6 pb-4">
            <div className="flex h-16 shrink-0 items-center">
              <img
                alt="Your Company"
                src="https://tailwindui.com/plus-assets/img/logos/mark.svg?color=indigo&shade=500"
                className="h-8 w-auto"
              />
              <span className="text-white text-2xl ml-3 font-bold">ERP - Globalfleet </span>
            </div>
            <nav className="flex flex-1 flex-col">
              <ul role="list" className="flex flex-1 flex-col gap-y-7">
                <li>
                  <ul role="list" className="-mx-2 space-y-1">
                    {updatedNavigation.map((item) => (
                      <li key={item.name}>
                        <a
                          href={item.href}
                          className={classNames(
                            item.current
                              ? "bg-gray-800 text-white"
                              : "text-gray-400 hover:bg-gray-800 hover:text-white",
                            "group flex gap-x-3 rounded-md p-2 text-sm/6 font-semibold"
                          )}
                        >
                          <item.icon
                            aria-hidden="true"
                            className="size-6 shrink-0"
                          />
                          {item.name}
                        </a>
                      </li>
                    ))}
                  </ul>
                </li>
                
              </ul>
            </nav>
          </div>
        </div>

        <div className="lg:pl-72">
          <div className="sticky top-0 z-40 flex h-16 shrink-0 items-center gap-x-4 border-b border-gray-200 bg-white px-4 shadow-xs sm:gap-x-6 sm:px-6 lg:px-8">
            <button
              type="button"
              onClick={() => setSidebarOpen(true)}
              className="-m-2.5 p-2.5 text-gray-700 lg:hidden"
            >
              <span className="sr-only">Open sidebar</span>
              <Bars3Icon aria-hidden="true" className="size-6" />
            </button>

            {/* Separator */}
            <div
              aria-hidden="true"
              className="h-6 w-px bg-gray-900/10 lg:hidden"
            />

            <div className="flex flex-1 gap-x-4 self-stretch lg:gap-x-6">
              <div className="grid flex-1 grid-cols-1"></div>
              <div className="flex items-center gap-x-4 lg:gap-x-6">
                <button
                  type="button"
                  className="-m-2.5 p-2.5 text-gray-400 hover:text-gray-500"
                >
                  <span className="sr-only">View notifications</span>
                  <BellIcon aria-hidden="true" className="size-6" />
                </button>

                {/* Separator */}
                <div
                  aria-hidden="true"
                  className="hidden lg:block lg:h-6 lg:w-px lg:bg-gray-900/10"
                />

                {/* Profile dropdown */}
                <Menu as="div" className="relative">
                  <MenuButton className="-m-1.5 flex items-center p-1.5">
                    <span className="sr-only">Open user menu</span>
                    <img
                      alt=""
                      src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                      className="size-8 rounded-full bg-gray-50"
                    />
                    <span className="hidden lg:flex lg:items-center">
                      <span
                        aria-hidden="true"
                        className="ml-4 text-sm/6 font-semibold text-gray-900"
                      >
                        Tom Cook
                      </span>
                      <ChevronDownIcon
                        aria-hidden="true"
                        className="ml-2 size-5 text-gray-400"
                      />
                    </span>
                  </MenuButton>
                  
                  <MenuItems
                    transition
                    className="absolute right-0 z-10 mt-2.5 w-32 origin-top-right rounded-md bg-white py-2 ring-1 shadow-lg ring-gray-900/5 transition focus:outline-hidden data-closed:scale-95 data-closed:transform data-closed:opacity-0 data-enter:duration-100 data-enter:ease-out data-leave:duration-75 data-leave:ease-in"
                  >
                    {userNavigation.map((item) => (
                      <MenuItem key={item.name}>
                        <a
                          href={item.href}
                          className="block px-3 py-1 text-sm/6 text-gray-900 data-focus:bg-gray-50 data-focus:outline-hidden"
                        >
                          {item.name}
                        </a>
                      </MenuItem>
                    ))}
                  </MenuItems>
                </Menu>
              </div>
            </div>
          </div>

          <main className="py-10">
            <div className="px-4 sm:px-6 lg:px-8">{children}</div>
          </main>
        </div>
      </div>
    </>
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
