# Deploy from this directory when using GCP

Be sure to run the following prior to deploying or the app will fail:


    pip install -r requirements.txt -t lib/

### Google App Engine deployment:

1. Download the `gcloud` SDK:


    https://cloud.google.com/sdk/docs/


2. Authorize the SDK for your Google account:


    $ gcloud init


3. Create a new project on Google Cloud:


    https://console.cloud.google.com/home/dashboard


4. Deploy the application


    $ gcloud app deploy app.yaml --project <YOUR PROJECT NAME>


