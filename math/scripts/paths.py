from __future__ import annotations

import os
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parent
MATH_ROOT = SRC_DIR.parent
REPO_ROOT = MATH_ROOT.parent

DEFAULT_MARKDOWN_ROOT = MATH_ROOT
DEFAULT_MATH_JSON_PATH = MATH_ROOT / "lib" / "math.json"
DEFAULT_TYPORA_PATH = Path(os.environ.get("TYPORA_EXE", r"C:\Software\Typora\Typora.exe"))
