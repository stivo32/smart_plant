import sys
import pathlib
import time

if __name__ == "__main__":
    sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from app.logging_config import setup_logging
setup_logging()

from app.scheduler.scheduler_service import SchedulerService
from app.db import init_db


def main():
    init_db()
    scheduler = SchedulerService()
    scheduler.setup_jobs()
    scheduler.start()
    print("[MAIN] Scheduler started, entering idle loop")
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("[MAIN] Shutting down scheduler")
        scheduler.scheduler.shutdown()


if __name__ == "__main__":
    main()
