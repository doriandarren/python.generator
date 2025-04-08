import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_components(full_path):
    #Btn
    create_button(full_path)

    # Section
    create_section(full_path)

    # Preloader
    create_preloader_svg(full_path)
    create_preloader(full_path)
    create_preloader_main(full_path)
    create_preloader_main_css(full_path)
    create_preloader_button(full_path)


    #DataTable
    create_datatable(full_path)


    ##ComboBoxes
    create_combobox(full_path)
    create_toggle_button(full_path)


    create_badges(full_path)







def create_button(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "Buttons")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "Button.jsx")

    # Contenido por defecto
    content = """import classNames from "classnames";

export const Button = ({ children, type = "button", variant = "primary", onClick, className, disabled = false }) => {
  return (
    <button
      type={type}
      className={classNames(
        "py-2 px-4 w-full xl:w-32 xl:mr-3 rounded-md text-white font-semibold transition-all duration-200",
        {
          "bg-primary hover:bg-primary-dark": !disabled && variant === "primary",
          "bg-gray-400 cursor-not-allowed": disabled,
          "bg-danger hover:bg-danger-dark": !disabled && variant === "danger",
          "bg-secondary hover:bg-secondary-dark": !disabled && variant === "secondary",
          "bg-success hover:bg-success-dark": !disabled && variant === "success",
        },
        className
      )}
      onClick={!disabled ? onClick : undefined}
      disabled={disabled}
    >
      {children}
    </button>
  );
};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_section(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "Sections")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "Section.jsx")

    # Contenido por defecto
    content = """import classNames from "classnames";

export const Section = ({title, subtitle, className, children}) => {
  return (
    <section className={classNames("section", className)}>
        <div className="section__container">
        {title && <h2 className="section__heading">{title}</h2>}
        {subtitle && <p className="section__subtitle">{subtitle}</p>}
        {children}
        </div>
    </section>
  )
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_preloader_svg(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "Preloader")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "PreloaderSVG.jsx")

    # Contenido por defecto
    content = """export const PreloaderSVG = () => {
  return (
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M2,12A10.94,10.94,0,0,1,5,4.65c-.21-.19-.42-.36-.62-.55h0A11,11,0,0,0,12,23c.34,0,.67,0,1-.05C6,23,2,17.74,2,12Z"><animateTransform attributeName="transform" dur="0.6s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>
    )
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_preloader(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "Preloader")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "Preloader.jsx")

    # Contenido por defecto
    content = """import { PreloaderSVG } from "./PreloaderSVG"

export const Preloader = () => {
    return (
        <div className="flex justify-center">
            <PreloaderSVG />  
        </div>
    )
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_preloader_main(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "Preloader")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "PreloaderMain.jsx")

    # Contenido por defecto
    content = """import { PreloaderSVG } from "./PreloaderSVG";
import "./PreloaderMain.css";

export const PreloaderMain = () => {
  return (
    <div className="preloader flex justify-center">
      <PreloaderSVG />   
    </div>
  )
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_preloader_main_css(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "Preloader")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "PreloaderMain.css")

    # Contenido por defecto
    content = """.preloader {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 9999;
}

