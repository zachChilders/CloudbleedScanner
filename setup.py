import os
import sys

from cx_Freeze import Executable, setup

options = {
        "build_exe": {
            "include_files": [ '.\lib\FileManager.py', '.\lib\HistoryConnector.py', os.getenv('LOCALAPPDATA') + '\Programs\Python\Python36-32\DLLs\sqlite3.dll'],
        }
    }

setup(
    name = "CloudBleedScanner",
    version = "1.0",
    description = "Scans your history for leaked websites",
    options = options,
    executables = [Executable("CloudBleedScanner.py")])
