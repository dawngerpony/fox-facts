# fox-facts

Facts about foxes in Python. Work in progress.

## How to run locally

    pip install -r requirements.txt
    python fox_facts/api.py
    curl http://locahost:5000/api.py

### Running via Docker

Prerequisites: Docker

    docker-compose run lint
    docker-compose up api

## Deploying to Google App Engine

Prerequisites: Google Cloud SDK, a GCP account with an active project

    cd fox_facts
    gcloud app create --project=[YOUR_PROJECT_ID]
    gcloud app deploy
    gcloud app browse

For more information, visit [Quickstart for Python 3 in the App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/python3/quickstart)

## Technologies

Uses:

- Python 3.8
- Flask
- Flask-RESTX
- CircleCI
- Terraform
- Google Cloud Platform (specifically Google App Engine)

## Thanks to

- [15 Fascinating Facts About Foxes](https://www.thefactsite.com/fascinating-fox-facts/)
- [Foxy facts for children](http://foxproject.org.uk/foxy-facts-for-children/)
- [Building a Microservice in Python](https://medium.com/@sonusharma.mnnit/building-a-microservice-in-python-ff009da83dac)
