# Floorplan Digitizer
🏗️ Image processing utility to digitize floorplans

## Setup Environment
- Install [Miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#miniforge3) to manage python libraries and environments.
- Open "miniforge3 Prompt" (search in Start menu).
- Run the following commands to setup python and required libraries.

```sh
# Ensure mamba is up-to-date
mamba upgrade --all

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

## External Dependencies
Extract the following external dependencies and copy the path of their executables (`.exe`).

1. [Potrace](https://potrace.sourceforge.net/#downloading) to trace cleaned up floorplan images as scalable vector graphic.
2. [Typst](https://github.com/typst/typst/releases/latest) to generate PDF with floorplan insights.

> [!NOTE]
> The program is tested using Potrace `v1.16` and Typst `v0.11`. Future releases may introduce breaking changes.

### Configuration
- Open `config/config.json` in `floorplan-digitizer`.
- Set the `potrace_path` to the absolute path of `potrace.exe`.
- Set the `typst_path` to the absolute path of `typst.exe`.

> [!WARNING]
> Windows uses `\` as path separator which is also an escape character. Either change `\` to `/` or `\` to `\\`.
>
> `"C:\Dev\Programs\Typst\typst.exe"` ❌
>
> `"C:/Dev/Programs/Typst/typst.exe"` ✅
>
> `"C:\\Dev\\Programs\\Typst\\typst.exe"` ✅

## Run Program
### Floorplan Image
- Place floorplan image inside `input` folder.

### Configuration
- Open `config/config.json` in `floorplan-digitizer`.
- Set `filename` to the name of floorplan image to work upon (eg: `fp.png`).
- [Optional] Change value of `threshold_value` to target darker shades. Increasing this value will allow lighter shades.
- [Optional] Change value of `thickness` to change the thickness of walls.

### Run
Open terminal in the root of `floorplan-digitizer` and run the following command.
```sh
C:/Users/Username/miniforge3/envs/floorplan/python.exe .\main.py
#          ^ Replace this with your username
```

> [!NOTE]
> If you have installed miniforge3 in a custom location (or are using Mac/Linux), then you'll have to change the path of `python.exe` from `floorplan` virtual environment accordingly.

### Blender
- The program will generate a `blender.py` script in `output` folder.
- Copy-paste this script in the `Scripting` tab of Blender.
- Run the script **in Blender** to generate 3D model of floorplan.
