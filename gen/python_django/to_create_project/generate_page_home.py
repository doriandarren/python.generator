import os
from gen.python_django.helpers.helper_file import helper_update_line, helper_update_list
from helpers.helper_print import print_message, GREEN, CYAN




def generate_page_home(full_path, project_name_format, app_name):
    update_setting(full_path, app_name)
    create_file_html(full_path)
    update_urls(full_path, project_name_format, app_name)
    
    
    



def update_setting(full_path, app_name):
    
    str = f"        'DIRS': [BASE_DIR / \"templates\"],"
    
    helper_update_line(
        full_path,
        f"{app_name}/settings.py",
        f"        'DIRS': [],",
        str
    )
    
    print_message(f"Se ha actualizado el archivo {app_name}/settings.py", GREEN)
    
     
    







def create_file_html(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "templates")
    file_path = os.path.join(folder_path, "index.html")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Bienvenida</title>

    <!-- Tailwind CDN (rápido para dev) -->
    <script src="https://cdn.tailwindcss.com"></script>
  </head>

  <body class="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-slate-100">
    <main class="mx-auto flex min-h-screen max-w-5xl items-center px-6 py-12">
      <section class="w-full">
        <div class="inline-flex items-center gap-2 rounded-full border border-slate-800 bg-slate-900/60 px-4 py-2 text-sm text-slate-300">
          <span class="h-2 w-2 rounded-full bg-emerald-400"></span>
          Django está corriendo en local
        </div>

        <h1 class="mt-6 text-4xl font-semibold tracking-tight sm:text-5xl">
          Bienvenida 👋
        </h1>

        <p class="mt-4 max-w-2xl text-lg leading-relaxed text-slate-300">
          Tu proyecto está listo. Desde aquí puedes ir al admin, ver la documentación Swagger o Redoc,
          y empezar a integrar tu carpeta <span class="font-mono text-slate-200">gen/</span>.
        </p>

        <div class="mt-8 grid gap-4 sm:grid-cols-3">
          <a href="/swagger/"
             class="group rounded-2xl border border-slate-800 bg-slate-900/60 p-5 shadow-sm transition hover:border-slate-700 hover:bg-slate-900">
            <div class="flex items-center justify-between">
              <h2 class="text-base font-medium">Swagger</h2>
              <span class="text-slate-400 transition group-hover:translate-x-0.5">→</span>
            </div>
            <p class="mt-2 text-sm text-slate-400">Explora endpoints y prueba la API.</p>
          </a>

          <a href="/redoc/"
             class="group rounded-2xl border border-slate-800 bg-slate-900/60 p-5 shadow-sm transition hover:border-slate-700 hover:bg-slate-900">
            <div class="flex items-center justify-between">
              <h2 class="text-base font-medium">Redoc</h2>
              <span class="text-slate-400 transition group-hover:translate-x-0.5">→</span>
            </div>
            <p class="mt-2 text-sm text-slate-400">Documentación más limpia y ordenada.</p>
          </a>

          <a href="/admin/"
             class="group rounded-2xl border border-slate-800 bg-slate-900/60 p-5 shadow-sm transition hover:border-slate-700 hover:bg-slate-900">
            <div class="flex items-center justify-between">
              <h2 class="text-base font-medium">Admin</h2>
              <span class="text-slate-400 transition group-hover:translate-x-0.5">→</span>
            </div>
            <p class="mt-2 text-sm text-slate-400">Gestiona el panel de administración.</p>
          </a>
        </div>

        <footer class="mt-10 text-sm text-slate-500">
          <span class="font-mono">localhost:8000</span> · Tailwind CDN · Home template
        </footer>
      </section>
    </main>
  </body>
</html>
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        

def update_urls(full_path, project_name_format, app_name):
    
    
    str = f"from django.urls import path, include\nfrom django.views.generic import TemplateView"
    
    helper_update_line(
        full_path,
        f"{app_name}/urls.py",
        f"from django.urls import path, include",
        str
    )
    
    

    helper_update_list(
        full_path,
        f"{app_name}/urls.py",
        "urlpatterns = [",
        f"    # Home"
    )
    
    helper_update_list(
        full_path, 
        f"{app_name}/urls.py", 
        "urlpatterns = [", 
        f"    path(\"\", TemplateView.as_view(template_name=\"index.html\"), name=\"home\")"
    )
    
    print_message(f"Se ha actualizado el archivo {app_name}/urls.py", GREEN)