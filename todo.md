# Prompts

```sh

def findByIsTextProcessed(self):
    return AiPromptGeneration.objects.filter(is_text_processed=False).first()


def findByIsImageProcessed(self):
    return AiPromptGeneration.objects.filter(is_image_processed=False).first()


data/data_prompt:







## enums/ai_prompt_category_enum.py

class AiPromptCategoryEnum:
    """
    Enum para las categorías de prompts de IA.
    Incluye ID, nombre, slug y descripción.
    """

    # INFANTIL
    CHILDREN_STORIES_ID = 1
    CHILDREN_STORIES_NAME = "Cuentos de niños"
    CHILDREN_STORIES_SLUG = "cuentos-de-ninos"
    CHILDREN_STORIES_DESCRIPTION = "Historias infantiles simples."

    FABLES_ID = 2
    FABLES_NAME = "Fábulas"
    FABLES_SLUG = "fabulas"
    FABLES_DESCRIPTION = "Cuentos con moraleja."

    # FANTASÍA / CIENCIA FICCIÓN
    FANTASY_ID = 3
    FANTASY_NAME = "Fantasía"
    FANTASY_SLUG = "fantasia"
    FANTASY_DESCRIPTION = "Mundos mágicos."

    SCIENCE_FICTION_ID = 4
    SCIENCE_FICTION_NAME = "Ciencia ficción"
    SCIENCE_FICTION_SLUG = "ciencia-ficcion"
    SCIENCE_FICTION_DESCRIPTION = "Tecnología y futuro."

    DYSTOPIA_ID = 5
    DYSTOPIA_NAME = "Distopía"
    DYSTOPIA_SLUG = "distopia"
    DYSTOPIA_DESCRIPTION = "Sociedades oscuras."

    # TERROR / OSCURO
    HORROR_ID = 6
    HORROR_NAME = "Terror"
    HORROR_SLUG = "terror"
    HORROR_DESCRIPTION = "Miedo y tensión."

    PSYCHOLOGICAL_HORROR_ID = 7
    PSYCHOLOGICAL_HORROR_NAME = "Terror psicológico"
    PSYCHOLOGICAL_HORROR_SLUG = "terror-psicologico"
    PSYCHOLOGICAL_HORROR_DESCRIPTION = "Miedo mental."

    PARANORMAL_ID = 8
    PARANORMAL_NAME = "Paranormal"
    PARANORMAL_SLUG = "paranormal"
    PARANORMAL_DESCRIPTION = "Fenómenos extraños."

    # MISTERIO / SUSPENSE
    SUSPENSE_ID = 9
    SUSPENSE_NAME = "Suspenso"
    SUSPENSE_SLUG = "suspenso"
    SUSPENSE_DESCRIPTION = "Tensión constante."

    MYSTERY_ID = 10
    MYSTERY_NAME = "Misterio"
    MYSTERY_SLUG = "misterio"
    MYSTERY_DESCRIPTION = "Casos por resolver."

    DETECTIVES_ID = 11
    DETECTIVES_NAME = "Detectives"
    DETECTIVES_SLUG = "detectives"
    DETECTIVES_DESCRIPTION = "Investigaciones."

    THRILLER_ID = 12
    THRILLER_NAME = "Thriller"
    THRILLER_SLUG = "thriller"
    THRILLER_DESCRIPTION = "Acción y suspense."

    # ACCIÓN / AVENTURA
    ADVENTURE_ID = 13
    ADVENTURE_NAME = "Aventura"
    ADVENTURE_SLUG = "aventura"
    ADVENTURE_DESCRIPTION = "Viajes y retos."

    ACTION_ID = 14
    ACTION_NAME = "Acción"
    ACTION_SLUG = "accion"
    ACTION_DESCRIPTION = "Ritmo rápido."

    SUPERHEROES_ID = 15
    SUPERHEROES_NAME = "Superhéroes"
    SUPERHEROES_SLUG = "superheroes"
    SUPERHEROES_DESCRIPTION = "Poderes y héroes."

    # CRIATURAS
    STRANGE_CREATURES_ID = 16
    STRANGE_CREATURES_NAME = "Criaturas extrañas"
    STRANGE_CREATURES_SLUG = "criaturas-extranas"
    STRANGE_CREATURES_DESCRIPTION = "Seres desconocidos."

    MONSTERS_ID = 17
    MONSTERS_NAME = "Monstruos"
    MONSTERS_SLUG = "monstruos"
    MONSTERS_DESCRIPTION = "Criaturas temibles."

    MYTHOLOGY_ID = 18
    MYTHOLOGY_NAME = "Mitología"
    MYTHOLOGY_SLUG = "mitologia"
    MYTHOLOGY_DESCRIPTION = "Dioses y leyendas."

    # DRAMA / EMOCIONAL
    DRAMA_ID = 19
    DRAMA_NAME = "Drama"
    DRAMA_SLUG = "drama"
    DRAMA_DESCRIPTION = "Conflictos emocionales."

    SELF_IMPROVEMENT_ID = 20
    SELF_IMPROVEMENT_NAME = "Superación personal"
    SELF_IMPROVEMENT_SLUG = "superacion-personal"
    SELF_IMPROVEMENT_DESCRIPTION = "Crecimiento personal."

    FRIENDSHIP_ID = 21
    FRIENDSHIP_NAME = "Amistad"
    FRIENDSHIP_SLUG = "amistad"
    FRIENDSHIP_DESCRIPTION = "Relaciones cercanas."

    # ROMANCE
    ROMANCE_ID = 22
    ROMANCE_NAME = "Romance"
    ROMANCE_SLUG = "romance"
    ROMANCE_DESCRIPTION = "Historias de amor."

    YOUNG_ADULT_ROMANCE_ID = 23
    YOUNG_ADULT_ROMANCE_NAME = "Romance juvenil"
    YOUNG_ADULT_ROMANCE_SLUG = "romance-juvenil"
    YOUNG_ADULT_ROMANCE_DESCRIPTION = "Amor joven."

    # HUMOR
    COMEDY_ID = 24
    COMEDY_NAME = "Comedia"
    COMEDY_SLUG = "comedia"
    COMEDY_DESCRIPTION = "Historias divertidas."

    SATIRE_ID = 25
    SATIRE_NAME = "Sátira"
    SATIRE_SLUG = "satira"
    SATIRE_DESCRIPTION = "Crítica con humor."

    # HISTÓRICO
    HISTORICAL_ID = 26
    HISTORICAL_NAME = "Histórico"
    HISTORICAL_SLUG = "historico"
    HISTORICAL_DESCRIPTION = "Basado en el pasado."

    FICTIONAL_HISTORICAL_ID = 27
    FICTIONAL_HISTORICAL_NAME = "Histórico ficticio"
    FICTIONAL_HISTORICAL_SLUG = "historico-ficticio"
    FICTIONAL_HISTORICAL_DESCRIPTION = "Historia imaginada."

    # TECNOLÓGICO
    TECHNOLOGY_ID = 28
    TECHNOLOGY_NAME = "Tecnología"
    TECHNOLOGY_SLUG = "tecnologia"
    TECHNOLOGY_DESCRIPTION = "Innovación digital."

    ARTIFICIAL_INTELLIGENCE_ID = 29
    ARTIFICIAL_INTELLIGENCE_NAME = "Inteligencia artificial"
    ARTIFICIAL_INTELLIGENCE_SLUG = "inteligencia-artificial"
    ARTIFICIAL_INTELLIGENCE_DESCRIPTION = "IA y máquinas."

    CYBERPUNK_ID = 30
    CYBERPUNK_NAME = "Ciberpunk"
    CYBERPUNK_SLUG = "ciberpunk"
    CYBERPUNK_DESCRIPTION = "Futuro tecnológico oscuro."

    # FILOSÓFICO
    PHILOSOPHICAL_ID = 31
    PHILOSOPHICAL_NAME = "Filosófico"
    PHILOSOPHICAL_SLUG = "filosofico"
    PHILOSOPHICAL_DESCRIPTION = "Ideas profundas."

    EXISTENTIAL_ID = 32
    EXISTENTIAL_NAME = "Existencial"
    EXISTENTIAL_SLUG = "existencial"
    EXISTENTIAL_DESCRIPTION = "Sentido de la vida."

    # REALISMO
    EVERYDAY_LIFE_ID = 33
    EVERYDAY_LIFE_NAME = "Vida cotidiana"
    EVERYDAY_LIFE_SLUG = "vida-cotidiana"
    EVERYDAY_LIFE_DESCRIPTION = "Situaciones reales."

    MAGICAL_REALISM_ID = 34
    MAGICAL_REALISM_NAME = "Realismo mágico"
    MAGICAL_REALISM_SLUG = "realismo-magico"
    MAGICAL_REALISM_DESCRIPTION = "Magia en lo real."

    # OTROS INTERESANTES
    TIME_TRAVEL_ID = 35
    TIME_TRAVEL_NAME = "Viajes en el tiempo"
    TIME_TRAVEL_SLUG = "viajes-en-el-tiempo"
    TIME_TRAVEL_DESCRIPTION = "Saltos temporales."

    ALTERNATE_UNIVERSES_ID = 36
    ALTERNATE_UNIVERSES_NAME = "Universos alternativos"
    ALTERNATE_UNIVERSES_SLUG = "universos-alternativos"
    ALTERNATE_UNIVERSES_DESCRIPTION = "Realidades paralelas."

    APOCALYPSE_ID = 37
    APOCALYPSE_NAME = "Apocalipsis"
    APOCALYPSE_SLUG = "apocalipsis"
    APOCALYPSE_DESCRIPTION = "Fin del mundo."

    POST_APOCALYPTIC_ID = 38
    POST_APOCALYPTIC_NAME = "Postapocalíptico"
    POST_APOCALYPTIC_SLUG = "postapocaliptico"
    POST_APOCALYPTIC_DESCRIPTION = "Después del caos."

    SURVIVAL_ID = 39
    SURVIVAL_NAME = "Supervivencia"
    SURVIVAL_SLUG = "supervivencia"
    SURVIVAL_DESCRIPTION = "Lucha por vivir."

    SPACE_ID = 40
    SPACE_NAME = "Espacio"
    SPACE_SLUG = "espacio"
    SPACE_DESCRIPTION = "Exploración espacial."

    # LIBRE
    OTHERS_ID = 41
    OTHERS_NAME = "Otros"
    OTHERS_SLUG = "otros"
    OTHERS_DESCRIPTION = "Categoría general."



```

## Tables:

📄 Table: ai_prompt_categories - AiPromptCategory - AiPromptCategories
Columns: name description slug

📄 Table: ai_prompt_generations - AiPromptGeneration - AiPromptGenerations
Columns: ai_prompt_category_id:fk system_role system_message user_role user_message is_text_processed:boolean is_image_processed:boolean is_video_processed:boolean

📄 Table: ai_text_generations - AiTextGeneration - AiTextGenerations
Columns: ai_prompt_generation_id:fk model_name response_message:text response_done response_done_reason response_total_duration response_load_duration response_prompt_eval_count response_prompt_eval_duration response_eval_count response_eval_duration

📄 Table: ai_image_generations - AiImageGeneration - AiImageGenerations
Columns: ai_prompt_generation_id:fk comfyui_prompt_id comfyui_output_path mime_type width:integer height:integer image_url
