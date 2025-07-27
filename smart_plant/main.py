import sys
import pathlib
import time
from typing import Optional

if __name__ == "__main__":
    sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from smart_plant.logging_config import setup_logging
setup_logging()

from smart_plant.scheduler.scheduler_service import SchedulerService
from smart_plant.db import init_db

import typer
from pathlib import Path

app = typer.Typer()

@app.command()
def start(
    tasks: Optional[Path] = typer.Option(None, "--tasks", "-t", help="Путь до файла с задачами"),
    config: Optional[Path] = typer.Option(None, "--config", "-c", help="Путь до конфигурационного файла"),
):
    """
    Start the Smart Plant application.
    Initializes the database and starts the scheduler.
    """
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


# def main():
#     init_db()
#     scheduler = SchedulerService()
#     scheduler.setup_jobs()
#     scheduler.start()
#     print("[MAIN] Scheduler started, entering idle loop")
#     try:
#         while True:
#             time.sleep(1)
#     except (KeyboardInterrupt, SystemExit):
#         print("[MAIN] Shutting down scheduler")
#         scheduler.scheduler.shutdown()


if __name__ == "__main__":
    app()
