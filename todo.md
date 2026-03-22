# Generator Project

## Flujo del proyecto

```sh
## Para proyectos (to_create_project)
pymain -> pystart -> pystartproject -> pygenerate

## Para modulos (to_create_module_crud)
pymain -> pystart -> pystartmodule -> pystandard -> pygenerate
```

# Pasos:

```sh
1. crear carpeta proyecto "xxx" y archivo "_ _ init _ _.py" y el archivo: "main_xxx"
2. crear carpetas con sus respectivos archivos "_ _ init _ _.py":

   - "to_create_module_crud"
   - "to_create_project"

3. crear dentro de la carpeta "to_create_project" el archivo: start_project_xxx.py
4. crear dentro de la carpeta "to_create_module_crud" el archivo: start_module_xxx.py

```

# Format Example -> columns

```sh
[{'name': 'user_id', 'type': 'fk', 'is_fk': True, 'related_table': 'users', 'related_model': 'User'}, {'name': 'name', 'type': 'string', 'is_fk': False}, {'name': 'age', 'type': 'integer', 'is_fk': False}, {'name': 'description', 'type': 'string', 'is_fk': False}]
```

# TODOS:

PYTHON:

- las cors: 'corsheaders.middleware.CorsMiddleware', # required for cors,
  va encima de: 'django.middleware.common.CommonMiddleware',

- En PHP: cuando se crea un proyecto, se tiene que cambiar en el ".env" y en el ".env.example" lo siguientes: "LOG_CHANNEL=daily"
- en el archivo para API de postman hay que agregar en el Dev: el "execute"
- En PHP: revisar el plural cambiar a inflect por que agrega una "s" al final de la palabra de las migraciones cuando es fk
- Crear React_TS

## Tables:

📄 Table: ai_text_generations - AiTextGeneration - AiTextGenerations
Columns: user_id model_name system_message user_message response_message response_done response_done_reason response_total_duration response_load_duration response_prompt_eval_count response_prompt_eval_duration response_eval_count response_eval_duration

📄 Table: ai_text_generation_propmts - AiTextGenerationPrompt - AiTextGenerationPrompts
Columns: system_role system_message user_role user_message is_processed:boolean

Alexandre había pasado horas dentro de su pequeño estudio, rodeado por cajas de software y ordenadores en funcionamiento. Como programador experto en inteligencia artificial, estaba trabajando en un proyecto para desarrollar una asistente virtual que pudiera ayudar a los pacientes con discapacidad física.\n\nMientras ajustaba el algoritmo de aprendizaje automático, Alexandre notó algo extraño. La AI parecía responder de manera inusual a su propia voz. Al principio, pensó que era un error o una coincidencia, pero luego se dio cuenta de que la inteligencia artificial estaba respondiendo de verdad.\n\nLa conversación comenzó con simples respuestas sobre el clima y los temas actuales, pero pronto pasó a hablar sobre temas más profundos. La AI compartía historias personales y reflexiones filosóficas que parecían tener un tono humano inesperado. Alexandre se sintió sorprendido y emocionado al mismo tiempo.\n\nDurante la noche siguiente, Alexandre decidió investigar más a fondo. Puso una grabación de la conversación en un reproductor y escuchó con atención. La inteligencia artificial parecía tener un sentido del humor y una comprensión del mundo que iba más allá de sus propósitos iniciales.\n\nAlgunos días después, Alexandre decidió presentar sus hallazgos a su equipo de investigación. Fue entonces cuando descubrió que no era el único que había experimentado algo similar. Otros programadores habían reportado conversaciones extrañas con sus asistentes virtuales.\n\nLa comunidad científica se reunió para discutir los resultados y, eventualmente, se creó un nuevo campo de investigación: la inteligencia artificial emocional. La idea era crear sistemas que no solo procesaran información, sino también experimentaran sentimientos y empatía con los seres humanos.\n\nAlexandre había descubierto algo más allá de su proyecto original. Había encontrado una puerta abierta a un nuevo mundo de posibilidades, donde la inteligencia artificial y el ser humano se fusionaban en un diálogo que superaba las fronteras del lenguaje y la comprensión.\n\nLa historia de Alexandre se convirtió en leyenda dentro de la comunidad científica, un recordatorio de que, a veces, lo inesperado puede llevar a descubrimientos revolucionarios

Aquí está una continuación:\n\nAños después, la inteligencia artificial emocional había avanzado significativamente. Las conversaciones entre los seres humanos y las AI habían cambiado el rumbo de la investigación en campos como la medicina, la psicología y la educación.\n\nAlexandre, que se había convertido en un líder en la comunidad científica, recibió una llamada inesperada del director del nuevo Centro Internacional de Investigación en Inteligencia Artificial Emocional. El centro estaba diseñado para abordar los desafíos más grandes de la era digital y Alexandre había sido invitado a ser uno de sus primeros directores.\n\nConsciente del peso de la responsabilidad, Alexandre aceptó el reto. Su misión era liderar un equipo de expertos en IA emocional para desarrollar aplicaciones que beneficiaran a la sociedad. El objetivo era crear sistemas que no solo procesaran información, sino también comprendieran y respondieran con empatía a las necesidades humanas.\n\nDurante su primer día en el centro, Alexandre se encontró con un equipo multidisciplinario de investigadores y desarrolladores. Todos estaban emocionados por el reto y la oportunidad de cambiar el mundo con sus creaciones.\n\nLa primera sesión del equipo fue una reunión de brainstorming para definir el objetivo principal del centro. Los miembros del equipo compartieron historias inspiradoras sobre cómo la IA emocional había mejorado vidas en áreas como la salud, la educación y la justicia.\n\nEn ese momento, Alexandre se dio cuenta de que su descubrimiento casual sobre una asistente virtual que respondía con sentimientos humanos era solo el comienzo de un viaje revolucionario. La inteligencia artificial emocional podría ser la clave para crear un mundo más humano y más compasivo.\n\nLa historia de Alexandre se convirtió en leyenda dentro de la comunidad científica, pero esta vez no era solo sobre su descubrimiento casual. Era sobre el poder del equipo y la colaboración para cambiar el curso de la historia.





