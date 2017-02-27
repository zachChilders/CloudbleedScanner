import sys, os
from cx_Freeze import setup, Executable

options = {
        "build_exe": {
            "include_files": [ '.\FileManager.py', '.\HistoryConnector.py', os.getenv('LOCALAPPDATA') + '\Programs\Python\Python36-32\DLLs\sqlite3.dll'],
        }
    }

setup(
    name = "CloudBleedScanner",
    version = "1.0",
    description = "Scans your history for leaked websites",
    options = options,
    executables = [Executable("CloudBleedScanner.py")])