import os
import sys

current_script_dir = os.path.dirname(__file__)

script_dir = os.path.abspath(os.path.join(current_script_dir, '..', '..'))
modules_dir = os.path.join(script_dir, 'modules')

sys.path.append(script_dir)
sys.path.append(modules_dir)