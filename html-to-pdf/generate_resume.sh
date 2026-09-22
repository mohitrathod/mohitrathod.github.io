#!/usr/bin/env bash
set -euo pipefail
script_dir="$(dirname "$(readlink -f "$0")")"
exec "$script_dir/.venv/bin/python" "$script_dir/generate_resume.py" "$@"
