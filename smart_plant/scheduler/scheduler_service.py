import json
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.util import ref_to_obj
from smart_plant.config import SCHEDULER_CONFIG_FILE


class SchedulerService:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.config = self._load_config()

    def _load_config(self):
        if not SCHEDULER_CONFIG_FILE.exists():
            raise FileNotFoundError(f"Scheduler config file not found: {SCHEDULER_CONFIG_FILE}")
        return json.loads(SCHEDULER_CONFIG_FILE.read_text())
        
    def setup_jobs(self):
        for job in self.config.get("jobs", []):
            func = ref_to_obj(job["func"])
            job_args = {k: v for k, v in job.items() if k not in ["id", "func"]}
            self.scheduler.add_job(func, id=job["id"], **job_args)

    def start(self):
        self.scheduler.start()