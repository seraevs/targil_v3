# DevOps Continuous Delivery Pipeline Exercise

# targil_v3

## Getting started
## To begin working, install virtual machines on VMWare.

1) GitLab server: Ubuntu 22.04

2) Jenkins with Docker server: Ubuntu 22.04

3) JFrog server: Ubuntu 20.04

    a) Jenkins server for creating CI/CD processes
    b) GitLab for creating and saving my repository and using it as a build machine
    c) JFrog Artifactory server for saving created Docker images

You can find my work at the following link: https://github.com/seraevs/targil_v3

Please note that the corrected version assumes the intended operating systems are Ubuntu versions 22.04 and 20.04 for GitLab, 
Jenkins with Docker, and JFrog server, respectively.

## Create Dockerfile for Docker image build as follows:

The path to Dockerfile: https://github.com/seraevs/targil_v3/tree/main/Dockerfile

    a. Based on python:3.9 image
    b. Define environment variable VERSION=1.2.0
    c. Install Python
    d. Install Vim
    e. Install Zip
    f. Install Unzip
    g. Copy zip_job.py into the image's /tmp folder
    h. Once the Docker container is up, run a command to print the OS type and architecture and verify that /tmp/zip_job.py exists

## Create zip_job.py python script as follows:
    a. Create an array of a, b, c, d
    b. Based on this array, create text files (a.txt, b.txt, etc.)
    c. Make sure all text files are created, and if not, fail the script
    d. Create zip files with names based on the array + VERSION environment variable, where each zip file contains one corresponding text file (e.g., a_1.2.0.zip should include a.txt, b_1.2.0.zip should include b.txt, and so on)
    e. Make sure all zip files are created, and if not, fail the script

Please note that the corrected version assumes that you have created the Dockerfile and zip_job.py script at the specified locations.


## Created 2 Jenkinsfile pipeline jobs with the same logic, one Declarative and one Scripted:
    a. The agent should be based on the Dockerfile you created in step 1.
    i. It should run in privileged mode with the label "zip-job-docker".
    b. The build stage should execute the zip_job.py you created in step 2.
    c. The publishing stage should upload all the zip files created (only if the build stage succeeded) to the Artifactory you installed using the following properties:
    i. Artifactory server: "http://192.168.44.133:8082/ui/native/jfrog-support-bundle/"
    ii. Artifactory user: "admin"
    iii. Artifactory password: "S#ystem1!"
    iv. Artifactory repository to upload to: "binary-storage/{VERSION env variable}"
    d. Created a Python script for the send Report stage - send an email with the job status in the subject to a specific email address.
    e. Cleanup stage - delete the workspace.

Please note that the corrected version assumes you have configured the Jenkins files and the necessary email-sending functionality in the Python script.


## Links to pictures: 
https://github.com/seraevs/targil_v3/tree/main/Pictures

## Links to JenkinsFoles: 
https://github.com/seraevs/targil_v3/tree/main/JenkinsFiles

## Links to Logs JenkinsFoles: 
https://github.com/seraevs/targil_v3/tree/main/LogJenkinsFiles


