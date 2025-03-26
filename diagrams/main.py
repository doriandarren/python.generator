import xml.etree.ElementTree as ET

def generate_diagrams():
    parent_id = "WIyWlLk6GJQsqaUBKTNV-1"
    table_id = "washes-0"
    fields = [
        "wash_counter", "trx_date", "customer_code", "company_name", "plate", "trailer_plate",
        "driver", "driver_doc", "wash_type_id", "init_time", "finish_time", "price", "special_price",
        "courtesy", "operator_id", "extras", "comments", "payment_method", "invoiced",
        "invoice_package_id", "in_job", "status"
    ]

    mxfile = ET.Element("mxfile", {
        "host": "app.diagrams.net",
        "agent": "PythonGenerated",
        "version": "26.1.3"
    })
    diagram = ET.SubElement(mxfile, "diagram", {"id": "wash-diagram-id", "name": "Page-1"})
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
        "value": "washes",
        "style": "swimlane;fontStyle=2;align=center;verticalAlign=top;childLayout=stackLayout;"
                 "horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;"
                 "collapsible=1;marginBottom=0;rounded=0;shadow=0;strokeWidth=1;",
        "parent": parent_id,
        "vertex": "1"
    })
    geometry = ET.SubElement(table_cell, "mxGeometry", {
        "x": "220", "y": "120", "width": "240",
        "height": str(30 + 26 * len(fields)), "as": "geometry"
    })
    ET.SubElement(geometry, "mxRectangle", {
        "x": "230", "y": "140", "width": "240", "height": "26", "as": "alternateBounds"
    })

    for i, field in enumerate(fields):
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

    ET.ElementTree(mxfile).write('washes_diagram_generated.drawio', encoding="utf-8", xml_declaration=True)

if __name__ == '__main__':
    print("******************************************************")
    print("**********************  DIAGRAMS   *******************")
    print("******************************************************")
    generate_diagrams()
    print("✅ Diagrama generado en washes_diagram_generated.drawio")
