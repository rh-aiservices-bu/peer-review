Peer-review
==============================

A structured project with data, notebooks, models and workflow to allow scientists to consistently replicate experiments. A typical data science experiment includes exploring data, building features (also called feature engineering), training multiple models inorder to compare and select one, optimizing the trained model through hyperparameter tuning and finally running prediction on new data (model inference). The notebooks have been named and numbered to easily identify the order in the workflow.

## Project Organization
```
README.md
LICENSE
config                          <- store path, data, model and run related configurations

data                            <- folder for training and test dataset
   └── input                    <- raw input data
   └── train-test               <- transformed input data for training and testing
   └── inference                <- data for inference

models                          <- folder to store ml models
   └── trained                  <- subfolder to store trained ml models
   └── tuned                    <- subfolder to store tuned ml models

notebooks                       <- folder for various notebooks
   └── 01-explore-data.ipynb    <- explore and visualize data
   └── 02-build-features.ipynb  <- clean and transform data for training and testing
   └── 03-train-model.ipynb     <- train multiple models and compare them
   └── 04-tune-model.ipynb      <- optimize ml model through hyperparameter tuning
   └── 05-model-inference.ipynb <- run prediction on new data

experiments                     <- folder to store artifacts from various runs
   └── experiment_0             <- folder to store results for each run.
           └── plots            <- contains plots from explore data notebook
           └── train-test       <- train and test data from build features notebook    
       └── models
           └── trained          <- trained models from train model notebook
           └── tuned            <- optimized model from tune model notebook
       └── prediction results   <- prediction results from model inference notebook

prediction.py                   <- the predict function called from Flask
wsgi.py                         <- basic Flask application
flask_run.ipynb                 <- run Flask application on localhost
flask_test.ipynb                <- test Flask application on localhost
Dockerfile                      <- Docker configuration to create containers

requirements.txt                <- List of all required packages
lib                             <- library routines to read configuration details

.gitignore                      <- standard python gitignore
.s2i                            <- hidden folder for advanced s2i configuration
   └── environment              <- s2i environment settings
gunicorn_config.py              <- configuration for gunicorn when run in OpenShift
```
--------

## Steps
1. Log into OpenShift Cluster and click on the Red Hat Applications (Rubik cube like icon). Under OpenShift Managed Services, click Red Hat OpenShift Data Science. If you are trying out OpenShift Data Science in the sandbox from https://developers.redhat.com/products/red-hat-openshift-data-science/overview, please skip to Step 2

