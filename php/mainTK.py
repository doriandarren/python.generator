import tkinter as tk
from tkinter import messagebox
from main import generate


def process_inputs():
    # Obtener los valores de los campos de entrada
    namespace = namespace_entry.get().strip()
    ruta = ruta_entry.get().strip()
    singular_name = singular_name_entry.get().strip()
    plural_name = plural_name_entry.get().strip()
    input_columns = input_columns_entry.get().strip()

    # Validar que los campos requeridos no estén vacíos
    if not singular_name or not plural_name or not input_columns:
        messagebox.showerror("Error", "Por favor, completa todos los campos obligatorios.")
        return

    # Procesar las columnas
    columns = [{"name": column} for column in input_columns.split()]

    # Mostrar los resultados en un cuadro de mensaje
    result_message = (
        f"Namespace: {namespace}\n"
        f"Ruta: {ruta}\n"
        f"Nombre singular: {singular_name}\n"
        f"Nombre plural: {plural_name}\n"
        f"Columnas: {columns}"
    )

    generate(namespace, ruta, singular_name, plural_name, columns)

    messagebox.showinfo("Resultado", result_message)




if __name__ == "__main__":

    root = tk.Tk()
    root.title("Generador de Código")
    root.geometry("800x800")


    # Crear las etiquetas y entradas
    tk.Label(root, text="Namespace (API / ERP / INVOICES):").pack(anchor="w", padx=10, pady=5)
    namespace_entry = tk.Entry(root)
    namespace_entry.insert(0, "API")  # Valor por defecto
    namespace_entry.pack(fill="x", padx=10)

    tk.Label(root, text="Ruta proyecto:").pack(anchor="w", padx=10, pady=5)
    ruta_entry = tk.Entry(root)
    ## /Users/dorian/PhpstormProjects81/laravel_test/
    ruta_entry.insert(0, "/Users/dorian/PhpstormProjects81/laravel_test/")  # Valor por defecto
    ruta_entry.pack(fill="x", padx=10)

    tk.Label(root, text="Nombre singular (AgendaUnloading):").pack(anchor="w", padx=10, pady=5)
    singular_name_entry = tk.Entry(root)
    singular_name_entry.pack(fill="x", padx=10)

    tk.Label(root, text="Nombre plural (AgendaUnloadings):").pack(anchor="w", padx=10, pady=5)
    plural_name_entry = tk.Entry(root)
    plural_name_entry.pack(fill="x", padx=10)

    tk.Label(root, text="Columnas (separadas por espacio):").pack(anchor="w", padx=10, pady=5)
    input_columns_entry = tk.Entry(root)
    input_columns_entry.pack(fill="x", padx=10)

    # Botón para procesar la entrada
    submit_button = tk.Button(root, text="Procesar", command=process_inputs)
    submit_button.pack(pady=20)


    root.mainloop()