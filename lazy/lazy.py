import subprocess
import traceback

def p(var):
    (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
    print('%s: %s'%(text[text.find('(')+1:-1],var))

def run(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, universal_newlines=True)
    return result.stdout
