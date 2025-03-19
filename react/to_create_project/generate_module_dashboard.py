import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command, create_folder




def generate_module_dashboard(project_path):
    install_recharts(project_path)

    create_routes(project_path)
    create_dashboard_page(project_path)
    create_profile_page(project_path)




def install_recharts(project_path):
    """Installation."""
    print_message("Instalando Recharts...", CYAN)
    run_command("npm install recharts", cwd=project_path)
    print_message("Recharts instalado correctamente.", GREEN)


def create_routes(project_path):
    """
    Genera el archivo AppRoutes.jsx dentro de la carpeta modules/routes.
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "dashboard", "routes")
    file_path = os.path.join(routes_dir, "DashboardRoutes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo jsx
    app_routes_content = """import { Navigate, Route, Routes } from "react-router";
import { DashboardPage } from "../pages/DashboardPage";


export const DashboardRoutes = () => {
  return (
    <Routes>
      
      <Route path="/" element={ <DashboardPage /> } />
      
      
      <Route path="/*" element={ <Navigate to="/admin/dashboard" /> } />
      
    </Routes>
  )
}

"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def create_dashboard_page(project_path):
    """
    Genera el archivo jsx dentro de la carpeta modules/dashboard/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "dashboard", "pages")
    file_path = os.path.join(pages_dir, "DashboardPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    home_page_content = """import { useTranslation } from "react-i18next";
import { SessionLayout } from "../../../layouts/private/SessionLayout";

import {
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  AreaChart,
  Area,
} from "recharts";

const data = [
  {
    name: "Page A",
    uv: 4000,
    pv: 2400,
    amt: 2400,
  },
  {
    name: "Page B",
    uv: 3000,
    pv: 1398,
    amt: 2210,
  },
  {
    name: "Page C",
    uv: 2000,
    pv: 9800,
    amt: 2290,
  },
  {
    name: "Page D",
    uv: 2780,
    pv: 3908,
    amt: 2000,
  },
  {
    name: "Page E",
    uv: 1890,
    pv: 4800,
    amt: 2181,
  },
  {
    name: "Page F",
    uv: 2390,
    pv: 3800,
    amt: 2500,
  },
  {
    name: "Page G",
    uv: 3490,
    pv: 4300,
    amt: 2100,
  },
];

export const DashboardPage = () => {
  
  const { t } = useTranslation();

  return (
    <SessionLayout>
      
      <div>
        <h2 className="text-2xl font-bold text-gray-800 mb-4">
          { t("dashboard") }
        </h2>
      </div>

      {/* Contenedor de las 3 Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        {/* Card 1 */}
        <div className="bg-white p-6 rounded-lg shadow-md flex justify-between mt-5 mr-5 bg-gradient-to-b from-gray-300/10 transition-ransform duration-300 hover:scale-105">
          <div>
            <h3 className="text-lg font-semibold text-gray-600">Total Ventas</h3>
            <small className="text-gray-500">{t("yesterday")}</small>
          </div>
          <div>
            <p className="text-3xl font-bold text-primary">$12.500</p>
          </div>
        </div>

        {/* Card 2 */}
        <div className="bg-white p-6 rounded-lg shadow-md flex justify-between mt-5 mr-5 bg-gradient-to-b from-gray-300/10 transition-ransform duration-300 hover:scale-105">
          <div>
            <h3 className="text-lg font-semibold text-gray-600">Clientes Nuevos</h3>
            <small className="text-gray-500">{t("yesterday")}</small>
          </div>
          <div>
            <p className="text-3xl font-bold text-success">320</p>
          </div>
        </div>

        {/* Card 3 */}
        <div className="bg-white p-6 rounded-lg shadow-md flex justify-between mt-5 mr-5 bg-gradient-to-b from-gray-300/10 transition-ransform duration-300 hover:scale-105">
          <div>
            <h3 className="text-lg font-semibold text-gray-600">Pedidos Totales</h3>
            <small className="text-gray-500">{t("yesterday")}</small>
          </div>
          <div>
            <p className="text-3xl font-bold text-info">870</p>
          </div>
        </div>
      </div>

      <div className="bg-white p-6 rounded-lg shadow-lg">
        <ResponsiveContainer width="100%" height={300}>
          <AreaChart
            data={data}
            margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
          >
            <defs>
              <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8} />
                <stop offset="95%" stopColor="#8884d8" stopOpacity={0} />
              </linearGradient>
              <linearGradient id="colorPv" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#82ca9d" stopOpacity={0.8} />
                <stop offset="95%" stopColor="#82ca9d" stopOpacity={0} />
              </linearGradient>
            </defs>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid strokeDasharray="3 3" />
            <Tooltip />
            <Area
              type="monotone"
              dataKey="uv"
              stroke="#8884d8"
              fillOpacity={1}
              fill="url(#colorUv)"
            />
            <Area
              type="monotone"
              dataKey="pv"
              stroke="#82ca9d"
              fillOpacity={1}
              fill="url(#colorPv)"
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </SessionLayout>
  );
};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(home_page_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def create_profile_page(project_path):
    """
    Genera el archivo jsx dentro de la carpeta modules/dashboard/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "dashboard", "pages")
    file_path = os.path.join(pages_dir, "ProfilePage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    home_page_content = """import { useTranslation } from "react-i18next"
import { SessionLayout } from "../../../layouts/private/SessionLayout"
import { useState } from "react";
import { Button } from "../../../components/Buttons/Button";
import { useNavigate } from "react-router-dom";

export const ProfilePage = () => {

  const navigate = useNavigate();

  const {t} = useTranslation();

  const [formData, setFormData] = useState({
    name: "",
    title: "",
    email: "",
    role: "",
  });
  
  // Manejar cambios en el formulario
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const onSubmit = (e) => {
    e.preventDefault();
    //dispatch(addUser(formData)); 
    navigate("/admin/team");
  };

  const onClickCancel = (e) => {
    e.preventDefault();
    navigate("/admin/team"); 
  }

  return (
    <SessionLayout>

      <div className="max-w-3xl mx-auto mt-10 p-6 bg-white rounded-lg shadow-lg">
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">
          {t("add")}
        </h2>
        <form onSubmit={onSubmit} className="space-y-4">
          {/* Nombre */}
          <div>
            <label className="block text-gray-700">Nombre</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              className="w-full p-2 border border-gray-300 rounded-md"
            />
          </div>

          {/* Cargo */}
          <div>
            <label className="block text-gray-700">Título</label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              required
              className="w-full p-2 border border-gray-300 rounded-md"
            />
          </div>

          {/* Correo Electrónico */}
          <div>
            <label className="block text-gray-700">Correo Electrónico</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="w-full p-2 border border-gray-300 rounded-md"
            />
          </div>

          {/* Rol */}
          <div>
            <label className="block text-gray-700">Rol</label>
            <select
              name="role"
              value={formData.role}
              onChange={handleChange}
              required
              className="w-full p-2 border border-gray-300 rounded-md"
            >
              <option value="">Selecciona un rol</option>
              <option value="Admin">Admin</option>
              <option value="Manager">Manager</option>
              <option value="User">User</option>
            </select>
          </div>

          {/* Botón de Crear */}
          <div className="flex justify-end">
            <div>
              <Button type="submit">{t("save")}</Button>
            </div>

            <div>
              <Button
                variant="danger"
                onClick={onClickCancel}
              >
                {t("cancel")}
              </Button>
            </div>

          </div>

        </form>
      </div>
      
    </SessionLayout>
  )
}
"""
    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(home_page_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")
