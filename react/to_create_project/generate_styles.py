import os

from .utils import print_message, GREEN, CYAN, run_command


def generate_styles(full_path):
    generate_tailwind(full_path)
    generate_tailwind_styles(full_path, "globals.css")
    generate_css_styles(full_path, "styles.css")
    generate_normalize_styles(full_path, "normalize.css")
    generate_scss(full_path, "style.scss")




def generate_tailwind(full_path):
    """Instala y configura Tailwind CSS."""
    print_message("Instalando Tailwind CSS...", CYAN)
    run_command("npm install tailwindcss @tailwindcss/postcss postcss", cwd=full_path)

    tailwind_config = """const config = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
export default config;
"""


    # Configurar tailwind.config.js
#     tailwind_config = """\
# /** @type {import('tailwindcss').Config} */
# export default {
#   content: [
#     "./index.html",
#     "./src/**/*.{js,ts,jsx,tsx}", // Asegúrate de incluir las extensiones que uses
#   ],
#   theme: {
#     extend: {
#       fontFamily: {
#         'sans': ['Lato', 'sans-serif'], // Usar Lato como fuente sans
#       },
#       colors: {
#         primary: {
#           DEFAULT: '#4f9da6', // Color sólido principal
#           light: '#7dbdc8',
#           dark: '#35757d',
#           alpha10: 'rgba(79, 157, 166, 0.1)', // Transparencia 10%
#           alpha30: 'rgba(79, 157, 166, 0.3)', // Transparencia 30%
#           alpha50: 'rgba(79, 157, 166, 0.5)', // Transparencia 50%
#           alpha70: 'rgba(79, 157, 166, 0.7)', // Transparencia 70%
#           alpha90: 'rgba(79, 157, 166, 0.9)', // Transparencia 90%
#         },
#         secondary: {
#           DEFAULT: '#78c800',
#           light: '#a4e542',
#           dark: '#569300',
#           alpha10: 'rgba(120, 200, 0, 0.1)',
#           alpha30: 'rgba(120, 200, 0, 0.3)',
#           alpha50: 'rgba(120, 200, 0, 0.5)',
#           alpha70: 'rgba(120, 200, 0, 0.7)',
#           alpha90: 'rgba(120, 200, 0, 0.9)',
#         },
#         accent: {
#           DEFAULT: '#ff8c42',
#           light: '#ffa866',
#           dark: '#cc702f',
#           alpha10: 'rgba(255, 140, 66, 0.1)',
#           alpha30: 'rgba(255, 140, 66, 0.3)',
#           alpha50: 'rgba(255, 140, 66, 0.5)',
#           alpha70: 'rgba(255, 140, 66, 0.7)',
#           alpha90: 'rgba(255, 140, 66, 0.9)',
#         },
#         neutral: {
#           DEFAULT: '#eaeaea',
#           light: '#f7f7f7',
#           dark: '#bfbfbf',
#         },
#         error: '#f44336',
#         success: '#4caf50',
#         navbar: '#222831',
#         background: '#f8fafc',
#       },
#     },
#   },
#   plugins: [],
# }
# """
    with open(os.path.join(full_path, "postcss.config.mjs"), "w") as f:
        f.write(tailwind_config)
    print_message("Tailwind CSS configurado correctamente.", GREEN)



