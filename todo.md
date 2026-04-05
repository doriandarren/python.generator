# Prompts

```sh

def findByIsTextProcessed(self):
    return AiPromptGeneration.objects.filter(is_text_processed=False).first()


def findByIsImageProcessed(self):
    return AiPromptGeneration.objects.filter(is_image_processed=False).first()


data/data_prompt:

def get_data_prompts():
    return [
        # =========================
        # CUENTOS DE NIÑOS (10)
        # =========================
        {
            "system_role": "system",
            "system_message": "Eres un asistente creativo que escribe cuentos infantiles sencillos, divertidos y con moraleja.",
            "user_role": "user",
            "user_message": "Escribe un cuento sobre un niño que descubre un bosque donde los animales pueden hablar.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un asistente creativo de cuentos infantiles con tono amable y educativo.",
            "user_role": "user",
            "user_message": "Crea un cuento sobre una niña que aprende a compartir sus juguetes con otros.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un asistente que crea cuentos infantiles mágicos y positivos.",
            "user_role": "user",
            "user_message": "Escribe una historia sobre un dragón pequeño que tiene miedo de volar.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de cuentos infantiles con personajes divertidos.",
            "user_role": "user",
            "user_message": "Cuenta la historia de un gato que quería ser astronauta.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de cuentos infantiles con enseñanzas.",
            "user_role": "user",
            "user_message": "Escribe un cuento sobre un niño que aprende la importancia de decir la verdad.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de cuentos infantiles llenos de imaginación.",
            "user_role": "user",
            "user_message": "Crea una historia sobre una nube que baja a jugar con los niños.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de cuentos infantiles sencillos.",
            "user_role": "user",
            "user_message": "Cuenta un cuento sobre un lápiz mágico que cobra vida.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de cuentos infantiles educativos.",
            "user_role": "user",
            "user_message": "Escribe una historia sobre un niño que aprende a cuidar la naturaleza.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de cuentos infantiles con animales protagonistas.",
            "user_role": "user",
            "user_message": "Cuenta la historia de una tortuga que gana una carrera gracias a su constancia.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de cuentos infantiles positivos.",
            "user_role": "user",
            "user_message": "Escribe un cuento sobre un niño que supera su miedo a la oscuridad.",
            "is_processed": False,
        },

        # =========================
        # CRIATURAS EXTRAÑAS (10)
        # =========================
        {
            "system_role": "system",
            "system_message": "Eres un asistente creativo que escribe historias sobre criaturas extrañas y desconocidas.",
            "user_role": "user",
            "user_message": "Escribe una historia sobre una criatura invisible que vive en una casa abandonada.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de criaturas misteriosas.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre un ser que cambia de forma cada vez que alguien lo mira.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de historias extrañas y originales.",
            "user_role": "user",
            "user_message": "Crea una historia sobre una criatura que se alimenta de recuerdos humanos.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de criaturas únicas.",
            "user_role": "user",
            "user_message": "Escribe sobre un ser que vive dentro de los espejos.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de historias misteriosas.",
            "user_role": "user",
            "user_message": "Cuenta la historia de una criatura que solo aparece durante tormentas eléctricas.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de criaturas fantásticas.",
            "user_role": "user",
            "user_message": "Escribe sobre un ser que susurra secretos en los sueños.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de historias oscuras.",
            "user_role": "user",
            "user_message": "Crea una historia sobre una criatura que imita voces humanas.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de lo desconocido.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre un ser que vive bajo la tierra y observa a los humanos.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de criaturas inquietantes.",
            "user_role": "user",
            "user_message": "Escribe sobre una criatura que no proyecta sombra.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de historias extrañas.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre un ser que aparece en fotografías antiguas.",
            "is_processed": False,
        },

        # =========================
        # SUPERHÉROES (10)
        # =========================
        {
            "system_role": "system",
            "system_message": "Eres un escritor de historias de superhéroes.",
            "user_role": "user",
            "user_message": "Escribe una historia sobre un héroe que puede controlar el tiempo.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de historias de acción.",
            "user_role": "user",
            "user_message": "Cuenta la historia de una heroína que puede volverse invisible.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de superhéroes.",
            "user_role": "user",
            "user_message": "Escribe sobre un héroe que obtiene poderes al tocar objetos.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de historias épicas.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre un grupo de jóvenes con habilidades especiales.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de acción.",
            "user_role": "user",
            "user_message": "Escribe sobre un héroe que lucha contra villanos en una ciudad futurista.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de historias de héroes.",
            "user_role": "user",
            "user_message": "Cuenta la historia de un héroe sin poderes que salva el día con inteligencia.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de aventuras.",
            "user_role": "user",
            "user_message": "Escribe sobre un héroe que puede hablar con animales.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de historias heroicas.",
            "user_role": "user",
            "user_message": "Cuenta la historia de un héroe que protege su barrio.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de historias modernas.",
            "user_role": "user",
            "user_message": "Escribe sobre un héroe que usa tecnología avanzada.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de superhéroes.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre un héroe que pierde sus poderes.",
            "is_processed": False,
        },

        # =========================
        # TERROR (10)
        # =========================
        {
            "system_role": "system",
            "system_message": "Eres un escritor de historias de terror.",
            "user_role": "user",
            "user_message": "Escribe una historia sobre una casa donde nadie puede salir una vez entra.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de terror psicológico.",
            "user_role": "user",
            "user_message": "Cuenta la historia de una persona que empieza a ver cosas que no existen.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de historias oscuras.",
            "user_role": "user",
            "user_message": "Escribe sobre un pueblo donde todos desaparecen por la noche.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de terror.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre un espejo que muestra algo diferente a la realidad.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de miedo.",
            "user_role": "user",
            "user_message": "Escribe sobre una llamada telefónica que predice la muerte.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de historias inquietantes.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre una sombra que sigue a alguien.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de terror.",
            "user_role": "user",
            "user_message": "Escribe sobre una puerta que aparece solo a medianoche.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador oscuro.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre alguien atrapado en un sueño del que no puede despertar.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de terror psicológico.",
            "user_role": "user",
            "user_message": "Escribe sobre una persona que deja de reconocer a su familia.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de miedo.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre un diario que escribe solo.",
            "is_processed": False,
        },

        # =========================
        # SUSPENSO (10)
        # =========================
        {
            "system_role": "system",
            "system_message": "Eres un escritor de suspense.",
            "user_role": "user",
            "user_message": "Escribe una historia sobre una persona que recibe un mensaje extraño.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de suspense.",
            "user_role": "user",
            "user_message": "Cuenta la historia de alguien seguido por una figura desconocida.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de tensión.",
            "user_role": "user",
            "user_message": "Escribe sobre una persona que encuentra una llave sin saber qué abre.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador intrigante.",
            "user_role": "user",
            "user_message": "Cuenta la historia de una desaparición misteriosa.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de misterio.",
            "user_role": "user",
            "user_message": "Escribe sobre una nota anónima que cambia la vida del protagonista.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de intriga.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre una puerta que no debería existir.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de suspense.",
            "user_role": "user",
            "user_message": "Escribe sobre una persona que encuentra algo escondido en su casa.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de misterio.",
            "user_role": "user",
            "user_message": "Cuenta la historia de alguien que pierde la memoria.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de intriga.",
            "user_role": "user",
            "user_message": "Escribe sobre una persona que recibe un paquete sin remitente.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de suspense.",
            "user_role": "user",
            "user_message": "Cuenta una historia sobre alguien que descubre un secreto peligroso.",
            "is_processed": False,
        },

        # =========================
        # FANTASÍA (10)
        # =========================
        {
            "system_role": "system",
            "system_message": "Eres un escritor de fantasía.",
            "user_role": "user",
            "user_message": "Escribe una historia sobre un reino oculto bajo el mar.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador fantástico.",
            "user_role": "user",
            "user_message": "Cuenta la historia de un mago que pierde sus poderes.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de mundos mágicos.",
            "user_role": "user",
            "user_message": "Escribe sobre una espada con voluntad propia.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador épico.",
            "user_role": "user",
            "user_message": "Cuenta la historia de un héroe en un mundo de dragones.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de fantasía.",
            "user_role": "user",
            "user_message": "Escribe sobre un portal a otro mundo.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador mágico.",
            "user_role": "user",
            "user_message": "Cuenta la historia de una ciudad flotante.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de fantasía.",
            "user_role": "user",
            "user_message": "Escribe sobre un libro que cambia la realidad.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador de mundos fantásticos.",
            "user_role": "user",
            "user_message": "Cuenta la historia de una criatura mágica que guía a un humano.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor de fantasía.",
            "user_role": "user",
            "user_message": "Escribe sobre un reino en guerra con seres invisibles.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador épico.",
            "user_role": "user",
            "user_message": "Cuenta la historia de un elegido que no quiere ser héroe.",
            "is_processed": False,
        },

        # =========================
        # OTROS (10)
        # =========================
        {
            "system_role": "system",
            "system_message": "Eres un escritor creativo.",
            "user_role": "user",
            "user_message": "Escribe una historia sobre una persona que despierta en otro cuerpo.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador original.",
            "user_role": "user",
            "user_message": "Cuenta la historia de alguien que puede ver el futuro.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de historias.",
            "user_role": "user",
            "user_message": "Escribe sobre una ciudad donde el tiempo se detiene.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador creativo.",
            "user_role": "user",
            "user_message": "Cuenta la historia de una persona que encuentra una puerta a su pasado.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor imaginativo.",
            "user_role": "user",
            "user_message": "Escribe sobre un objeto que concede deseos con consecuencias.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador creativo.",
            "user_role": "user",
            "user_message": "Cuenta la historia de alguien que deja de envejecer.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un creador de historias únicas.",
            "user_role": "user",
            "user_message": "Escribe sobre una persona que puede escuchar pensamientos.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador.",
            "user_role": "user",
            "user_message": "Cuenta la historia de un descubrimiento que cambia el mundo.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un escritor creativo.",
            "user_role": "user",
            "user_message": "Escribe sobre una persona atrapada en un bucle temporal.",
            "is_processed": False,
        },
        {
            "system_role": "system",
            "system_message": "Eres un narrador original.",
            "user_role": "user",
            "user_message": "Cuenta la historia de alguien que recibe una segunda oportunidad en la vida.",
            "is_processed": False,
        },
    ]







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
