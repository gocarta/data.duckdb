# Stop the script if any command fails (equivalent to -e)
$ErrorActionPreference = "Stop"

# Run the command
uv run --env-file .env main.py