def generate_tailwind_styles(full_path, file_name):
    """
    Genera un archivo CSS en la carpeta src/styles.

    Args:
        full_path (str): Ruta completa del proyecto.
        file_name (str): Nombre del archivo a generar (por defecto, 'globals.css').
    """
    styles_path = os.path.join(full_path, "src", "styles")

    # Crear la carpeta src/styles si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, file_name)

    # Contenido por defecto

    content = """/*
|--------------------------------------------------------------------------
| Font
|--------------------------------------------------------------------------
|
*/ 
/* @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap'); */



/*
|--------------------------------------------------------------------------
| Tailwind Directives
|--------------------------------------------------------------------------
|
| Import TailwindCSS directives and swipe out at build-time with all of
| the styles it generates based on your configured design system.
|
*/ 
@import "tailwindcss";



/*
|--------------------------------------------------------------------------
| Tailwind Theme Variables
|--------------------------------------------------------------------------
|
| Definir variables personalizadas utilizando `@theme`.
|
*/
@theme {
  --font-display: "Satoshi", "sans-serif";
  --color-primary: #4f9da6;
  --color-primary-light: #7dbdc8;
  --color-primary-dark: #35757d;
  --color-primary-alpha70: rgba(79, 157, 166, 0.7);
  
  --color-secondary: #78c800;
  --color-secondary-light: #a4e542;
  --color-secondary-dark: #569300;
  
  --color-error: #f44336;
  --color-success: #4caf50;
  --color-navbar: #222831;
  --color-background: #f8fafc;
  
  --ease-fluid: cubic-bezier(0.3, 0, 0, 1);
  --ease-snappy: cubic-bezier(0.2, 0, 0, 1);
}




/*
|--------------------------------------------------------------------------
| Tailwind Layer
|--------------------------------------------------------------------------
|
| Import layer components.
|
*/
@layer components {
    
    /* Botones */
    .btn {
        @apply py-2 px-4 font-semibold rounded-lg shadow-md transition duration-300 ease-in-out;
    }

    .btn-primary {
        background-color: var(--color-primary);
        color: white;
        @apply shadow-sm hover:bg-[var(--color-primary-dark)] hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)];
    }

    .btn-secondary {
        background-color: var(--color-secondary);
        color: white;
        @apply shadow-sm hover:bg-[var(--color-secondary-dark)] hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-[var(--color-secondary)];
    }

    .btn-danger {
        background-color: var(--color-error);
        color: white;
        @apply shadow-sm hover:bg-red-700 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-red-400;
    }

    /* Inputs */
    .form-control {
        @apply w-full h-10 px-3 text-base placeholder-gray-600 border rounded-lg focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)];
    }

    .text-danger {
        color: var(--color-error);
    }

    .border-danger {
        border-color: var(--color-error);
        @apply border rounded-lg;
    }

    .card {
        @apply shadow border p-4 rounded bg-white;
    }

    .card--featured {
        background-color: var(--color-primary-alpha70);
        border-color: var(--color-primary);
    }

    .card__title {
        @apply text-2xl font-bold text-gray-800;
    }

    .card__description {
        @apply text-gray-600;
    }

    .card__button {
        background-color: var(--color-primary);
        color: white;
        @apply py-2 px-4 rounded hover:bg-[var(--color-primary-dark)] transition duration-300 ease-in-out;
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


def generate_css_styles(full_path, file_name):
    """
    Genera un archivo CSS en la carpeta src/styles.

    Args:
        full_path (str): Ruta completa del proyecto.
        file_name (str): Nombre del archivo a generar (por defecto, 'globals.css').
    """
    styles_path = os.path.join(full_path, "src", "styles")

    # Crear la carpeta src/styles si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, file_name)

    # Contenido por defecto
    content = """:root {
    --primary: #6834a6;  /* #6834a6 */
    --white: #FFF;
    --black: #000000;
    --mainFont: 'Poppins', sans-serif;
    /* --mainFont: 'Lato', sans-serif;  */
}

html {
    font-size: 62.5%;
    box-sizing: border-box;
}
*, *:before, *:after {
    box-sizing: inherit;
}

body {
    font-family: var(--mainFont);
    font-size: 2.6rem;
    line-height: 1.8;
}

h1, h2, h3 {
    font-weight: 900;
    margin: 2rem 0;
}
h1 {
    font-size: 5rem;
}
h2 {
    font-size: 4.6rem;
}
h3 {
    font-size: 3rem;
}
a {
    text-decoration: none;
}
img {
    max-width: 100%;
    display: block;
}

/** Attribute Selector **/
[class$="__container"]{
    max-width: 120rem;
    margin: 0 auto;
    width: 90%;
}

[class$="__heading"]{
    text-align: center;
    margin-bottom: 5rem;
}

/** Header **/

.header {
    /* background-image: url(../assets/images/header_bg.svg);
    background-repeat: no-repeat;
    background-position: top right;
    background-size: 45rem; */
    padding: 5rem 0;
}

/* @media (min-width: 768px) { 
    .header {
        background-size: 50rem;
    }
} */

/* @media (min-width: 992px) { 
    .header {
        background-size: 60rem;
    }
} */

