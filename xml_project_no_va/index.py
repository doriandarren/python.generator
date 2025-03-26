import xml.etree.ElementTree as ET


def read_file(file):
    tree = ET.parse(file)
    root = tree.getroot()


    # for child in root:
    #     print(f"Tag: {child.tag}, Atributos: {child.attrib}")
    #
    #     for subchild in child:
    #         print(f"  Subtag: {subchild.tag}, Atributos: {subchild.attrib}, Valor: {subchild.text}")



    for diagram in root.findall("diagram"):
        print(f"Tag: {diagram.tag}, Atributos: {diagram.attrib}")

        # Nivel 2: Encontrar <mxGraphModel> dentro de <diagram>
        mxgraph_model = diagram.find("mxGraphModel")

        if mxgraph_model is not None:
            print(f"  Subtag: {mxgraph_model.tag}, Atributos: {mxgraph_model.attrib}")

            # Nivel 3: Encontrar <root> dentro de <mxGraphModel>
            mxgraph_root = mxgraph_model.find("root")

            if mxgraph_root is not None:
                # print(f"    Subsubtag: {mxgraph_root.tag}, Atributos: {mxgraph_root.attrib}")

                # Nivel 4: Iterar sobre cada <mxCell> dentro de <root>
                for mxcell in mxgraph_root.findall("mxCell"):
                    # print(f"      Subsubsubtag: {mxcell.tag}, Atributos: {mxcell.attrib}")

                    # Verificar y extraer datos de <mxGeometry> si existe dentro de <mxCell>
                    mxgeometry = mxcell.find("mxGeometry")
                    if mxgeometry is not None:
                        print(f"        mxGeometry Atributos: {mxgeometry.attrib}")
        #     else:
        #         print("No se encontró <root> dentro de <mxGraphModel>.")
        # else:
        #     print("No se encontró <mxGraphModel> en <diagram>.")





if __name__ == "__main__":
    file = "portuarios.xml"
    read_file(file)