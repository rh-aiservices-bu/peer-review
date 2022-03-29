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
.gitignore                      <- standard python gitignore
.s2i                            <- hidden folder for advanced s2i configuration
   └── environment              <- s2i environment settings
gunicorn_config.py              <- configuration for gunicorn when run in OpenShift
```
--------

## Steps

## Experiment replication using RedHat OpenShift Data Science

## Data Science Workflow

