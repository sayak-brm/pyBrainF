##   Copyright 2016 Sayak Brahmachari
##
##   Licensed under the Apache License, Version 2.0 (the "License");
##   you may not use this file except in compliance with the License.
##   You may obtain a copy of the License at
##
##       http://www.apache.org/licenses/LICENSE-2.0
##
##   Unless required by applicable law or agreed to in writing, software
##   distributed under the License is distributed on an "AS IS" BASIS,
##   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##   See the License for the specific language governing permissions and
##   limitations under the License.

import code
import sys

import bfTerp

sys.ps1 = "BF> "
sys.ps2 = ">>> "
banner = "pyBrainF REPL v1.0.20161024a.\nPress Ctrl-D to quit."

class Shell(code.InteractiveConsole):
    def runsource(self, source, filename="<stdin>"):
        try:
            terp.run(source)
        except:
            self.showsyntaxerror(filename)
        return False

terp = bfTerp.Terp()
Shell().interact(banner)
