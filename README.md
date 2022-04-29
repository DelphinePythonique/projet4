# Projet4: Tool to manage chess tournaments

## Goals: 
Ultimately, our goal will be to manage chess tournament

version: 0.0.1

## Summary

[Install](#install)

[Use](#use)

[Todo](TODO.md)

[Changelog](CHANGELOG.md)

------------
### <a name="install"></a>Install

This setup is for a development environment.

Prerequisite:

- \>= python3,9

Through a terminal(Debian linux) or Powershell(Windows) : 

Position yourself in the local directory in which you want to position the sources of the application
``` bash
 cd [path_to_source_directory]
```
-  Clone the repository via the clone command in ssh mode
[ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh), via la commande suivante

``` bash
 git clone git@github.com:DelphinePythonique/projet4.git
```

- Position yourself in the project directory, create a virtual environment

``` bash
 cd projet4
 python -m venv env
```
- Activate virtual environment

   If OS is Debian Linux: 
``` bash
 source env/bin/activate
```
   If OS is Windows:
``` bash
 .\env\Scripts\activate
```

### <a name="use"></a>Uses

#### Start  
Enter the following command
``` bash
 python app.py 
```
This *home screen* is displayed
``` bash
Chess tournaments managment
1 - Manage players
2 - Manage tournaments
Enter the number of the action to be perform and press enter
```

#### Manage Players  
From *home screen* Enter 1; *Players screen* is displayed; 
on top, there is menu, and below players list
``` bash
Chess tournaments managment - Players
1 - Add player
2 - Update Ranking
========================================
PLAYERS
========================================
#1:Delphine joueurA-100(100)
#4:Delphine joueurA-20(20)
#3:Remi joueurA-30(30)
#5:Jean joueurA-50(50)
.
.
.
Enter the number of the action to be perform and press enter
```

##### Add player
From *Players screen*, enter 1 to add player, and answer questions
after that, the *Players screen is updated with new player
``` bash
Chess tournaments managment - Players
1 - Add player
2 - Update Ranking
========================================
PLAYERS
========================================
#13:Jim Mentor(100)
#1:Delphine joueurA-100(100)
#4:Delphine joueurA-20(20)
```
##### Add update ranking
From *Players screen*, enter 2 to update ranking 
After that the prompt asks you to enter the player id, (*i.e 13 for Jim*)

see you soon for the next step