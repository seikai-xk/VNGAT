#!D:\pythonObject\VNGAT\g_vn\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sqlparse==0.3.1','console_scripts','sqlformat'
__requires__ = 'sqlparse==0.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sqlparse==0.3.1', 'console_scripts', 'sqlformat')()
    )
