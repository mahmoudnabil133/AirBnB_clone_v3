#!/bin/bash

# Define virtual environment name (replace with your actual name)
venv_name="/home/mahmoudnabil/myvenv/bin/python"

# Check if virtual environment exists
if [ ! -d "$venv_name" ]; then
  echo "Virtual environment '$venv_name' not found. Please create it first."
  exit 1
fi

# Activate virtual environment
source "$venv_name/bin/activate" || {
  echo "Failed to activate virtual environment '$venv_name'."
  exit 1
}

# Check if fabfile.py exists
if [ ! -f "fabfile.py" ]; then
  echo "fabfile.py not found in the current directory."
  echo "Please create a fabfile.py with your deployment tasks."
  exit 1
fi

# Check if Fabric is installed
if ! command -v fab &> /dev/null; then
  echo "Fabric not found in virtual environment '$venv_name'."
  echo "Installing Fabric..."
  pip install Fabric
fi

# Execute your Fabric command (replace with your actual command)
fab do_deploy:archive_path=versions/web_static_20240310095451.tgz -u ubuntu -i ~/.ssh/id_rsa

# Deactivate virtual environment (optional)
# deactivate