.loader {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_datatable(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "DataTables")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "DataTable.jsx")

    # Contenido por defecto
    content = r"""import { useState } from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import { Pencil, Trash2, ChevronUp, ChevronDown, Search } from "lucide-react";
import { useTranslation } from "react-i18next";

export const Datatable = ({
  columns,
  data,
  editPath = "",
  onDelete,
  onEdit = () => {},
}) => {
  const { t } = useTranslation();

  const defaultItemPerPage = 10;

  const showActions = !!editPath || typeof onDelete === "function";

  const [searchQuery, setSearchQuery] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage, setItemsPerPage] = useState(defaultItemPerPage);
  const [sortColumn, setSortColumn] = useState(null);
  const [sortDirection, setSortDirection] = useState(null);


  const getNestedValue = (obj, path) => {
    return path.split(".").reduce((acc, part) => acc?.[part], obj);
  };


  // Filtrar datos por búsqueda
  const filteredData = data.filter((row) =>
    columns.some((column) => {
      const value = column.render
        ? column.render(row)
        : getNestedValue(row, column.key);
      return value
        ?.toString()
        .toLowerCase()
        .includes(searchQuery.toLowerCase());
    })
  );

  // Ordenar datos
  const sortedData = [...filteredData];
  if (sortColumn) {
    sortedData.sort((a, b) => {
      const valueA = a[sortColumn] || "";
      const valueB = b[sortColumn] || "";

      if (typeof valueA === "number" && typeof valueB === "number") {
        return sortDirection === "asc" ? valueA - valueB : valueB - valueA;
      }

      return sortDirection === "asc"
        ? valueA.toString().localeCompare(valueB.toString())
        : valueB.toString().localeCompare(valueA.toString());
    });
  }

  // Paginación
  const totalRecords = sortedData.length;
  const totalPages = Math.ceil(totalRecords / itemsPerPage);
  const indexOfFirstItem = (currentPage - 1) * itemsPerPage;
  const indexOfLastItem = Math.min(
    indexOfFirstItem + itemsPerPage,
    totalRecords
  );
  const currentItems = sortedData.slice(indexOfFirstItem, indexOfLastItem);

  // Manejar orden de columnas
  const handleSort = (columnKey) => {
    if (sortColumn === columnKey) {
      setSortDirection(sortDirection === "asc" ? "desc" : "asc");
    } else {
      setSortColumn(columnKey);
      setSortDirection("asc");
    }
  };

  // Generar paginación con "..."
  const generatePaginationRange = () => {
    const range = [];
    if (totalPages <= 6) {
      for (let i = 1; i <= totalPages; i++) range.push(i);
    } else {
      range.push(1);
      let startPage = Math.max(2, currentPage - 2);
      let endPage = Math.min(totalPages - 1, currentPage + 2);

      if (startPage > 2) range.push("...");
      for (let i = startPage; i <= endPage; i++) range.push(i);
      if (endPage < totalPages - 1) range.push("...");
      range.push(totalPages);
    }
    return range;
  };



  return (
    <div className="w-full border-2 border-gray-100 shadow-xl rounded-xl overflow-hidden p-4">
      {/* Barra de búsqueda con lupa */}
      <div className="flex flex-col sm:flex-row justify-between items-center mb-4 gap-3">
        <div className="relative w-full sm:w-auto">
          <Search className="absolute left-3 top-2.5 text-gray-500 w-5 h-5" />
          <input
            type="text"
            placeholder={t("search")}
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full sm:w-64 pl-10 pr-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary focus:border-primary-dark sm:text-sm"
          />
        </div>
      </div>

      {/* Tabla */}
      <div className="overflow-x-auto rounded-xl">
        <table className="min-w-full w-full divide-y divide-gray-300">
          <thead className="bg-gray-100">
            <tr>
              {columns.map((column) => (
                <th
                  key={column.key}
                  className="px-4 py-3 text-left text-sm font-semibold text-gray-900 cursor-pointer"
                  onClick={() => handleSort(column.key)}
                >
                  <div className="flex items-center gap-1">
                    {column.label}
                    {sortColumn === column.key &&
                      (sortDirection === "asc" ? (
                        <ChevronUp className="w-4 h-4" />
                      ) : (
                        <ChevronDown className="w-4 h-4" />
                      ))}
                  </div>
                </th>
              ))}

              {showActions && (
                <th className="px-4 py-3 text-left text-sm font-semibold text-gray-900">
                  {t("actions")}
                </th>
              )}              
            </tr>
          </thead>
          <tbody className="bg-white">
            {currentItems.length > 0 ? (
              currentItems.map((item, index) => {
                const rowKey =
                  item.id && !isNaN(item.id)
                    ? `row-${item.id}`
                    : `row-${index}`;

                return (
                  <tr key={rowKey} className="even:bg-gray-50">
                    {columns.map((column) => (
                      <td
                        key={`${column.key}-${rowKey}`}
                        className="px-4 py-4 text-sm whitespace-nowrap text-gray-500"
                      >
                        {column.render ? column.render(item) : getNestedValue(item, column.key) ?? "-"}
                      </td>
                    ))}
                    
                    {showActions && (
                      <td className="px-4 py-4 text-sm whitespace-nowrap">
                        <div className="flex gap-5">

                          {editPath && (
                            <Link
                              to={`${editPath}/edit/${item.id}`}
                              className="text-primary hover:text-primary-dark"
                              onClick={() => onEdit(item.id)}
                            >
                              <Pencil className="w-5 h-5" />
                            </Link>
                          )}

                          {typeof onDelete === "function" && (
                            <button
                              onClick={() => onDelete(item.id)}
                              className="text-red-600 hover:text-red-800"
                            >
                              <Trash2 className="w-5 h-5" />
                            </button>
                          )}                  
                          
                        </div>
                      </td>
                    )} 
                  </tr>
                );
              })
            ) : (
              <tr key="no-data">
                <td
                  colSpan={columns.length + (showActions ? 1 : 0)}
                  className="text-center py-4 text-gray-500"
                >
                  {t("no_results_found")}
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {/* Paginación y selección de registros */}
      <div className="flex flex-col sm:flex-row justify-between items-center mt-4 gap-3">
        <div className="flex items-center">
          <span className="text-sm text-gray-700 mr-2">{t("show")}</span>
          <select
            className="border border-gray-300 rounded-md px-2 py-1 text-sm"
            value={itemsPerPage}
            onChange={(e) => {
              setItemsPerPage(Number(e.target.value));
              setCurrentPage(1);
            }}
          >
            {[5, 10, 50, 100].map((num) => (
              <option key={num} value={num}>
                {num}
              </option>
            ))}
          </select>
          <span className="text-gray-500 ml-2">
            {indexOfFirstItem + 1} - {indexOfLastItem} de {totalRecords}
          </span>
        </div>

        <div className="flex items-center gap-2">
          <button
            disabled={currentPage === 1}
            onClick={() => setCurrentPage(currentPage - 1)}
            className="px-3 py-2 text-sm rounded-md bg-gray-300 hover:bg-gray-400 disabled:opacity-50"
          >
            {t("back")}
          </button>
          {generatePaginationRange().map((page, index) => (
            <button
              key={index}
              onClick={() => typeof page === "number" && setCurrentPage(page)}
              className={`px-3 py-2 text-sm rounded-md ${
                currentPage === page
                  ? "bg-primary text-white"
                  : "bg-gray-200 hover:bg-gray-300"
              }`}
              disabled={page === "..."}
            >
              {page}
            </button>
          ))}
          <button
            disabled={currentPage === totalPages}
            onClick={() => setCurrentPage(currentPage + 1)}
            className="px-3 py-2 text-sm rounded-md bg-gray-300 hover:bg-gray-400 disabled:opacity-50"
          >
            {t("next")}
          </button>
        </div>
      </div>
    </div>
  );
};

// Definición de `PropTypes`
Datatable.propTypes = {
  columns: PropTypes.arrayOf(
    PropTypes.shape({
      key: PropTypes.string.isRequired,
      label: PropTypes.string.isRequired,
      render: PropTypes.func // <-- Agregado
    })
  ).isRequired,
  data: PropTypes.arrayOf(PropTypes.object).isRequired,
  editPath: PropTypes.string,
  onDelete: PropTypes.func,
  onEdit: PropTypes.func,
};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_preloader_button(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "Preloader")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "PreloaderButton.css")

    # Contenido por defecto
    content = """import { PreloaderSVG } from "./PreloaderSVG"

