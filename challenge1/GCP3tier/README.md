# tech_challenge
Challenge1:

The three tier web application we will be deploying to Kubernetes is SnapPass. It is a Python Flask application that uses redis as the storage backend to provide a simple way to share passwords.

Prerequisites: Login to a GCP console and create a Project. Open CloudShell and set the Project created as default project.
   gcloud config set project $GCP_PROJECT_ID

The Web application has 3 tiers: nginx, Python and redis. The docker images of nginx and SnapPass are built and stored in the google container registry with following commands from respective source code. 

         gcloud builds submit --tag us.gcr.io/$GCP_PROJECT_ID/snappass-nginx:$SNAPPASS_NGINX_VERSION .
         gcloud builds submit --tag us.gcr.io/$GCP_PROJECT_ID/snappass:$SNAPPASS_VERSION .

Redis Docker image is taken from redis official Docker Hub Repository.


We create Kubernetes Cluster named "gke-terraform-learn"and deploy the application to it. 


            cd challenge1/GCP3tier/terraform 
            terraform apply 
Now navigate to challenge1 and run the command 

      
            gcloud builds submit 
The deployment files reside in deploy-gke directory and the default cloudbuild.yaml has the information to connect to the cluster and deploy the applications.

