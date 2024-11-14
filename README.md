# shareit

An application that enables seamless file sharing without barriers.


### Setting up project 

git clone https://github.com/krishna-kumark/shareit.git \
cd shareit \
python manage.py makemigrations \
python manage.py migrate \
python manage.py run_shareit  --port 8080 --deploy local/server



### To Run the project
$env:DJANGO_SETTINGS_MODULE="shareit.settings"
daphne -p 8000 shareit.asgi:application
