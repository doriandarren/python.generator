import os


def list_xml_assets(assets_dir):
    """
    Devuelve una lista de dicts estilo Node:
    [{ name, value }]
    """
    if not os.path.isdir(assets_dir):
        return []

    files = []

    for f in os.listdir(assets_dir):
        if f.lower().endswith(".drawio.xml"):
            files.append({
                "name": f,
                "value": os.path.join(assets_dir, f)
            })

    return files
