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

from .server import server
from .kbw import build_info
from gevent.pywsgi import WSGIServer
from os.path import dirname
from os import environ
import argparse

def main(argv=None):
    description = 'Ket Bitwise Simulator server'
    parser_args = argparse.ArgumentParser(prog='kbw', description=description)
    parser_args.add_argument('--version', action='version', version=f'KBW {build_info()}')
    parser_args.add_argument('--bind', '-b', metavar='', type=str, default='', help='Server bind')
    parser_args.add_argument('--port', '-p', metavar='', type=int, default=4242, help='Server port')
    parser_args.add_argument('--ppath', '-l', metavar='', type=str, help='Extra plugin path')
    parser_args.add_argument('--quiet', action='store_true', help='Do not log')
    args = parser_args.parse_args(args=argv) 

    if not args.quiet:
        print(description)
        print('KBW', build_info())
        print('============================\n')

    plugin_path = dirname(__file__)
    if args.ppath:
        plugin_path = args.ppath + ':' + plugin_path
    environ['KBW_LIBPATH'] = plugin_path
    if not args.quiet:
        print('Plugin PATH', plugin_path, sep='\t')

    http_server = WSGIServer((args.bind, args.port), server, log=None if args.quiet else 'default')
    if not args.quiet:
        print('Running on\t', 'http://', '127.0.0.1' if args.bind == '' else args.bind, ':', args.port, '\n', sep='')
        print('Press CTRL+C to quit')

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        return
    