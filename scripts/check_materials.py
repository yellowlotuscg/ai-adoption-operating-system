"""Offline structural checks, not proof of training effectiveness."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
files = sorted(root.rglob("*.md"))
for path in files:
    text = path.read_text()
    assert "\u2014" not in text, str(path)
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        assert (path.parent / target.split("#")[0]).is_file(), (path, target)
required = {
    "curriculum/03-facilitator-guide.md": ["proposed", "Role variations", "Deployment handoff"],
    "curriculum/04-source-checking-lab.md": ["S1", "S2", "S3", "Facilitator answer key", "synthetic"],
    "templates/assessment.md": ["privacy", "approval", "not measured"],
    "templates/pilot-feedback-handoff.md": ["Stop condition", "manual", "Do not insert made-up results"],
}
for name, markers in required.items():
    text = (root / name).read_text()
    for marker in markers:
        assert marker in text, (name, marker)
print(f"PASS: {len(files)} Markdown files; local links and required workshop sections checked")
