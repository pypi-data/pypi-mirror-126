#  Copyright 2020, 2021 Evandro Chagas Ribeiro da Rosa <evandro.crr@posgrad.ufsc.br>
#  Copyright 2020, 2021 Rafael de Santiago <r.santiago@ufsc.br>
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from .kbw import kbw, set_plugin_path, set_seed
from .script import main
from multiprocessing import Process
from os import environ
from os.path import dirname
from random import randint

__all__ = ['kbw', 'set_plugin_path', 'set_seed', 'plugin_path']

plugin_path = dirname(__file__)
set_plugin_path(plugin_path)
environ['KET_PYCALL'] = plugin_path+'/ket_pycall_interpreter'

seed = randint(0, 2**31)
set_seed(seed)

def start_server(quiet=True, **kwargs) -> Process:
    """Start the KBW server in a new Process"""
    quiet = ['--quiet'] if quiet else []
    args = [f'--{arg}={kwargs[arg]}' for arg in kwargs] 
    p = Process(name='KBW Server', target=main, args=(quiet+args,))
    p.start()
    return p
