from pathlib import Path
import os
import shutil
from appdirs import user_config_dir

# User editable variables
# API url
api_url = "https://api.audnex.us/books"

# output directory for cleaned metadata/folder structure
# leaving blank uses /output for docker or $USER/output for anything else
output = ""

# Number of cpus to use for jobs
cpus_to_use = ""
#

# Set defaults if no user changes
# Setup output folder defaults
if not output:
    # If using docker, default to /output folder, else $USER/output
    if Path('/output').is_dir():
        output = Path('/output')
    else:
        default_output = Path.home()
        output = Path(f"{default_output}/output")

# If using docker, default to /input/done folder, else $USER/input/done
if Path('/input').is_dir():
    junk_dir = Path('/input/done')
else:
    default_input = Path.home()
    junk_dir = Path(f"{default_input}/input/done")

# Available CPU cores to use
if not cpus_to_use:
    num_cpus = os.cpu_count()
else:
    num_cpus = cpus_to_use

# config section for docker
if Path('/config').is_dir():
    config_path = Path('/config')
else:
    appname = "m4b-merge"
    config_path = Path(user_config_dir(appname))
    Path(config_path).mkdir(
        parents=True,
        exist_ok=True
    )

# Find path to m4b-tool binary
# Check that binary actually exists
m4b_tool_bin = shutil.which('m4b-tool')
if not m4b_tool_bin:
    raise SystemExit(
        'Error: Cannot find m4b-tool binary.'
        )

# Test existence of mp4chaps
mp4chaps_bin = shutil.which('mp4chaps')
if not mp4chaps_bin:
    raise SystemExit(
        'Error: Cannot find mp4chaps binary.'
        )
###
