# This file is part of stable-diffusion-webui (https://github.com/sd-webui/stable-diffusion-webui/).

# Copyright 2022 sd-webui team.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
import os, time

# USER CHANGABLE ARGUMENTS

# Change to `True` if you wish to enable these common arguments

# Run upscaling models on the CPU
extra_models_cpu = False

# Automatically open a new browser window or tab on first launch
open_in_browser = False

# Run Stable Diffusion in Optimized Mode - Only requires 4Gb of VRAM, but is significantly slower
optimized = False

# Run in Optimized Turbo Mode - Needs more VRAM than regular optimized mode, but is faster
optimized_turbo = False

# Creates a public xxxxx.gradio.app share link to allow others to use your interface (requires properly forwarded ports to work correctly)
share = False

# Generate tiling images
tiling = False

# Enter other `--arguments` you wish to use - Must be entered as a `--argument ` syntax
additional_arguments = ""





# BEGIN RELAUNCHER PYTHON CODE

common_arguments = ""

if extra_models_cpu == True:
    common_arguments += "--extra-models-cpu "
if optimized_turbo == True:
    common_arguments += "--optimized-turbo "
if optimized == True:
    common_arguments += "--optimized "
if tiling == True:
    common_arguments += "--tiling "
if share == True:
    common_arguments += "--share "

if open_in_browser == True:
    inbrowser_argument = "--inbrowser "
else:
    inbrowser_argument = ""

n = 0
while True:
    if n == 0:
        print('Relauncher: Launching...')
        os.system(f"python scripts/webui.py {common_arguments} {inbrowser_argument} {additional_arguments}")
        
    else:
        print(f'\tRelaunch count: {n}')
        print('Relauncher: Launching...')
        os.system(f"python scripts/webui.py {common_arguments} {additional_arguments}")
    
    n += 1
    if n > 100:
        print ('Too many relaunch attempts. Aborting...')
        break
    print('Relauncher: Process is ending. Relaunching in 1s...')
    time.sleep(1)
