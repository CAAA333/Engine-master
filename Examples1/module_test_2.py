# default paths (either change here or use the interface below)
ore_exe_path = 'C:\\ORE\\Engine-master\\App\\bin\\x64\\Release\\ore.exe'
ore_xml = 'C:\\ORE\\Engine-master\\Examples\\Example_2\\Input\\ore.xml'

import subprocess
import os
# from ipywidgets import Text, Button

# ore_path_selector = Text(description='ORE Path:', value=ore_exe_path, width=200)
# xml_selector = Text(description='XML File:', value=ore_xml, width=200)

def launch_ore():
    cwd = os.getcwd() # save directory of the jupyter notebook
    config_path = os.path.dirname(os.path.dirname(ore_xml))
    os.chdir(config_path) # navigate to ore config folder
    command = [ore_exe_path, os.path.join(os.path.join(config_path, 'Input'),'ore.xml')]
    print("Starting ORE run... please wait...")
    p = subprocess.Popen(command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    os.chdir(cwd) # go back to jupyter notebook
    print("ORE run successful!")
    global npv_cube_filename
    npv_cube_filename = os.path.join(os.path.join(config_path, 'Output'),'rawcube.csv')

launch_ore()