export const PreloaderButton = () => {
    return (
        <div className="w-8 h-8">
            <PreloaderSVG />  
        </div>
    )
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_combobox(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "ComboBoxes")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "ComboBox.php")

    # Contenido por defecto
    content = r""""use client";

import {
  Combobox,
  ComboboxButton,
  ComboboxInput,
  ComboboxOption,
  ComboboxOptions,
} from "@headlessui/react";
import { CheckIcon, ChevronUpDownIcon } from "@heroicons/react/20/solid";
import { useState } from "react";

// CustomCombobox.jsx

export default function CustomCombobox({
  label = "Select an option",
  options = [],
  selected,
  setSelected,
  onChange,
  error,
  getLabel = (item) => item?.name, // 👈 nuevo prop con fallback
}) {
  const [query, setQuery] = useState("");

  const filteredOptions =
    query === ""
      ? options
      : options.filter((item) =>
          getLabel(item).toLowerCase().includes(query.toLowerCase())
        );

  return (
    <div>
      <label className="block text-gray-700">{label}</label>
      <Combobox
        autoComplete="off"
        value={selected}
        onChange={(value) => {
          setQuery("");
          setSelected(value);
          onChange?.(value);
        }}
      >
        <div className="relative">
          <ComboboxInput
            autoComplete="off"
            className={`block w-full rounded-md bg-white py-2.5 pr-12 pl-3 text-base text-gray-900 outline-1 placeholder:text-gray-400 sm:text-sm ${
              error
                ? "border border-danger"
                : "outline-gray-300 focus:outline-indigo-600"
            }`}
            onChange={(e) => setQuery(e.target.value)}
            onBlur={() => setQuery("")}
            displayValue={(item) => getLabel(item)}
          />
          <ComboboxButton className="absolute inset-y-0 right-0 flex items-center px-2">
            <ChevronUpDownIcon className="size-5 text-gray-400" />
          </ComboboxButton>

          {filteredOptions.length > 0 && (
            <ComboboxOptions className="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm">
              {filteredOptions.map((item) => (
                <ComboboxOption
                  key={item.id}
                  value={item}
                  className="group relative cursor-default select-none py-2 pl-3 pr-9 text-gray-900 data-focus:bg-indigo-600 data-focus:text-white"
                >
                  <span className="block truncate group-data-selected:font-semibold">
                    {getLabel(item)}
                  </span>

                  <span className="absolute inset-y-0 right-0 hidden items-center pr-4 text-indigo-600 group-data-focus:text-white group-data-selected:flex">
                    <CheckIcon className="size-5" aria-hidden="true" />
                  </span>
                </ComboboxOption>
              ))}
            </ComboboxOptions>
          )}
        </div>
      </Combobox>
      {error && <p className="text-danger text-sm mt-1">{error}</p>}
    </div>
  );
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_toggle_button(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "Toggles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "ToggleButton.php")

    # Contenido por defecto
    content = r"""'use client'

