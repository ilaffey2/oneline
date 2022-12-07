from sys import argv
if len(argv) != 2:
    print("Please run as oneline_compiler.py <path-to-file>")

file = open(argv[1], 'r')
lines = file.readlines() 
file.close()

file_name = argv[1].removesuffix(".py")
file = open(file_name + "_oneline.py", 'w', newline='')

evil ='import os; list(map(lambda x: os.system("echo \\"" + x + "\\" >> 10002121_tempfile.py"),['
file.write(evil)

new_lines = list(map(lambda x:"'"+ x.replace("\n","").replace("'", "\"").replace("\"","\\'") + "'", lines))
evil = ','.join(new_lines)
file.write(evil)

evil = ', \'\"\\npython3 10002121_tempfile.py; echo "made by @ilaffey2\'])); os.system("rm 10002121_tempfile.py");'
file.write(evil)