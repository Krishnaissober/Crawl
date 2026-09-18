"""Shared SQLite location for desktop, Docker, and ephemeral Vercel instances."""
import os
import tempfile
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
configured_dir = os.getenv('LIBRECRAWL_DATA_DIR', '').strip()
if configured_dir:
    DATA_DIR = Path(configured_dir).expanduser().resolve()
elif os.getenv('VERCEL') == '1':
    DATA_DIR = Path(tempfile.gettempdir()) / 'librecrawl' / 'data'
else:
    DATA_DIR = PROJECT_DIR / 'data'

DB_FILE = str(DATA_DIR / 'users.db')
