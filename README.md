# Floorplan Digitizer
🏗️ Image processing utility to digitize floorplans

## Setup Environment
```sh
# Create a new virtual environment
mamba create -n floorplan
mamba activate floorplan

# Add python
mamba install python=3.12

# Add dependencies
mamba install numpy

# Add dev dependencies
mamba install ruff loguru

# Install opencv (not available via mamba/conda)
pip install opencv-python
```

### Updating Packages
```sh
mamba activate floorplan
mamba upgrade --all
pip install opencv-python --upgrade
```
