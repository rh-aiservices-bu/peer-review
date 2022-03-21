Peer-review
==============================

A structured project with data, notebook, models and workflow to allow scientists to consistently replicate experiments.

## Project Organization
```
README.md
LICENSE
requirements.txt        <- Used to install packages for s2i application
data                    <- folder for training and test dataset
models                  <- folder for trained ml models
notebooks               <- folder for various notebooks
images                  <- folder for saved images
reports/figures         <- folder to save results from various runs.
.gitignore              <- standard python gitignore
.s2i                    <- hidden folder for advanced s2i configuration
   └── environment         <- s2i environment settings
gunicorn_config.py      <- configuration for gunicorn when run in OpenShift
prediction.py           <- the predict function called from Flask
wsgi.py                 <- basic Flask application
```
--------

## Using this template


## Set Up

## Steps


## Data Science Workflow

