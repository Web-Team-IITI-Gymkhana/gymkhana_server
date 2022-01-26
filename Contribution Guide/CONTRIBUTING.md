# Note to the Contributors

### Change in Environment Variables
Change in environment variables must be accompanied with the changes in setup.sh files and config.py in the Server directory.

### Newly Installed Packages
Newly installed packages must be written into the requirements.txt file.
Using the command `pip freeze > requirements.txt` in the parent directory.

### To Create New Apps
To create new apps, (eg. "Hostel"), write the following in the parent directory.  
`python createapp.py <app_name>`

### New Models
While creating new models, or updating the existing ones, schemas must be created or updated. The Base needs to be added to the `migrations/env.py` file if not present. To reflect those changes in the database, the following commands need to be run.  
`alembic revision --autogenerate -m "Comment about the changes"`  
`alembic upgrade heads`

### To Reset Database
To reset the database, run the following commands.  
`alembic downgrade base`  
`alembic upgrade heads`

### To update the database
In order to update the database after each pull, run the following command.  
`alembic upgrade heads`
