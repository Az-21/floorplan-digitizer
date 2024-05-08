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
3. [Blender](https://www.blender.org/download/) to view 3D floorplan.

> [!NOTE]
> The program is tested using Potrace `v1.16`, Typst `v0.11`, Blender `v4.1`. Future (and older) releases may introduce breaking changes.

### Configuration
- Open `config.json` in root of `floorplan-digitizer` project.
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
- Open `config.json` in root of `floorplan-digitizer` project.
- Set `filename` to the name of floorplan image to work upon (eg: `fp.png`).
- [Optional] Change value of `threshold_value` to target darker shades.
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

## Sample I/O
### Input
![Input Image](https://ucarecdn.com/3e4865f0-9a3e-448d-a638-00ab611c1792/floorplaninput.jpeg)

### Config Parameters
`config.json` parameters used to process the sample input image. Different images with different resolutions and black levels will require different parameters.
```json
{
  "threshold_value": 100,
  "thickness_reduction_iterations": 5,
  "thickness_increase_iterations": 3,
}
```
> [!NOTE]
> Lower resolution images will require fewer `thickness_reduction_iterations`. Setting this parameter too high will erase everything, producing a blank image.

### Output
![Output in Blender](https://ucarecdn.com/106fe2d6-6d94-44ed-809a-2bc1772207a9/floorplanoutput.jpeg)
