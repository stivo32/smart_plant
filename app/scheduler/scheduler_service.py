import os
import json
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.util import ref_to_obj

CONFIG_PATH = "tasks.json"

class SchedulerService:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.config = self._load_or_create_config()

    def _load_or_create_config(self):
        if not os.path.exists(CONFIG_PATH):
            default_config = {"jobs": []}
            with open(CONFIG_PATH, "w") as f:
                json.dump(default_config, f, indent=2)
            return default_config
        with open(CONFIG_PATH) as f:
            return json.load(f)
        
    def setup_jobs(self):
        for job in self.config.get("jobs", []):
            func = ref_to_obj(job["func"])
            job_args = {k: v for k, v in job.items() if k not in ["id", "func"]}
            self.scheduler.add_job(func, id=job["id"], **job_args)

    def start(self):
        self.scheduler.start()