![image](https://user-images.githubusercontent.com/16919509/160602298-da6f09ce-2401-4b47-a38e-52c31a286d97.png | width=100)

2. You will see the following screen open in a separate tab.

![image](https://user-images.githubusercontent.com/16919509/160602646-c92bdb4b-26ef-4053-993d-24ce7503015d.png)

If it is the sandbox, you will see the following 

![image](https://user-images.githubusercontent.com/16919509/160619005-be7eb4e9-bc76-4941-81cd-d2d9950a0c4b.png)


3. Click on 'Launch Application' in the Jupyterhub tile. In the following page, select 'TensoFlow' as Notebook Image and 'Small' as Container Size. Click on 'Start Server' as shown below. 

![image](https://user-images.githubusercontent.com/16919509/160617548-6a9e802b-7abe-4183-a1e3-3c37e251af16.png)

For Sandbox, you will see

![image](https://user-images.githubusercontent.com/16919509/160619376-bb582beb-f1b2-4d79-8324-fe048ba925a3.png)

The rest of the screenshots will the same across a full deployment or the sandbox. Once you click on 'Start Server', you should see the following screens. If any error in starting the server, please click on 'Expand Event log' and refer to the log messages. Now we are ready to move on to setup.

![image](https://user-images.githubusercontent.com/16919509/160619478-3ca13298-01f5-410b-a79a-8750d583ff52.png)

![image](https://user-images.githubusercontent.com/16919509/160619537-4e611b30-7d2c-4229-aa82-a32ac5d5fa8a.png)

![image](https://user-images.githubusercontent.com/16919509/160619895-78c972e0-68ce-40da-ba4f-f33a2f3008a2.png)

## Set up

1. First step in set up is to clone the repo into the JupyterLab. There are multiple ways to do this: From the drop down menu 'Git', select 'Clone a Repository' (or) use 'Git' on the left panel and click on 'Clone a Repository' button (screenshot shown below) or use the terminal and clone repository using cli 'git clone https://github.com/rh-aiservices-bu/peer-review.git'


![image](https://user-images.githubusercontent.com/16919509/160640616-35ad4b15-b00d-4da0-a63d-cf2e207746c9.png)

Once cloned, you should be able to see the contents of the peer-review repo as below. 
![image](https://user-images.githubusercontent.com/16919509/160641453-9078e88b-2504-49c7-9456-37cf8ce95580.png)

2. Scroll down the 'Launcher' panel on the right to view the 'Terminal under 'Other'. Click on the Terminal and type the following commands 'cd peer-review' and 'pip install -r requirements.txt'

![image](https://user-images.githubusercontent.com/16919509/160644089-c2362062-1451-4ec8-98be-be2b85ee108a.png)

## Experiment replication using RedHat OpenShift Data Science

This repository is structured in a way to serve as guidance in packaging data, notebooks, models, etc., such that it is easier to replicate the experiments or workflow (combination of notebook, models and results) once published.

### Review/Rerun published notebooks

1. First step in the workflow is to configure the path, model, data, and run information in config file. Prior to the each replication or run, users need to update the version number under [Run] section in Config. This allows results from the following run to be recorded under experiments folder in their respective versioned folder. For example, version 1 of the run would be recorded under experiments/experiment_1.

![image](https://user-images.githubusercontent.com/16919509/160679472-3e6a866c-ddfd-44d3-a97f-e5b811e0930c.png)

Note that the other parameters in Config file can be left as is for now. To start with, we are attempting to rerun the notebooks with the default data, i.e., data used by the author while publishing the experiment. In the later steps, we will show how users can point a run to custom data.

2. Users can review as well as rerun the notebooks in the typical order of the data science workflow. Users can either execute all the cells in a notebook (using the option 'Run all cells' from the drop down menu 'Run') or walk through and execute each cell using the play button ('Run the selected cells and advance')

![image](https://user-images.githubusercontent.com/16919509/160708585-4e107aa4-4ffc-424e-8b57-ff23d1fd9394.png)

![image](https://user-images.githubusercontent.com/16919509/160709579-73f68a55-f31b-4bde-a06c-0398fdeba361.png)

3. Repeat Step 2 for all the 5 notebooks. The following artifacts are stored at the end of each notebook,
4. ```
      experiments                   
       └── experiment_1             <- assuming user sets version in config to 1 
           └── data                    
               └── plots            <- 01-explore-data.ipynb
               └── train-test       <- 02-build-features.ipynb
           └── models
               └── trained          <- 03-train-model.ipynb
               └── tuned            <- 04-tune-model.ipynb
           └── prediction results   <- 05-model-inference.ipynb

--------

For example, after executing all the notebooks, you will see the following files populated under experiments/experiments_1. This is helpful when performing multiple runs of the experiments and comparing results with published version. 

![image](https://user-images.githubusercontent.com/16919509/160889308-3361d9ed-a445-4222-b0f2-5b5e97b9efed.png)


### Rerun published notebooks with custom data

Replicating the experiments with custom data is super easy. Upload your new data and update the config to point to your data. For example, assume user uploads my_input.csv to data/input folder. Update the config file (value for 'input' in Section [Data] and the version for the current run) as shown below. 

![image](https://user-images.githubusercontent.com/16919509/160914615-101d04df-c494-449c-a760-6064099e103a.png)

Then rerun all the notebooks. You should observe that the results are stored in experiments/experiment_2 folder.

![image](https://user-images.githubusercontent.com/16919509/160915210-23fd0461-6116-4b10-a6f2-e7750095386c.png)

Now you can compare your results against the published version/your rerun of the published version. For example, the screenshot below shows comparison of the trained models from both runs

![image](https://user-images.githubusercontent.com/16919509/160915944-31e90145-237b-4123-850f-412946937209.png)

## Serving the model in OpenShift

To serve the model in OpenShift, you need to
```
 1. Wrap the model inference code in to prediction function            <- prediction.py
 2. Build a Flask application to serve the prediction function         <- wsgi.py
     └── Run and test the Flask application locally before deploying   <- flask_run.ipynb and flask_test.ipynb
         it to OpenShift
 3. Create Dockerfile to containerize everything - Flask application,  <- Dockerfile
    prediction code, model and dependencies.
 4. Deploy container to OpenShift and run prediction via REST API
```

All the above are provided with the repository. Some things to note,
- the prediction function is simply the 05-model-inference.ipynb notebook in the form of a function.
- Flask application allows you to create a web application that serves the user input into the prediction function and return back the result.
- Dockerfile copies all the necessary files including the saved model, as well as includes commands to install all necessary packages

## Deploying container in OpenShift

1. On the Red Hat OpenShift Data Science page, click on the Rubik cube icon to list the Red Hat Applications and click on OpenShift console

![image](https://user-images.githubusercontent.com/16919509/160920544-8d022fc7-32fc-469b-a88f-44e7d931c802.png)

2. Once you are inside the OpenShift console, Click on 'Topology '. Right click on the right panel to bring up 'Add to Project'. Then select 'Import from Git'

![image](https://user-images.githubusercontent.com/16919509/160922150-88cfed00-e2ba-48a2-9f50-982c447f75b1.png)

3. Enter the Git repo URL https://github.com/rh-aiservices-bu/peer-review.git and click 'Create'

![image](https://user-images.githubusercontent.com/16919509/160927026-8e53b9cc-035e-43d5-b691-a30d0df485be.png)

![image](https://user-images.githubusercontent.com/16919509/160927164-e5602481-d065-49e1-a733-73f257e2f6e3.png)

4. Wait for the Build to complete and Pod ready. Once the pod is ready, you can see a route available to access this application

![image](https://user-images.githubusercontent.com/16919509/160929226-d9953395-977e-4867-9e5e-6eba53ca2064.png)


5. Test the application using the curl command from flask_test.ipynb but use the route copied from above

![image](https://user-images.githubusercontent.com/16919509/160929503-99d85b5c-efec-4701-8f1a-21fcd6e01294.png)

![image](https://user-images.githubusercontent.com/16919509/160931637-3ba763ed-0a1b-4347-a421-db41ee0f2cdb.png)

![image](https://user-images.githubusercontent.com/16919509/160930960-f3e7dcae-4484-48d1-967c-c6b5389cc75e.png)

 or paste the curl command in the terminal to get the prediction for sample data,
```
[1002700000@jupyterhub-nb-panbalag experiments]$ curl -X POST -H "Content-Type: application/json" --data '{"HR": 103, "O2Sat": 90, "Temp": null, "SBP": null, "MAP": null, "DBP": null, "Resp": 30, "EtCO2": null, "BaseExcess": 21, "HCO3": 45, "FiO2": null, "pH": 7.37, "PaCO2": 90, "SaO2": 91, "AST": 16, "BUN": 14, "Alkalinephos": 98, "Calcium": 9.3, "Chloride": 85, "Creatinine": 0.7, "Glucose": 193, "Lactate": null, "Magnesium": 2, "Phosphate": 3.3, "Potassium": 3.8, "Bilirubin_total": 0.3, "Hct": 37.2, "Hgb": 12.5, "PTT": null, "WBC": 5.7, "Fibrinogen": null, "Platelets": 317}' http://peer-review-panbalag-dev.apps.rhods-sb-prod.3sox.p1.openshiftapps.com/predictions
{
  "prediction": "No Sepsis"
} 
