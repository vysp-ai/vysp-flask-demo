# ChatGPT, Protected by VYSP.AI

ChatGPT Demo Application with VYSP.AI Security

Credit to @RamSailopal for the base project to run this demo!

 ![Alt text](ChatGPT.JPG?raw=true?raw=true "ChatGPT")
 
# Getting Started
Run:
     git clone https://github.com/vysp-ai/vysp-flask-demo.git

Skip to "Back to your IDE" if you already have your account set up in the VYSP.AI Platform

## Get started on the VYSP.AI Platform
     Navigate to https://dashboard.vysp.ai/signup
     Sign up for an account, and move on to the next step.

## Create a Gate
     Once you're logged in, go to "Gates" in the sidebar or navigate to https://dashboard.vysp.ai/gates
     
     Click "Add Gate" in the top right, and enter a name for your application, like "Chat Application"

## Add Rule
     Go to the Flows page in the sidebar, and you'll see that two flows were created, one input flow and one output flow.
     
     Go to the Input Flow and click "Add Rule". Enter a name, and select "Prompt Injection Detection". Click "Submit" and you'll see that the rule was created.

## Back to your IDE
     Go back to your IDE, and create a ".env" file using the ".env.example" file in the /app directory.

     cd vysp-flask-demo
     cd app

## Grab your credentials
     The dropdown menu that has your username in it contains your Tenant API key, copy and add to your .env, assigned to the variable "VYSP_TENANT_API_KEY". Then, go to the gate you just created, and copy the gate's API key. Copy and assign the env variable "VYSP_GATE_API_KEY".

     Add your own openai API token (attained from https://openai.com/api/)

## Running the application
     
### Create a virtualenv environment to run the application
     python3 -m virtualenv .venv
     source .venv/bin/activate
### Install libraries and dependencies
     pip install -r requirements.txt

### Run the application!
     flask run --host=0.0.0.0 --port=5001
     Navigate to http://localhost:5001
 
     Ask a question
     
     Get the answer

     
