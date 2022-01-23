# Note to the Contributors

### Change in Environment Variables
Change in environment variables must be accompanied with the changes in setup.sh files and config.py in the Server directory.

### Newly Installed Packages
Newly installed packages must be written into the requirements.txt file.
Using the command `pip freeze > requirements.txt` in the parent directory.

### Create New Apps
To create new apps, (eg. "Hostel"), write the following in the parent directory.  
`python createapp.py <app_name>`