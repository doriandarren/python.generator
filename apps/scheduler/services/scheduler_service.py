from apps.scheduler.jobs.ai_generation_job import AIGenerationJob


class SchedulerService:
    def run(self):
        jobs = [
            AIGenerationJob(),
        ]

        for job in jobs:
            try:
                job.handle()
            except Exception as e:
                print(f"Error ejecutando {job.__class__.__name__}: {str(e)}")