def ImportModule(name: str):
    try:
        import name
        print('Good Import')
    except ImportError:
        print('Error Import')
        import sys, os
        import subprocess
        subprocess.call([sys.executable, '-m', 'pip', 'install', name])

ImportModule('cv')
