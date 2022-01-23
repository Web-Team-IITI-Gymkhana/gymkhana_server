#!/bin/bash

cd ../..
pip install virtualenv
virtualenv venv
echo "Virtual Environment Created"

source venv/bin/activate
pip install -r requirements.txt
echo "Install Required Packages"

touch .env
printf "DATABASE_USERNAME=\nDATABASE_PASSWORD=\nDATABASE=\nIN=DEVELOPMENT\nGOOGLE_CLIENT_ID=\nGOOGLE_CLIENT_SECRET=\nSECRET_KEY=" >> .env
echo "Fill the credentials in .env file"
echo "You are now in the parent directory"