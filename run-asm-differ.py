#!/usr/bin/env -S uv run
import sys
import subprocess
exit(subprocess.call([sys.executable, "asm-differ/diff.py", *sys.argv[1:]]))
