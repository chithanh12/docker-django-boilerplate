#Setup and installation
1. Install docker
2. For window please clone project uner C:/User to utilize share folder feature
3. For convenience, `cmd_*.sh` script is prepared to use
- `cmd_refresh_lib.sh` reload lib (should run it before run start server script)
- `cmd_start_server.sh` start django server and postgres db
- `cmd_fix_owner.sh` fix permission deined issuse    
4. IDE setup
- `VSCode`: already config for autocomplete feature (.vscode/settings.json)

#Docker in advance
1. Start up db docker
- Move into the db folder
```docker-compose up```
2. Start up docker server
- Move into the server folder
```docker-compose up```

3. Other django commands, ppend command with `docker-compose run web
- Create admin user for firsttime use
```docker-compose run web  /bin/bash ./cmd_init_sample_data.sh```
- Get django version
```docker-compose run web python -c "import django;
print(django.get_version())```
- Create Posts app
```docker-compose run web python manage.py startapp posts```
- Make migration code
```docker-compose run web python manage.py makemigrations posts```
- Check sql migration code
```docker-compose run web python manage.py sqlmigrate posts 0001```

- Update data from migration
```docker-compose run web python manage.py migrate```

- Locate django commands
```docker-compose run web python -c "import django;
print(django.__path__)"```

# Doing translation https://dethoima.info/da-ngu-trong-django/
- Ask django to create VN translation files 
```docker-compose run web python manage.py makemessages -l vi```
- Compile translation file 
```docker-compose run web python manage.py compilemessages```


#Trouble shooting
1. Error when run docker run web xyz
```ERROR: Conflicting options: host type networking can't be used with links. This would result in undefined behavior```
- Solutions:
  a. List all docker container in your host
 ```docker ps```
  b. Kill the running web container
```docker kill [replace_your_running_web_container]```  