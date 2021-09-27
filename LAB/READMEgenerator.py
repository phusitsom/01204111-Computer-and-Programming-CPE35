import os
from typing import List

lab_folders:List[str] = [directory for directory in os.listdir() if directory.startswith('L')][1:]

for lf in lab_folders:
    for dir_name in (dn for dn in os.listdir(lf) if not dn.endswith('.py')):
        fol = os.path.join(lf, dir_name)
        
        try:
            with open(os.path.join(fol,'README.md'), 'w') as file:
                file.write('')
        except: pass
    
    for py_fn in (fn for fn in os.listdir(lf) if fn.endswith('.py')):
        
        dir_name = py_fn[:-3]
        py_path = os.path.join(lf, py_fn)
        fol = os.path.join(lf, dir_name)
        
        try:
            os.mkdir(fol)
            os.rename(py_path, os.path.join(fol, py_fn))
            with open(os.path.join(fol,'README.md'), 'w') as file:
                file.write('')
        except: pass
    