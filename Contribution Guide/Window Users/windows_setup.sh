cd../..
pip install virtualenv
virtualenv venv
# echo "Virtual Environment Created"
source venv/Scripts/activate.bat
pip install -r windows_requirements.txt
# echo "Installed Required Packages"  