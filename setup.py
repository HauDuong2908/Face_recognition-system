import cx_Freeze
import sys
import os

base = None

if sys.platform == "win32":
    base = "Win32GUI"

os.environ[
    "TCL_LIBRARY"
] = r"C:\Users\hau09\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ[
    "TK_LIBRARY"
] = r"C:\Users\hau09\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name="Facial Recognition Software",
    options={
        "build_exe": {
            "packages": ["tkinter", "os"],
            "include_files": [
                "face.ico",
                "tcl86t.dll",
                "tk86t.dll",
                "college_images",
                "data",
                "database",
                "attendance.csv",
            ],
        }
    },
    version="1.0",
    description="Face Recognition Automatic Attendace System ",
    executables=executables,
)
