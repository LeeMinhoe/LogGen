
import os
import inspect

# Target Dir Setting
# Target file Setting
main_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/main.py'
print(main_path)
os.system("python3.5 " + main_path + " -d ./../99_JSON -f *.json -t 10 -s 1 -r 2 4 -g 5 2 -l 1")
print()

os.system("python3.5 " + main_path + " -d ./../99_JSON -f *.json -l 1")
print()

os.system("python3.5 " + main_path + " -d ./../99_JSON -f *.json ")
print()

os.system("python3.5 " + main_path + " -d ./../99_JSON -f *.json -t 10 -l 1")
print()

os.system("python3.5 " + main_path + " -d ./../99_JSON -f *.json -s 1 -l 1")
print()

os.system("python3.5 " + main_path + " -d ./../99_JSON -f *.json -r 2 4 -l 1")
print()

os.system("python3.5 " + main_path + " -d ./../99_JSON -f *.json -g 5 2 -l 1")
print()

