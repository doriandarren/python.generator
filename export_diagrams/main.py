import xml.etree.ElementTree as ET

from helpers.helper_print import print_header


def generate_diagrams(table, user_columns):
    parent_id = "WIyWlLk6GJQsqaUBKTNV-1"
    table_id = f"{table}-0"

    # Columnas automáticas
    columns = ["id"] + user_columns + ["created_at", "updated_at", "deleted_at"]

    mxfile = ET.Element("mxfile", {
        "host": "app.diagrams.net",
        "agent": "PythonGenerated",
        "version": "26.1.3"
    })

    diagram = ET.SubElement(mxfile, "diagram", {"id": f"{table}-diagram-id", "name": "Page-1"})
    graph_model = ET.SubElement(diagram, "mxGraphModel", {
        "dx": "1434", "dy": "785", "grid": "1", "gridSize": "10", "guides": "1", "tooltips": "1",
        "connect": "1", "arrows": "1", "fold": "1", "page": "1", "pageScale": "1",
        "pageWidth": "827", "pageHeight": "1169", "math": "0", "shadow": "0"
    })
    root = ET.SubElement(graph_model, "root")

    ET.SubElement(root, "mxCell", {"id": "WIyWlLk6GJQsqaUBKTNV-0"})
    ET.SubElement(root, "mxCell", {"id": parent_id, "parent": "WIyWlLk6GJQsqaUBKTNV-0"})

    table_cell = ET.SubElement(root, "mxCell", {
        "id": table_id,
        "value": table,
        "style": "swimlane;fontStyle=2;align=center;verticalAlign=top;childLayout=stackLayout;"
                 "horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;"
                 "collapsible=1;marginBottom=0;rounded=0;shadow=0;strokeWidth=1;",
        "parent": parent_id,
        "vertex": "1"
    })

    geometry = ET.SubElement(table_cell, "mxGeometry", {
        "x": "220", "y": "120", "width": "240",
        "height": str(30 + 26 * len(columns)), "as": "geometry"
    })
    ET.SubElement(geometry, "mxRectangle", {
        "x": "230", "y": "140", "width": "240", "height": "26", "as": "alternateBounds"
    })

    for i, field in enumerate(columns):
        cell = ET.SubElement(root, "mxCell", {
            "id": f"{table_id}-{i+1}",
            "value": field,
            "style": "text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
                     "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;",
            "parent": table_id,
            "vertex": "1"
        })
        ET.SubElement(cell, "mxGeometry", {
            "y": str(26 * (i+1)), "width": "240", "height": "26", "as": "geometry"
        })

    output_filename = f"{table}_diagram_generated.drawio"
    ET.ElementTree(mxfile).write(output_filename, encoding="utf-8", xml_declaration=True)
    print(f"✅ Diagrama generado en {output_filename}")





if __name__ == '__main__':

    print_header("EXPORT DIAGRAMS")

    while True:
        table = input("🔤 Nombre de la tabla: ").strip()
        columns_input = input("✏️  Escribe los campos separados por espacios (sin incluir id, timestamps): ").strip()
        user_columns = columns_input.split()

        if not table or not user_columns:
            print("❌ Datos inválidos. Inténtalo de nuevo.")
        else:
            generate_diagrams(table, user_columns)

        continuar = input("¿Deseas agregar otra tabla? (s/n): ").strip().lower()
        if continuar != "s":
            break

    print("👋 Fin del generador de diagramas.")
