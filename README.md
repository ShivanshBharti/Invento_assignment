# Assignment for Invento

## Getting Started
 - Make virtual environment in python
 - Install requirements.txt
    `pip install -r requirements.txt`


## Starting Django Project

This project has 2 settings files for production and development


### Models
There are 3 models:
    -Category
    -Language
    -Coder

    - Language and Category models ManyToOne relationship using Foreign Key .
    -The Coder model and Language model connected with ManyToMany relationship.

### Running in Development
Using the settings/development.py file
    `python manage.py runserver --settings=api.settings.development`

    - Head over to http://127.0.0.1:8000



### Running in Production
Using the settings/production.py file
    `python manage.py runserver --settings=api.settings.production`

    - Head over to http://127.0.0.1:8000

### Outputs
    -Main Page 
        ![Main Page](https://github.com/ShivanshBharti/Invento_assignment.git/blob/master/images/Base.png?raw=true)
    
    -Category Page
       ![Category Page](https://github.com/ShivanshBharti/Invento_assignment.git/blob/master/images/Category.png?raw=true)
    
    -Language Page
        ![Language Page](https://github.com/ShivanshBharti/Invento_assignment.git/blob/master/images/Language.png?raw=true)

    -Coder Page
        ![Coder Page](https://github.com/ShivanshBharti/Invento_assignment.git/blob/master/images/Coder.png?raw=true)

