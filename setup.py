#python
import sys
from cx_Freeze import setup, Executable
base = None
base = "Win32GUI"
setup(
        name = "门户登陆",
        version = "0.1 alpha",
        description = "天津理工大学信息门户登陆工具",
        executables =[Executable ("main.py")]
           )