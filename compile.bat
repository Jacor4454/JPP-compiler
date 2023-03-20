@echo off
set /P id=Enter filename: 

mkdir compiler_logs

( 
    echo %id%
 ) > compiler_logs/filename.txt

python Jpp-Jp_compiler.py
python Jp-J_compiler.py
python J_compiler.py