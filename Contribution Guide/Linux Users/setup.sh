#!/bin/bash

cd ../..
pip install virtualenv
virtualenv venv
echo "Virtual Environment Created"

source venv/bin/activate
pip install -r requirements.txt
echo "Installed Required Packages"

touch .env
printf "ENVIRONMENT=DEVELOPMENT\nDATABASE_USERNAME=\nDATABASE_PASSWORD=\nDATABASE=\nSECRET_KEY=\nGOOGLE_CLIENT_ID=\nGOOGLE_CLIENT_SECRET=\nFRONTEND_URL=" >> .env
echo "Fill the credentials in .env file"
echo "You are now in the parent directory"