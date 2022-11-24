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
        [Imgur](https://i.imgur.com/sSFMlEp.png)
    
    -Category Page
        [Imgur](https://i.imgur.com/113PF6Y.png)
    
    -Language Page
        [Imgur](https://i.imgur.com/jNRUraV.png)

    -Coder Page
        [Imgur](https://i.imgur.com/eaX9YDk.png)