/* @media (min-width: 1280px) { 
    .header {
        background-size: 110rem;
    }
} */

@media (min-width: 768px) { 
    .header__bar {
        display: flex;
        justify-content: space-between;
    }
}

.header__logo {
    width: 15rem;
    margin: 0 auto 3rem auto;
}

@media (min-width: 768px) { 
    .header__logo {
        margin: 0;
    }
    .header__grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 4rem;
        align-items: center;
    }
}

.header__heading {
    font-size: 3rem;
}

@media (min-width: 768px) { 
    .header__heading {
        text-align: left;
        font-size: 5rem;
        line-height: 1.2;
    }
}

@media (min-width: 768px) { 
    .header__image {
        max-width: 30rem;
        margin: 0 auto;
    }
}

.header__button {
    background-color: var(--primary);
    display: block;
    padding: 1rem;
    text-align: center;
    color: var(--white);
    margin-bottom: 4rem;
}

@media (min-width: 768px) { 
    .header__button {
        padding: 1rem 3rem;
        display: inline-block;
    }
}


/** Navbar **/

.navbar__bar{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    margin-top: 3rem;
}

.navbar__logo {
    width: 15rem;
    margin: 0 auto 3rem auto;
}

@media (min-width: 768px) { 
    .navbar__logo {
        margin: 0;
    }
}


@media (min-width: 768px) { 
    .navbar__bar {
        display: flex;
        flex-direction: row;
    }
}


/** Navigation **/

.navigation {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    list-style: none;
}

@media (min-width: 768px) { 
    .navigation {
        flex-direction: row;
        align-items: flex-start;
        gap: 2rem;
    }
}

.navigation__link {
    color: var(--primary);
    transition: color 0.3s ease;
}

.navigation__link:hover {
    color: var(--black); /* Cambia al color primario al pasar el cursor */
}

@media (min-width: 768px) { 
    .navigation__link {
        color: var(--primary);
    }
}

.navigation__link--white {
    color: var(--white);
}

.navigation__link--active{
    color: var(--black);
}


/** About **/

.nucleus {
    margin-top: 3rem;
}

.nucleus__grid {
    display: flex;
    flex-direction: column-reverse;
}

@media (min-width: 768px) { 
    .nucleus__grid {
        display: grid;
        grid-template-columns: 1fr 2fr;
        column-gap: 5rem;
        align-items: center;
    }
}



.list__item {
    background-color: var(--white);
    box-shadow: 0px 0px 15px 3px rgb(0 0 0 / .15);
    padding: 2rem;
    margin-bottom: 5rem;
    transition-property: transform;
    transition-duration: 300ms;
    /* transition-delay: 1s; */
}

.list__item:hover {
    transform: scale(1.1);
}

@media (min-width: 768px) { 
    .list__item--2col {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 2rem;
    }
}

.list__heading {
    font-size: 3rem;
    color: var(--primary);
    margin: 0;
}

.list__number {
    font-size: 6rem;
    margin: 0;
    font-weight: 900;
    color: var(--primary);
    text-align: center;
}

@media (min-width: 768px) { 
    .list__number {
        flex-basis: 20rem;
        text-align: right;
        font-size: 4rem;
    }
}

.list__text {
    margin: 0;
    font-size: 2rem;
}

/** Security **/

.security {
    background-color: var(--primary);
    padding: 20rem 0;
    position: relative;
    margin: 10rem 0;
    overflow: hidden;
}

.security::before, 
.security::after {
    background-color: var(--white);
    content: '';
    height: 20rem;
    width: 120%;
    position: absolute;
}

.security::before {
    top: -10rem;
    left: 0;
    transform: rotate(3deg);
}

.security::after {
    bottom: -10rem;
    left: -1rem;
    transform: rotate(3deg);
}

.security__heading {
    color: var(--white);
}

@media (min-width: 768px) { 
    .security__grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        column-gap: 5rem;
        align-items: center;
    }
}



/** Testimonials **/

.testimonials {
    background-color: var(--primary);
    padding: 5rem 0;
}

.testimonials__heading {
    color: var(--white);
}

.testimonials__grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 4rem;
}

