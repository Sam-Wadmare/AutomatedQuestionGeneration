# Packaging the Updated Project as ZIP

Generate a distributable ZIP from the repo root (excluding `.git`, caches, and existing zip):

```bash
python - <<'PY'
from pathlib import Path
import zipfile

root = Path('.')
zip_path = root / 'AutomatedQuestionGeneration_updated.zip'
exclude_dirs = {'.git', '__pycache__', '.pytest_cache', '.venv'}
exclude_suffixes = {'.pyc'}

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for p in root.rglob('*'):
        rel = p.relative_to(root)
        if any(part in exclude_dirs for part in rel.parts):
            continue
        if p.is_dir():
            continue
        if p.suffix in exclude_suffixes:
            continue
        if p.name == 'AutomatedQuestionGeneration_updated.zip':
            continue
        zf.write(p, rel.as_posix())

print(zip_path)
PY
```
