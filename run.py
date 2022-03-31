import time
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from datetime import datetime
import inquirer
import sys
sys.path.append("lib/")
from getConfig import *
config = getConfig("")
config.cleanup(config.notebooks_path)

notebook_path = 'notebooks/'
notebooks = ['01-explore-data.ipynb', '02-build-features.ipynb', '03-train-model.ipynb', '04-tune-model.ipynb', '05-model-inference.ipynb', 'all']


def execute_notebook(notebook_list, timeout=None):
    for notebook in notebook_list:
        print("Running notebook: " + notebook)
        with open(notebook_path + notebook) as f:
            nb = nbformat.read(f, as_version=4) 
        ep = ExecutePreprocessor(timeout=timeout, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': notebook_path}})
        if not os.path.exists(config.notebooks_path):
            os.makedirs(config.notebooks_path)
        with open(config.notebooks_path + notebook, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("Execute notebook - " + notebook + ":Complete!")
        print("Please check the rerun results here: " + config.notebooks_path + notebook)


def select_operation():
    questions = [
        inquirer.List('notebook',
                    message="Which notebook would you like to rerun?",
                    choices=['01-explore-data.ipynb', '02-build-features.ipynb', '03-train-model.ipynb', '04-tune-model.ipynb', '05-model-inference.ipynb', 'all'],
                ),
    ]
    answers = inquirer.prompt(questions)
    return answers

def create_nb_list_and_run():
    nb = []
    result = select_operation()
    if result["notebook"] == 'all':
        nb = notebooks[:5]
    else:
        nb.append(result["notebook"])
    execute_notebook(nb, None)

while (True):
    create_nb_list_and_run()
    continue_run = {
        inquirer.Confirm('continue',
                         message="Would you like to continue ?" ,
                         default=True),
    }
    choice = inquirer.prompt(continue_run)
    if ( not choice["continue"]):
        print("Exiting now..!")
        break;