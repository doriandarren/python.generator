# ============================================================
# BASE STYLE GENERAL
# ============================================================

BASE_STYLE = "horror, abandoned, dirty, scratched, worn, realistic proportions, game ready, centered, isolated, single object"

LOW_POLY = "low poly, clean topology, simple geometry, optimized mesh, game asset"




# ============================================================
# MODEL PROMPTS
# ============================================================

MODEL_PROMPTS = [

    {"title": "hammer", "prompt": f"hammer, wooden handle, metal head, old and worn, horror atmosphere, scratched, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "kitchen_knife", "prompt": f"kitchen knife, simple metal blade, worn handle, horror atmosphere, stained, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "butcher_knife", "prompt": f"butcher knife, wide blade, old and worn, horror atmosphere, dirty, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "spoon", "prompt": f"spoon, metal utensil, old and worn, horror atmosphere, scratched, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "fork", "prompt": f"fork, metal utensil, old and worn, horror atmosphere, scratched, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "plate", "prompt": f"plate, simple round dish, cracked and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "bowl", "prompt": f"bowl, simple container, cracked and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "cup", "prompt": f"cup, simple drinking cup, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "glass_bottle", "prompt": f"glass bottle, simple shape, dirty and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "plastic_bottle", "prompt": f"plastic bottle, simple shape, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "wooden_chair", "prompt": f"wooden chair, simple structure, old and worn, horror atmosphere, scratched, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "wooden_table", "prompt": f"wooden table, simple structure, old and worn, horror atmosphere, scratched, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "small_stool", "prompt": f"stool, simple seat, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "bed_frame", "prompt": f"bed frame, simple structure, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "pillow", "prompt": f"pillow, simple cushion, dirty and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "mattress", "prompt": f"mattress, simple rectangular shape, stained and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "wooden_door", "prompt": f"wooden door, simple flat structure, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "door_handle", "prompt": f"door handle, simple shape, worn metal, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "metal_key", "prompt": f"key, simple metal key, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "padlock", "prompt": f"padlock, simple lock shape, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "flashlight", "prompt": f"flashlight, cylindrical shape, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "candle", "prompt": f"candle, wax candle, partially melted, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "light_bulb", "prompt": f"light bulb, glass bulb, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "book", "prompt": f"book, closed book, old and worn cover, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "notebook", "prompt": f"notebook, simple notebook, worn pages, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "paper_sheet", "prompt": f"paper sheet, flat surface, torn and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "mirror", "prompt": f"mirror, simple rectangular mirror, cracked surface, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "rope", "prompt": f"rope, simple rope coil, worn fibers, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "chain", "prompt": f"chain, linked metal chain, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "wooden_box", "prompt": f"wooden box, simple cube shape, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},
    {"title": "cardboard_box", "prompt": f"cardboard box, simple cube shape, worn and dirty, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "trash_can", "prompt": f"trash can, simple container, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "bucket", "prompt": f"bucket, simple container, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "toy_doll", "prompt": f"doll, simple toy doll, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "face_mask", "prompt": f"mask, simple face mask, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "shoe", "prompt": f"shoe, simple footwear, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "boot", "prompt": f"boot, simple footwear, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "clock", "prompt": f"wall clock, round shape, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "skull", "prompt": f"human skull, simple bone structure, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

    {"title": "bone", "prompt": f"bone, simple bone shape, old and worn, horror atmosphere, centered, isolated, single object, clean silhouette, {BASE_STYLE}, {LOW_POLY}"},

]
