from django.core.management.base import BaseCommand

from apps.ai_prompt_categories.enums.ai_prompt_category_enum import AiPromptCategoryEnum
from apps.ai_prompt_categories.models import AiPromptCategory
from apps.ai_prompt_generations.data.data_prompt import get_data_prompts
from apps.ai_prompt_generations.models import AiPromptGeneration



class Command(BaseCommand):
    help = 'Seed default data for the devs app'

    def handle(self, *args, **options):
        
        self.stdout.write(self.style.SUCCESS('Seeding default data...'))
        
        self.create_categories()
        
        self.create_prompts()
        
        self.stdout.write(self.style.SUCCESS('Default data seeded successfully!'))
        

        
    
    def create_categories(self):
        
        self.stdout.write(self.style.SUCCESS('Creating categories...'))
        
        categories = [
            {
                "id": AiPromptCategoryEnum.CHILDREN_STORIES_ID,
                "name": AiPromptCategoryEnum.CHILDREN_STORIES_NAME,
                "slug": AiPromptCategoryEnum.CHILDREN_STORIES_SLUG,
                "description": AiPromptCategoryEnum.CHILDREN_STORIES_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.FABLES_ID,
                "name": AiPromptCategoryEnum.FABLES_NAME,
                "slug": AiPromptCategoryEnum.FABLES_SLUG,
                "description": AiPromptCategoryEnum.FABLES_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.FANTASY_ID,
                "name": AiPromptCategoryEnum.FANTASY_NAME,
                "slug": AiPromptCategoryEnum.FANTASY_SLUG,
                "description": AiPromptCategoryEnum.FANTASY_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.SCIENCE_FICTION_ID,
                "name": AiPromptCategoryEnum.SCIENCE_FICTION_NAME,
                "slug": AiPromptCategoryEnum.SCIENCE_FICTION_SLUG,
                "description": AiPromptCategoryEnum.SCIENCE_FICTION_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.DYSTOPIA_ID,
                "name": AiPromptCategoryEnum.DYSTOPIA_NAME,
                "slug": AiPromptCategoryEnum.DYSTOPIA_SLUG,
                "description": AiPromptCategoryEnum.DYSTOPIA_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.HORROR_ID,
                "name": AiPromptCategoryEnum.HORROR_NAME,
                "slug": AiPromptCategoryEnum.HORROR_SLUG,
                "description": AiPromptCategoryEnum.HORROR_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.PSYCHOLOGICAL_HORROR_ID,
                "name": AiPromptCategoryEnum.PSYCHOLOGICAL_HORROR_NAME,
                "slug": AiPromptCategoryEnum.PSYCHOLOGICAL_HORROR_SLUG,
                "description": AiPromptCategoryEnum.PSYCHOLOGICAL_HORROR_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.PARANORMAL_ID,
                "name": AiPromptCategoryEnum.PARANORMAL_NAME,
                "slug": AiPromptCategoryEnum.PARANORMAL_SLUG,
                "description": AiPromptCategoryEnum.PARANORMAL_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.SUSPENSE_ID,
                "name": AiPromptCategoryEnum.SUSPENSE_NAME,
                "slug": AiPromptCategoryEnum.SUSPENSE_SLUG,
                "description": AiPromptCategoryEnum.SUSPENSE_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.MYSTERY_ID,
                "name": AiPromptCategoryEnum.MYSTERY_NAME,
                "slug": AiPromptCategoryEnum.MYSTERY_SLUG,
                "description": AiPromptCategoryEnum.MYSTERY_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.DETECTIVES_ID,
                "name": AiPromptCategoryEnum.DETECTIVES_NAME,
                "slug": AiPromptCategoryEnum.DETECTIVES_SLUG,
                "description": AiPromptCategoryEnum.DETECTIVES_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.THRILLER_ID,
                "name": AiPromptCategoryEnum.THRILLER_NAME,
                "slug": AiPromptCategoryEnum.THRILLER_SLUG,
                "description": AiPromptCategoryEnum.THRILLER_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.ADVENTURE_ID,
                "name": AiPromptCategoryEnum.ADVENTURE_NAME,
                "slug": AiPromptCategoryEnum.ADVENTURE_SLUG,
                "description": AiPromptCategoryEnum.ADVENTURE_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.ACTION_ID,
                "name": AiPromptCategoryEnum.ACTION_NAME,
                "slug": AiPromptCategoryEnum.ACTION_SLUG,
                "description": AiPromptCategoryEnum.ACTION_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.SUPERHEROES_ID,
                "name": AiPromptCategoryEnum.SUPERHEROES_NAME,
                "slug": AiPromptCategoryEnum.SUPERHEROES_SLUG,
                "description": AiPromptCategoryEnum.SUPERHEROES_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.STRANGE_CREATURES_ID,
                "name": AiPromptCategoryEnum.STRANGE_CREATURES_NAME,
                "slug": AiPromptCategoryEnum.STRANGE_CREATURES_SLUG,
                "description": AiPromptCategoryEnum.STRANGE_CREATURES_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.MONSTERS_ID,
                "name": AiPromptCategoryEnum.MONSTERS_NAME,
                "slug": AiPromptCategoryEnum.MONSTERS_SLUG,
                "description": AiPromptCategoryEnum.MONSTERS_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.MYTHOLOGY_ID,
                "name": AiPromptCategoryEnum.MYTHOLOGY_NAME,
                "slug": AiPromptCategoryEnum.MYTHOLOGY_SLUG,
                "description": AiPromptCategoryEnum.MYTHOLOGY_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.DRAMA_ID,
                "name": AiPromptCategoryEnum.DRAMA_NAME,
                "slug": AiPromptCategoryEnum.DRAMA_SLUG,
                "description": AiPromptCategoryEnum.DRAMA_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.SELF_IMPROVEMENT_ID,
                "name": AiPromptCategoryEnum.SELF_IMPROVEMENT_NAME,
                "slug": AiPromptCategoryEnum.SELF_IMPROVEMENT_SLUG,
                "description": AiPromptCategoryEnum.SELF_IMPROVEMENT_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.FRIENDSHIP_ID,
                "name": AiPromptCategoryEnum.FRIENDSHIP_NAME,
                "slug": AiPromptCategoryEnum.FRIENDSHIP_SLUG,
                "description": AiPromptCategoryEnum.FRIENDSHIP_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.ROMANCE_ID,
                "name": AiPromptCategoryEnum.ROMANCE_NAME,
                "slug": AiPromptCategoryEnum.ROMANCE_SLUG,
                "description": AiPromptCategoryEnum.ROMANCE_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.YOUNG_ADULT_ROMANCE_ID,
                "name": AiPromptCategoryEnum.YOUNG_ADULT_ROMANCE_NAME,
                "slug": AiPromptCategoryEnum.YOUNG_ADULT_ROMANCE_SLUG,
                "description": AiPromptCategoryEnum.YOUNG_ADULT_ROMANCE_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.COMEDY_ID,
                "name": AiPromptCategoryEnum.COMEDY_NAME,
                "slug": AiPromptCategoryEnum.COMEDY_SLUG,
                "description": AiPromptCategoryEnum.COMEDY_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.SATIRE_ID,
                "name": AiPromptCategoryEnum.SATIRE_NAME,
                "slug": AiPromptCategoryEnum.SATIRE_SLUG,
                "description": AiPromptCategoryEnum.SATIRE_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.HISTORICAL_ID,
                "name": AiPromptCategoryEnum.HISTORICAL_NAME,
                "slug": AiPromptCategoryEnum.HISTORICAL_SLUG,
                "description": AiPromptCategoryEnum.HISTORICAL_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.FICTIONAL_HISTORICAL_ID,
                "name": AiPromptCategoryEnum.FICTIONAL_HISTORICAL_NAME,
                "slug": AiPromptCategoryEnum.FICTIONAL_HISTORICAL_SLUG,
                "description": AiPromptCategoryEnum.FICTIONAL_HISTORICAL_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.TECHNOLOGY_ID,
                "name": AiPromptCategoryEnum.TECHNOLOGY_NAME,
                "slug": AiPromptCategoryEnum.TECHNOLOGY_SLUG,
                "description": AiPromptCategoryEnum.TECHNOLOGY_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.ARTIFICIAL_INTELLIGENCE_ID,
                "name": AiPromptCategoryEnum.ARTIFICIAL_INTELLIGENCE_NAME,
                "slug": AiPromptCategoryEnum.ARTIFICIAL_INTELLIGENCE_SLUG,
                "description": AiPromptCategoryEnum.ARTIFICIAL_INTELLIGENCE_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.CYBERPUNK_ID,
                "name": AiPromptCategoryEnum.CYBERPUNK_NAME,
                "slug": AiPromptCategoryEnum.CYBERPUNK_SLUG,
                "description": AiPromptCategoryEnum.CYBERPUNK_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.PHILOSOPHICAL_ID,
                "name": AiPromptCategoryEnum.PHILOSOPHICAL_NAME,
                "slug": AiPromptCategoryEnum.PHILOSOPHICAL_SLUG,
                "description": AiPromptCategoryEnum.PHILOSOPHICAL_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.EXISTENTIAL_ID,
                "name": AiPromptCategoryEnum.EXISTENTIAL_NAME,
                "slug": AiPromptCategoryEnum.EXISTENTIAL_SLUG,
                "description": AiPromptCategoryEnum.EXISTENTIAL_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.EVERYDAY_LIFE_ID,
                "name": AiPromptCategoryEnum.EVERYDAY_LIFE_NAME,
                "slug": AiPromptCategoryEnum.EVERYDAY_LIFE_SLUG,
                "description": AiPromptCategoryEnum.EVERYDAY_LIFE_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.MAGICAL_REALISM_ID,
                "name": AiPromptCategoryEnum.MAGICAL_REALISM_NAME,
                "slug": AiPromptCategoryEnum.MAGICAL_REALISM_SLUG,
                "description": AiPromptCategoryEnum.MAGICAL_REALISM_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.TIME_TRAVEL_ID,
                "name": AiPromptCategoryEnum.TIME_TRAVEL_NAME,
                "slug": AiPromptCategoryEnum.TIME_TRAVEL_SLUG,
                "description": AiPromptCategoryEnum.TIME_TRAVEL_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.ALTERNATE_UNIVERSES_ID,
                "name": AiPromptCategoryEnum.ALTERNATE_UNIVERSES_NAME,
                "slug": AiPromptCategoryEnum.ALTERNATE_UNIVERSES_SLUG,
                "description": AiPromptCategoryEnum.ALTERNATE_UNIVERSES_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.APOCALYPSE_ID,
                "name": AiPromptCategoryEnum.APOCALYPSE_NAME,
                "slug": AiPromptCategoryEnum.APOCALYPSE_SLUG,
                "description": AiPromptCategoryEnum.APOCALYPSE_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.POST_APOCALYPTIC_ID,
                "name": AiPromptCategoryEnum.POST_APOCALYPTIC_NAME,
                "slug": AiPromptCategoryEnum.POST_APOCALYPTIC_SLUG,
                "description": AiPromptCategoryEnum.POST_APOCALYPTIC_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.SURVIVAL_ID,
                "name": AiPromptCategoryEnum.SURVIVAL_NAME,
                "slug": AiPromptCategoryEnum.SURVIVAL_SLUG,
                "description": AiPromptCategoryEnum.SURVIVAL_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.SPACE_ID,
                "name": AiPromptCategoryEnum.SPACE_NAME,
                "slug": AiPromptCategoryEnum.SPACE_SLUG,
                "description": AiPromptCategoryEnum.SPACE_DESCRIPTION,
            },
            {
                "id": AiPromptCategoryEnum.OTHERS_ID,
                "name": AiPromptCategoryEnum.OTHERS_NAME,
                "slug": AiPromptCategoryEnum.OTHERS_SLUG,
                "description": AiPromptCategoryEnum.OTHERS_DESCRIPTION,
            },
        ]
        
        
        for category_data in categories:
            AiPromptCategory.objects.update_or_create(
                id=category_data["id"],
                defaults={
                    "name":category_data["name"],
                    "description":category_data["description"],
                    "slug":category_data["slug"],
                }
            )
            
        self.stdout.write(self.style.SUCCESS(f'Categorías creadas: {len(categories)}'))
        



    def create_prompts(self):
        
        self.stdout.write(self.style.SUCCESS('Cargando prompts...'))
        
        
        for payload in get_data_prompts():
            
            AiPromptGeneration.objects.get_or_create(
                ai_prompt_category_id=payload.get("category_id"),
                system_role=payload.get("system_role", ""),
                system_message=payload.get("system_message", ""),
                user_role=payload.get("user_role", ""),
                user_message=payload.get("user_message", ""),
            )
            
            
            
            
        self.stdout.write(self.style.SUCCESS(f'Prompts creados: {len(get_data_prompts())}'))
        
        