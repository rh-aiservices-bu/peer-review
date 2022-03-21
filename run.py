import time
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from datetime import datetime
import inquirer

notebook_path = 'notebooks/'
reports_path = 'reports/'
notebooks = ['01-explore-data.ipynb', '02-build-features.ipynb', '03-train-model.ipynb', '04-tune-model.ipynb', '05-model-inference.ipynb']
date = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")
os.mkdir(reports_path+'run_' + date)

#for file in notebooks:
#    with open(notebook_path + file) as f:
#        nb = nbformat.read(f, as_version=4)
#    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
#    ep.preprocess(nb, {'metadata': {'path': notebook_path}})
#    with open(reports_path +'run_' + date + '/' + file, 'w', encoding='utf-8') as f:
#        nbformat.write(nb, f)

def execute_notebook(notebook, timeout=600):
    with open(notebook_path + notebook) as f:
        nb = nbformat.read(f, as_version=4) 
    ep = ExecutePreprocessor(timeout=timeout, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': notebook_path}})
        
    with open(reports_path +'run_' + date + '/' + notebook, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Execute notebook - " + notebook + ":Complete!")
    print("Please check the rerun results here: " + reports_path +'run_' + date + '/' + notebook)


def select_operation():
    questions = [
        inquirer.List('notebook',
                    message="Which notebook would you like to rerun?",
                    choices=['01-explore-data.ipynb', '02-build-features.ipynb', '03-train-model.ipynb', '04-tune-model.ipynb', '05-model-inference.ipynb'],
                ),
    ]
    answers = inquirer.prompt(questions)
    return answers


result = select_operation()
execute_notebook(result["notebook"], 600)

while (True):
    continue_run = {
        inquirer.Confirm('continue',
                         message="Would you like to continue ?" ,
                         default=True),
    }
    choice = inquirer.prompt(continue_run)
    if ( not choice["continue"]):
        print("Exiting now..!")
        break;
    else:
        result = select_operation()
        execute_notebook(result["notebook"], 600)
        print(result["notebook"])