@media (min-width: 768px) { 
    .testimonials__grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

.testimonial {
    box-shadow: 0px 0px 15px 3px rgb(0 0 0 / .15);
    background-color: var(--white);
    padding: 2rem;
    position: relative;
}

.testimonial__text {
    padding-left: 4rem;
}

.testimonial__text::before {
    content: '';
    background-image: url(../img/quote.png);
    background-size: 3rem;
    background-repeat: no-repeat;
    background-position: center;
    width: 3rem;
    height: 3rem;
    position: absolute;
    top: 3.5rem;
    left: 2rem;
}

.testimonial__author {
    color: var(--primary);
    font-weight: 700;
    text-align: right;
}

/** Footer **/

.footer {
    background-color: var(--primary);
    padding: 3rem 0;
    margin-top: 3rem;
}

@media (min-width: 768px) { 
    .footer__grid {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
}

.footer__logo {
    width: 20rem;
    margin: 0 auto 4rem auto;
}

@media (min-width: 768px) { 
    .footer__logo {
        margin: 0;
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


def generate_normalize_styles(full_path, file_name):
    """
    Genera un archivo CSS en la carpeta src/styles.

    Args:
        full_path (str): Ruta completa del proyecto.
        file_name (str): Nombre del archivo a generar (por defecto, 'globals.css').
    """
    styles_path = os.path.join(full_path, "src", "styles")

    # Crear la carpeta src/styles si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, file_name)

    # Contenido por defecto
    content = """/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */

/* Document
   ========================================================================== */

/**
 * 1. Correct the line height in all browsers.
 * 2. Prevent adjustments of font size after orientation changes in iOS.
 */

 html {
    line-height: 1.15; /* 1 */
    -webkit-text-size-adjust: 100%; /* 2 */
  }
  
  /* Sections
     ========================================================================== */
  
  /**
   * Remove the margin in all browsers.
   */
  
  body {
    margin: 0;
  }
  
  /**
   * Render the `main` element consistently in IE.
   */
  
  main {
    display: block;
  }
  
  /**
   * Correct the font size and margin on `h1` elements within `section` and
   * `article` contexts in Chrome, Firefox, and Safari.
   */
  
  h1 {
    font-size: 2em;
    margin: 0.67em 0;
  }
  
  /* Grouping content
     ========================================================================== */
  
  /**
   * 1. Add the correct box sizing in Firefox.
   * 2. Show the overflow in Edge and IE.
   */
  
  hr {
    box-sizing: content-box; /* 1 */
    height: 0; /* 1 */
    overflow: visible; /* 2 */
  }
  
  /**
   * 1. Correct the inheritance and scaling of font size in all browsers.
   * 2. Correct the odd `em` font sizing in all browsers.
   */
  
  pre {
    font-family: monospace, monospace; /* 1 */
    font-size: 1em; /* 2 */
  }
  
  /* Text-level semantics
     ========================================================================== */
  
  /**
   * Remove the gray background on active links in IE 10.
   */
  
  a {
    background-color: transparent;
  }
  
  /**
   * 1. Remove the bottom border in Chrome 57-
   * 2. Add the correct text decoration in Chrome, Edge, IE, Opera, and Safari.
   */
  
  abbr[title] {
    border-bottom: none; /* 1 */
    text-decoration: underline; /* 2 */
    text-decoration: underline dotted; /* 2 */
  }
  
  /**
   * Add the correct font weight in Chrome, Edge, and Safari.
   */
  
  b,
  strong {
    font-weight: bolder;
  }
  
  /**
   * 1. Correct the inheritance and scaling of font size in all browsers.
   * 2. Correct the odd `em` font sizing in all browsers.
   */
  
  code,
  kbd,
  samp {
    font-family: monospace, monospace; /* 1 */
    font-size: 1em; /* 2 */
  }
  
  /**
   * Add the correct font size in all browsers.
   */
  
  small {
    font-size: 80%;
  }
  
  /**
   * Prevent `sub` and `sup` elements from affecting the line height in
   * all browsers.
   */
  
  sub,
  sup {
    font-size: 75%;
    line-height: 0;
    position: relative;
    vertical-align: baseline;
  }
  
  sub {
    bottom: -0.25em;
  }
  
  sup {
    top: -0.5em;
  }
  
  /* Embedded content
     ========================================================================== */
  
  /**
   * Remove the border on images inside links in IE 10.
   */
  
  img {
    border-style: none;
  }
  
  /* Forms
     ========================================================================== */
  
  /**
   * 1. Change the font styles in all browsers.
   * 2. Remove the margin in Firefox and Safari.
   */
  
  button,
  input,
  optgroup,
  select,
  textarea {
    font-family: inherit; /* 1 */
    font-size: 100%; /* 1 */
    line-height: 1.15; /* 1 */
    margin: 0; /* 2 */
  }
  
  /**
   * Show the overflow in IE.
   * 1. Show the overflow in Edge.
   */
  
  button,
  input { /* 1 */
    overflow: visible;
  }
  
  /**
   * Remove the inheritance of text transform in Edge, Firefox, and IE.
   * 1. Remove the inheritance of text transform in Firefox.
   */
  
  button,
  select { /* 1 */
    text-transform: none;
  }
  
  /**
   * Correct the inability to style clickable types in iOS and Safari.
   */
  
  button,
  [type="button"],
  [type="reset"],
  [type="submit"] {
    -webkit-appearance: button;
  }
  
  /**
   * Remove the inner border and padding in Firefox.
   */
  
  button::-moz-focus-inner,
  [type="button"]::-moz-focus-inner,
  [type="reset"]::-moz-focus-inner,
  [type="submit"]::-moz-focus-inner {
    border-style: none;
    padding: 0;
  }
  
  /**
   * Restore the focus styles unset by the previous rule.
   */
  
  button:-moz-focusring,
  [type="button"]:-moz-focusring,
  [type="reset"]:-moz-focusring,
  [type="submit"]:-moz-focusring {
    outline: 1px dotted ButtonText;
  }
  
  /**
   * Correct the padding in Firefox.
   */
  
  fieldset {
    padding: 0.35em 0.75em 0.625em;
  }
  
  /**
   * 1. Correct the text wrapping in Edge and IE.
   * 2. Correct the color inheritance from `fieldset` elements in IE.
   * 3. Remove the padding so developers are not caught out when they zero out
   *    `fieldset` elements in all browsers.
   */
  
  legend {
    box-sizing: border-box; /* 1 */
    color: inherit; /* 2 */
    display: table; /* 1 */
    max-width: 100%; /* 1 */
    padding: 0; /* 3 */
    white-space: normal; /* 1 */
  }
  
  /**
   * Add the correct vertical alignment in Chrome, Firefox, and Opera.
   */
  
  progress {
    vertical-align: baseline;
  }
  
  /**
   * Remove the default vertical scrollbar in IE 10+.
   */
  
  textarea {
    overflow: auto;
  }
  
  /**
   * 1. Add the correct box sizing in IE 10.
   * 2. Remove the padding in IE 10.
   */
  
  [type="checkbox"],
  [type="radio"] {
    box-sizing: border-box; /* 1 */
    padding: 0; /* 2 */
  }
  
  /**
   * Correct the cursor style of increment and decrement buttons in Chrome.
   */
  
  [type="number"]::-webkit-inner-spin-button,
  [type="number"]::-webkit-outer-spin-button {
    height: auto;
  }
  
  /**
   * 1. Correct the odd appearance in Chrome and Safari.
   * 2. Correct the outline style in Safari.
   */
  
  [type="search"] {
    -webkit-appearance: textfield; /* 1 */
    outline-offset: -2px; /* 2 */
  }
  
  /**
   * Remove the inner padding in Chrome and Safari on macOS.
   */
  
  [type="search"]::-webkit-search-decoration {
    -webkit-appearance: none;
  }
  
  /**
   * 1. Correct the inability to style clickable types in iOS and Safari.
   * 2. Change font properties to `inherit` in Safari.
   */
  
  ::-webkit-file-upload-button {
    -webkit-appearance: button; /* 1 */
    font: inherit; /* 2 */
  }
  
  /* Interactive
     ========================================================================== */
  
  /*
   * Add the correct display in Edge, IE 10+, and Firefox.
   */
  
  details {
    display: block;
  }
  
  /*
   * Add the correct display in all browsers.
   */
  
  summary {
    display: list-item;
  }
  
  /* Misc
     ========================================================================== */
  
  /**
   * Add the correct display in IE 10+.
   */
  
  template {
    display: none;
  }
  
  /**
   * Add the correct display in IE 10.
   */
  
  [hidden] {
    display: none;
  }
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def generate_scss(full_path, file_name):
    """
    Genera un archivo CSS en la carpeta src/styles.

    Args:
        full_path (str): Ruta completa del proyecto.
        file_name (str): Nombre del archivo a generar (por defecto, 'globals.css').
    """
    styles_path = os.path.join(full_path, "src", "styles")

    # Crear la carpeta src/styles si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, file_name)

    # Contenido por defecto
    content = """/*================================
🎨 Variables Globales 
================================ */
:root {
    --primary: #6834a6; /* Color Principal */
    --primary-light: #8b5cf6;
    --primary-dark: #4a1d85;
  
    --secondary: #ff8c42;
    --secondary-light: #ffa866;
    --secondary-dark: #cc702f;
  
    --white: #ffffff;
    --black: #000000;
  
    --gray-100: #f8f9fa;
    --gray-200: #e9ecef;
    --gray-300: #dee2e6;
    --gray-400: #ced4da;
    --gray-500: #adb5bd;
    --gray-600: #6c757d;
    --gray-700: #495057;
    --gray-800: #343a40;
    --gray-900: #212529;
  
    /* 🎨 Estados */
    --success: #28a745;
    --warning: #ffc107;
    --error: #dc3545;
  
    /* 🎨 Fondo */
    --background: var(--gray-100);
    --navbar: var(--primary);
  
    /* 🎨 Tipografías */
    --mainFont: 'Poppins', sans-serif;
    --secondaryFont: 'Lato', sans-serif;
}
  
/* ================================
 ✨ Reset & Global Styles
 ================================ */
*, *:before, *:after {
    margin: 0;
    padding: 0;
    box-sizing: inherit;
}

html {
    font-size: 62.5%;
    box-sizing: border-box;
}
  
body {
    font-family: var(--mainFont);
    font-size: 2.6rem;
    line-height: 1.8;
    background-color: var(--background);
    color: var(--gray-900);
}
  
/* ================================
 🏗️ Tipografía
 ================================ */
h1, h2, h3 {
    font-weight: 900;
    margin: 2rem 0;
}
  
h1 { font-size: 5rem; }
h2 { font-size: 4.6rem; }
h3 { font-size: 3rem; }
  
a {
    text-decoration: none;
    color: var(--primary);
    transition: all 0.3s ease-in-out;
    
    &:hover {
      color: var(--primary-dark);
    }
}
  
/* ================================
 🏗️ Layout (Contenedor base)
 ================================ */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem;
}

/* ================================
 🔗 Navegación
 ================================ */
.navbar {
    padding: 1rem;
    background-color: var(--navbar);
    
    &__container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    &__logo img {
        height: 50px;
        width: auto;
    }
}
    
.navigation {
    &__list {
        display: flex;
        gap: 1.5rem;
        list-style: none;
    }
    
    &__item {
        margin: 0;
    }
    
    &__link {
        color: var(--black);
        font-weight: 600;
        padding: 0.5rem 1rem;
        transition: color 0.3s ease-in-out;
        
        &:hover {
            color: var(--primary-light);
        }
        
        &--active {
            color: var(--primary);
            border-bottom: 2px solid var(--primary);
        }
    }
}
  
/* ================================
 🎨 Botones
 ================================ */
.btn {
    display: inline-block;
    font-weight: 600;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    text-align: center;
    transition: background 0.3s ease-in-out;
    cursor: pointer;
}
  
.btn-primary {
    background-color: var(--primary);
    color: var(--white);
    
    &:hover {
        background-color: var(--primary-dark);
    }
}
  
.btn-secondary {
    background-color: var(--secondary);
    color: var(--white);
    
    &:hover {
        background-color: var(--secondary-dark);
    }
}
  
/* ================================
 📱 Responsive Design
 ================================ */
@media (max-width: 768px) {
    .container {
        padding: 0.5rem;
    }
    
    .navigation__list {
        flex-direction: column;
        gap: 1rem;
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