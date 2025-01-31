# Projet Site
Project Site is a simple Python project to demostrate the CI/CD workflow from Github Actions through to AWS CodePipeline and Elastic Beanstalk, as well as provide a basic website to highlight AWS projects I've worked on.

## Github Actions
As this project is a simple Flask application the default "Python Applicaton" Actions workflow is sufficient to run pytest and flake8 for verification and validation of the project before PR are allowed into main.

## AWS
### CodePipeline
CodePipeline is configured in the following manner:
* Github webhook used to notify when commits to main occur
* A simple zip command is used to build the package required for Beanstalk, this zips the app.py file, as well as others required.
* The artifact created by the build command is passed to AWS Elastic Beanstalk

Full details under [AWS_Projects/CodePipeline](https://github.com/Deepthisasi89/AWS_Projects/blob/main/CodePipeline/)
### Elastic Beanstalk
Full details under [AWS_Projects/ElasticBeanstalk](https://github.com/Deepthisasi89/AWS_Projects/tree/main/ElasticBeanstalk)
