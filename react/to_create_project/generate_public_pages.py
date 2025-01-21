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
    home_page_content = """export const HomePage = () => {
  return (
    <>
      <header className="header">
          <div className="header__container">
              <div className="header__grid">
                  <div className="header__text">
                      <h1 className="header__heading">Recibe y realiza pagos en tu móvil con nucleus</h1>
                      <a className="header__button" href="#">Obtener cuenta</a>
                  </div>
                  <div className="header__grafico">
                      <img className="header__image" src={app1} alt="imagen nucleus app" />
                  </div>
              </div>
          </div>
      </header>


      <section className="bg-primary-dark text-white py-16">
        <div className="container mx-auto text-center px-6">
          <h2 className="text-4xl font-bold mb-4">Bienvenido a Nucleus</h2>
          <p className="text-lg mb-6">Creamos soluciones específicas para tus necesidades.</p>
          <a
            href="#"
            className="bg-white text-primary-dark font-medium py-3 px-6 rounded-lg shadow-md hover:bg-gray-100 transition duration-300"
          >
            Contáctanos
          </a>
        </div>
      </section>



      <div className="card card--featured bg-yellow-100 border-yellow-500">
        <h2 className="card__title text-2xl font-bold text-gray-800">Título Destacado</h2>
        <p className="card__description text-gray-600">
          Este es el contenido destacado de la tarjeta.
        </p>
        <button className="btn btn-primary">
          Leer Más
        </button>
      </div>


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