import { Switch } from '@headlessui/react'

export default function ToggleButton({
  label,
  enabled,
  setEnabled,
  error,
}) {
  return (
    <div>
      {label && (
        <label className="block text-gray-700 mb-1">{label}</label>
      )}
      <Switch
        checked={enabled}
        onChange={setEnabled}
        className={`group relative inline-flex h-6 w-11 shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2 focus:outline-hidden ${
          enabled ? 'bg-indigo-600' : 'bg-gray-200'
        }`}
      >
        <span className="sr-only">{label ?? 'Toggle setting'}</span>
        <span
          className={`pointer-events-none relative inline-block size-5 transform rounded-full bg-white ring-0 shadow-sm transition duration-200 ease-in-out ${
            enabled ? 'translate-x-5' : 'translate-x-0'
          }`}
        >
          {/* Iconos */}
          <span
            aria-hidden="true"
            className={`absolute inset-0 flex size-full items-center justify-center transition-opacity duration-200 ease-in ${
              enabled ? 'opacity-0 duration-100 ease-out' : 'opacity-100'
            }`}
          >
            <svg fill="none" viewBox="0 0 12 12" className="size-3 text-gray-400">
              <path
                d="M4 8l2-2m0 0l2-2M6 6L4 4m2 2l2 2"
                stroke="currentColor"
                strokeWidth={2}
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </span>
          <span
            aria-hidden="true"
            className={`absolute inset-0 flex size-full items-center justify-center transition-opacity duration-200 ease-in ${
              enabled ? 'opacity-100' : 'opacity-0'
            }`}
          >
            <svg fill="currentColor" viewBox="0 0 12 12" className="size-3 text-indigo-600">
              <path d="M3.707 5.293a1 1 0 00-1.414 1.414l1.414-1.414zM5 8l-.707.707a1 1 0 001.414 0L5 8zm4.707-3.293a1 1 0 00-1.414-1.414l1.414 1.414zm-7.414 2l2 2 1.414-1.414-2-2-1.414 1.414zm3.414 2l4-4-1.414-1.414-4 4 1.414 1.414z" />
            </svg>
          </span>
        </span>
      </Switch>
      {error && (
        <p className="text-danger text-sm mt-1">{error}</p>
      )}
    </div>
  )
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_badges(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "components", "Badges")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "Badge.php")

    # Contenido por defecto
    content = r"""const colorMap = {
  gray: "bg-gray-100 text-gray-600",
  red: "bg-red-100 text-red-700",
  yellow: "bg-yellow-100 text-yellow-800",
  green: "bg-green-100 text-green-700",
  blue: "bg-blue-100 text-blue-700",
  indigo: "bg-indigo-100 text-indigo-700",
  purple: "bg-purple-100 text-purple-700",
  pink: "bg-pink-100 text-pink-700",
};

export const Badge = ({ text, color = "gray" }) => {
  const colorClasses = colorMap[color] || colorMap.gray;

  return (
    <span
      className={`inline-flex items-center rounded-full px-2 py-1 text-xs font-medium ${colorClasses}`}
    >
      {text}
    </span>
  );
};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

