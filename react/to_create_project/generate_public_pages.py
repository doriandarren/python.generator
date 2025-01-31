import os

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")



def generate_pages(project_path):
    generate_home_page(project_path)
    generate_contact_page(project_path)
    generate_about_page(project_path)



def generate_home_page(project_path):
    """
    Genera el archivo HomePage.jsx dentro de la carpeta modules/public/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "public", "pages")
    file_path = os.path.join(pages_dir, "HomePage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo HomePage.jsx
    home_page_content = """import app1 from "../../../assets/images/app_1.svg";

export const HomePage = () => {
  return (
    <>
      <main className="main">
        <div className="main__container">
          <div className="main__grid">
            <div className="main__text">
              <h1 className="main__heading">
                Recibe y realiza pagos en tu móvil con nucleus
              </h1>
              <a className="main__button" href="#">
                Obtener cuenta
              </a>
            </div>
            <div className="main__graphic">
              <img
                className="main__image"
                src={app1}
                alt="imagen nucleus app"
              />
            </div>
          </div>
        </div>
      </main>

      <section className="nucleus">
        <h2 className="nucleus__heading">¿Qué es?</h2>
        <div className="nucleus__container">
          <div className="nucleus__grid">
            <div className="list__item">
              <h2 className="list__heading">Fácil</h2>
              <p className="list__text">
                Crea una cuenta, envía tu documentación y comienza a utilizar
                nucleus en un par de horas
              </p>
            </div>

            <div className="list__item">
              <h2 className="list__heading">Seguro</h2>
              <p className="list__text">
                Por su tecnología digital nucleus es imposible de hackear o
                robar
              </p>
            </div>

            <div className="list__item">
              <h2 className="list__heading">Administrable</h2>
              <p className="list__text">
                Añade o tranfiere fondos a tu banco, añade limites o controla
                tus gastos
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="commissions">
        <div className="commissions__container">
          <h2 className="commissions__heading">Comisiones</h2>

          <div className="commissions__grid">
            <div className="commissions__content">
              <p className="commissions__text">
                The more you use Nucleus, the less you pay:
              </p>

              <div className="list">
                <div className="list__item list__item--2col">
                  <p className="list__number">3%</p>
                  <p className="list__text">
                    de todas tus transacciones si tus movimientos son menores a $999 USD
                  </p>
                </div>

                <div className="list__item list__item--2col">
                  <p className="list__number">2.5%</p>
                  <p className="list__text">
                    de todas tus transacciones si tus movimientos son mayores a $999 USD.
                  </p>
                </div>
              </div>
            </div>

            <div className="commissions__image">
              {/* <img src="img/app_3.svg" alt="App image" /> */}
            </div>
          </div>
        </div>
      </section>
    </>
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


def generate_contact_page(project_path):
    """
    Genera el archivo HomePage.jsx dentro de la carpeta modules/public/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "public", "pages")
    file_path = os.path.join(pages_dir, "ContactPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo HomePage.jsx
    home_page_content = """export const ContactPage = () => {
  return (
    <>
      {/* Hero Section */}
      <section className="text-center py-16 bg-gradient-to-r from-primary to-secondary text-white p-8 rounded">
        <h2 className="text-black text-4xl font-bold mb-4">Acerca de Nosotros</h2>
        <p className="text-lg">Conoce más sobre nuestra misión, visión y equipo.</p>
      </section>

      {/* About Content */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <h3 className="text-3xl font-semibold text-center mb-8 text-primary-dark">Nuestra Historia</h3>
          <p className="text-lg text-neutral-dark text-center mb-12">
            En <span className="font-bold text-primary">Famindex</span>, creemos en el poder del software personalizado. Desde nuestros inicios, nos hemos dedicado a ofrecer soluciones a medida que se adaptan a las necesidades específicas de cada cliente.
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="p-6 bg-neutral-light rounded-lg shadow">
              <h4 className="text-xl font-bold mb-2 text-primary">Nuestra Misión</h4>
              <p>
                Ayudar a las empresas a alcanzar sus objetivos mediante software innovador y adaptado a sus necesidades.
              </p>
            </div>
            <div className="p-6 bg-neutral-light rounded-lg shadow">
              <h4 className="text-xl font-bold mb-2 text-primary">Nuestra Visión</h4>
              <p>
                Ser líderes en desarrollo de software a medida, reconocidos por nuestra excelencia técnica y atención al cliente.
              </p>
            </div>
          </div>
        </div>
      </section>
    </>
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


def generate_about_page(project_path):
    """
    Genera el archivo HomePage.jsx dentro de la carpeta modules/public/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "public", "pages")
    file_path = os.path.join(pages_dir, "AboutPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo HomePage.jsx
    home_page_content = """export const AboutPage = () => {
  return (
    <>
      {/* Hero Section */}
      <section className="text-center py-16 bg-gradient-to-r from-primary to-secondary text-white p-8 rounded">
        <h2 className="text-black text-4xl font-bold mb-4">Acerca de Nosotros</h2>
        <p className="text-lg">Conoce más sobre nuestra misión, visión y equipo.</p>
      </section>

      {/* About Content */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <h3 className="text-3xl font-semibold text-center mb-8 text-primary-dark">Nuestra Historia</h3>
          <p className="text-lg text-neutral-dark text-center mb-12">
            En <span className="font-bold text-accent">Famindex</span>, creemos en el poder del software personalizado. Desde nuestros inicios, nos hemos dedicado a ofrecer soluciones a medida que se adaptan a las necesidades específicas de cada cliente.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Misión */}
            <div className="p-6 bg-neutral-light rounded-lg shadow">
              <h4 className="text-xl font-bold mb-2 text-primary">Nuestra Misión</h4>
              <p>
                Ayudar a las empresas a alcanzar sus objetivos mediante software
                innovador y adaptado a sus necesidades.
              </p>
            </div>

            {/* Visión */}
            <div className="p-6 bg-neutral-light rounded-lg shadow">
              <h4 className="text-xl font-bold mb-2 text-primary">Nuestra Visión</h4>
              <p>
                Ser líderes en desarrollo de software a medida, reconocidos por
                nuestra excelencia técnica y atención al cliente.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Team Section */}
      <section className="py-16 bg-neutral-light">
        <div className="container mx-auto px-4">
          <h3 className="text-3xl font-semibold text-center mb-8 text-primary-dark">Nuestro Equipo</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Team Member */}
            <div className="text-center">
              <div className="w-24 h-24 mx-auto mb-4 rounded-full bg-primary-light"></div>
              <h4 className="text-lg font-bold">Milena Aguilar</h4>
              <p className="text-sm text-neutral-dark">CEO y Desarrolladora Principal</p>
            </div>

            {/* Placeholder Team Members */}
            <div className="text-center">
              <div className="w-24 h-24 mx-auto mb-4 rounded-full bg-primary-light"></div>
              <h4 className="text-lg font-bold">Nombre Miembro</h4>
              <p className="text-sm text-neutral-dark">Rol del Equipo</p>
            </div>
            <div className="text-center">
              <div className="w-24 h-24 mx-auto mb-4 rounded-full bg-primary-light"></div>
              <h4 className="text-lg font-bold">Nombre Miembro</h4>
              <p className="text-sm text-neutral-dark">Rol del Equipo</p>
            </div>
          </div>
        </div>
      </section>
    </>
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