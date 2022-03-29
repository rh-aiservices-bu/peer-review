Peer-review
==============================

A structured project with data, notebook, models and workflow to allow scientists to consistently replicate experiments.

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
   └── experiment_0             <- replicate experiment and store results in similar 
       └── data                    directory structure for data and models.
           └── trained             (similar structure created for each run)  
           └── tuned  
       └── models
           └── trained
           └── tuned           
       └── prediction results   
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

The rest of the screenshots will the same across a full deployment or the sandbox. Once you click on 'Start Server', you should see the following screens. If any error in starting the server, please click on 'Expand Event log' and refer to the log messages.

![image](https://user-images.githubusercontent.com/16919509/160619478-3ca13298-01f5-410b-a79a-8750d583ff52.png)

![image](https://user-images.githubusercontent.com/16919509/160619537-4e611b30-7d2c-4229-aa82-a32ac5d5fa8a.png)

![image](https://user-images.githubusercontent.com/16919509/160619895-78c972e0-68ce-40da-ba4f-f33a2f3008a2.png)

4. 



## Experiment replication using RedHat OpenShift Data Science

## Data Science Workflow

