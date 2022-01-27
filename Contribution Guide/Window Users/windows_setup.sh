cd ../..
pip install virtualenv
virtualenv venv
echo "Virtual Environment Created"
venv\Scripts\activate
pip install -r windows_requirements.txt
echo "Installed Required Packages"  