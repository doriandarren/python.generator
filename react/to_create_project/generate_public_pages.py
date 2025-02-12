import os

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")



def generate_public_pages(project_path):
    generate_routes(project_path)
    generate_home_page(project_path)
    generate_contact_page(project_path)
    generate_about_page(project_path)


def generate_routes(project_path):
    """
    Genera el archivo AppRoutes.jsx dentro de la carpeta modules/routes.
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "public", "routes")
    file_path = os.path.join(routes_dir, "PublicRoutes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo AppRoutes.jsx
    app_routes_content = """import { Navigate, Route, Routes } from \"react-router\";
import { HomePage } from \"../pages/HomePage\";
import { AboutPage } from \"../pages/AboutPage\";
import { ContactPage } from \"../pages/ContactPage\";
import { HeaderLayout } from \"../../../layouts/components/HeaderLayout\";
import { FooterLayout } from \"../../../layouts/components/FooterLayout\";


export const PublicRoutes = () => {
  return (
    <>

      <HeaderLayout />

      <Routes>

        <Route path=\"/home\" element={<HomePage />} />
        <Route path=\"/about\" element={<AboutPage />} />
        <Route path=\"/contact\" element={<ContactPage />} />

        {/* <Route path=\"/*\" element={ <LoginPage /> } /> */}
        <Route path=\"/*\" element={ <Navigate to=\"/auth/login\" /> } />

      </Routes>

      <FooterLayout />

    </>
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
    home_page_content = """import { Button } from "../../../layouts/components/Button";
import { Section } from "../../../layouts/components/Section";

export const ContactPage = () => {
  return (
    <>
      <Section
        title="Contact Us"
        subtitle="We'd love to hear from you!"
        className="bg-gray-100"
      >
        <div className="contact__grid">
          {/* Formulario de Contacto */}
          <form className="contact__form">
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                id="name"
                name="name"
                placeholder="Your name"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                placeholder="Your email"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="message">Message</label>
              <textarea
                id="message"
                name="message"
                placeholder="Your message"
                required
              ></textarea>
            </div>

            <Button
              variant="secondary"
              onClick={() => alert("Primary Button Clicked!")}
            >
              <span>Hola</span>
            </Button>
          </form>

          {/* Información de Contacto */}
          <div className="contact__info">
            <p>
              <strong>📍 Address:</strong> 1234 Street Name, City, Country
            </p>
            <p>
              <strong>📞 Phone:</strong> +1 234 567 890
            </p>
            <p>
              <strong>✉ Email:</strong> contact@nucleus.com
            </p>
          </div>
        </div>
      </Section>
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


def generate_about_page(project_path):
    """
    Genera el archivo AboutPage.jsx dentro de la carpeta modules/public/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "public", "pages")
    file_path = os.path.join(pages_dir, "AboutPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo AboutPage.jsx
    home_page_content = """import { Section } from "../../../layouts/components/Section";

export const AboutPage = () => {
  return (
    <>
      <Section
        title="Quiénes Somos"
        subtitle="Conoce más sobre nuestra misión y valores"
        className="bg-gray-100"
      >
        <div className="about__grid">
          
          {/* Contenido sobre la empresa */}
          <div className="about__content">
            <p>
              En <strong>Nucleus</strong>, creemos en el poder de la tecnología
              para simplificar las transacciones financieras. Nuestra misión es
              ofrecer soluciones seguras, rápidas y confiables para la gestión
              de pagos, ahorros e inversiones.
            </p>
            <p>
              Con un equipo de profesionales dedicados y tecnología de
              vanguardia, nos esforzamos por crear un ecosistema donde la
              libertad financiera sea accesible para todos.
            </p>

            <div className="about__values">
              <div className="about__value">
                <h3>🔒 Seguridad</h3>
                <p>
                  Tu información financiera está protegida con los más altos
                  estándares.
                </p>
              </div>

              <div className="about__value">
                <h3>🚀 Innovación</h3>
                <p>
                  Mejoramos continuamente nuestra plataforma con las últimas
                  tecnologías.
                </p>
              </div>

              <div className="about__value">
                <h3>🤝 Confianza</h3>
                <p>
                  Construimos relaciones transparentes con nuestros clientes y
                  socios.
                </p>
              </div>
            </div>
          </div>
        </div>
      </Section>
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


