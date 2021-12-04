from pathlib import Path, PurePath

ROOT_DIR = PurePath(__file__).parent
LOGS_DIR = Path(ROOT_DIR / "logs")
Path(LOGS_DIR).mkdir(exist_ok=True)
