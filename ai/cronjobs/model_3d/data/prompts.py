# ============================================================
# BASE STYLE GENERAL
# ============================================================

# Estilo base optimizado para assets industriales de horror compatibles con UE5
BASE_STYLE = (
    "horror bunker industrial asset, realistic proportions, centered, isolated, single object, "
    "neutral pose, symmetrical, no background, uniform scale, clean topology, watertight mesh, "
    "solid geometry, hard surface, game ready, realtime asset, 3d model"
)

# Modificador para obtener mallas optimizadas en tiempo real
LOW_POLY = "low poly, optimized mesh, low triangle count"


# ============================================================
# MODEL PROMPTS
# ============================================================

MODEL_PROMPTS = [

    {
        "title": "rusty_metal_key",
        "prompt": f"rusty old metal key, worn surface, detailed industrial design, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "heavy_industrial_padlock",
        "prompt": f"heavy rusty padlock, thick metal, worn edges, mechanical locking mechanism, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_bunker_door",
        "prompt": f"industrial bunker metal door, heavy steel, reinforced structure, modular asset, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_flashlight",
        "prompt": f"industrial handheld flashlight, worn metal and plastic, cylindrical shape, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "abandoned_wooden_table",
        "prompt": f"old abandoned wooden table, worn wood planks, simple structure, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "abandoned_wooden_chair",
        "prompt": f"old abandoned wooden chair, worn surface, simple geometry, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "concrete_wall_panel",
        "prompt": f"modular concrete wall panel, bunker structure, flat surface, modular construction, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "concrete_floor_tile",
        "prompt": f"modular concrete floor tile, flat surface, modular bunker floor segment, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_pipe_segment",
        "prompt": f"industrial metal pipe segment, cylindrical modular pipe, mechanical structure, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "mechanical_puzzle_box",
        "prompt": f"mechanical puzzle box, mysterious device, intricate mechanical parts, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_generator",
        "prompt": f"industrial electric generator, heavy machinery, mechanical details, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "electrical_fuse_panel",
        "prompt": f"industrial electrical fuse panel, mechanical box, wall mounted device, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "horror_mannequin",
        "prompt": f"old mannequin, human shaped dummy, neutral standing pose, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "metal_stair_segment",
        "prompt": f"industrial metal stair segment, modular staircase element, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "ventilation_duct",
        "prompt": f"industrial air ventilation duct segment, modular ventilation pipe, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "hanging_light_bulb",
        "prompt": f"old hanging light bulb, glass bulb, metal socket, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "old_paper_note",
        "prompt": f"old worn paper note sheet, flat surface, thin geometry, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "metal_chain_segment",
        "prompt": f"industrial heavy metal chain segment, linked chain structure, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "wooden_storage_crate",
        "prompt": f"old wooden crate storage box, worn wood planks, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "glass_bottle",
        "prompt": f"old glass bottle, cylindrical shape, worn glass surface, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "rusty_kitchen_knife",
        "prompt": f"large rusty kitchen knife, long blade, worn metal surface, sharp edge, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_butcher_knife",
        "prompt": f"industrial butcher knife, heavy blade, thick metal, worn handle, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_chainsaw",
        "prompt": f"old industrial chainsaw, mechanical tool, worn metal and plastic, detailed chain blade, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_axe",
        "prompt": f"industrial axe, heavy metal blade, worn wooden handle, sharp edge, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "metal_shelf_unit",
        "prompt": f"industrial metal shelf unit, storage furniture, modular structure, worn metal, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "wall_metal_shelf",
        "prompt": f"industrial wall shelf, metal structure, storage surface, worn edges, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "wooden_shelving_unit",
        "prompt": f"old wooden shelving unit, worn planks, abandoned furniture, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "wall_metal_ledge",
        "prompt": f"small industrial wall ledge, metal surface, storage support, worn texture, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_metal_table",
        "prompt": f"old industrial metal table, heavy structure, worn surface, abandoned furniture, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_workbench",
        "prompt": f"industrial workbench table, mechanical workspace, worn metal and wood, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_locker",
        "prompt": f"industrial metal locker, storage cabinet, worn paint, mechanical structure, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "metal_storage_cabinet",
        "prompt": f"industrial storage cabinet, metal doors, worn surface, mechanical object, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_barrel",
        "prompt": f"industrial metal barrel, cylindrical container, worn surface, storage object, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "hazardous_barrel",
        "prompt": f"hazardous industrial barrel, warning container, worn metal surface, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_toolbox",
        "prompt": f"industrial toolbox, mechanical container, worn metal case, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_hammer",
        "prompt": f"industrial hammer, heavy tool, worn metal head, mechanical object, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_crowbar",
        "prompt": f"industrial crowbar tool, long metal bar, worn surface, mechanical object, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "industrial_fan",
        "prompt": f"old industrial fan, mechanical blades, worn metal structure, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "utility_transport_cart",
        "prompt": f"industrial utility cart, metal frame, storage transport object, worn surface, {BASE_STYLE}, {LOW_POLY}"
    },

    {
        "title": "medical_stretcher",
        "prompt": f"old medical stretcher bed, metal frame, worn surface, hospital equipment, {BASE_STYLE}, {LOW_POLY}"
    },

]


