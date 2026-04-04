# Prompts


```sh



```






## Tables:

📄 Table: ai_prompt_generations - AiPromptGeneration - AiPromptGenerations
Columns: system_role system_message user_role user_message is_text_processed:boolean is_image_processed:boolean is_video_processed:boolean

📄 Table: ai_text_generations - AiTextGeneration - AiTextGenerations
Columns: ai_prompt_generation_id:fk model_name response_message:text response_done response_done_reason response_total_duration response_load_duration response_prompt_eval_count response_prompt_eval_duration response_eval_count response_eval_duration

📄 Table: ai_image_generations - AiImageGeneration - AiImageGenerations
Columns: ai_prompt_generation_id:fk comfyui_prompt_id comfyui_output_path mime_type width:integer height:integer image_url
