# Projet4: Tool to manage chess tournaments

## Goals: 
Ultimately, our goal will be to manage chess tournament

version: 0.0.9

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
- Install dependencies
``` bash
 python install -r requirements.txt
```
- Install dev dependencies
``` bash
 python install -r requirements_dev.txt
```

- generate the flake8-html report
``` bash
  flake8 --format=html --htmldir=flake-report --exclude=env
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
3 - Homepage
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
3 - Homepage
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
``` bash
Enter player identifier
1
Player:
Identifier:1
surname:joueurA-100
first_name:Delphine
date_of_birth:01/01/1970
gender:feminine
ranking:100
Enter new_ranking
```
Then enter the new ranking

#### Manage Tournament
From *Home screen*, enter 2
``` bash
Enter the number of the action to be perform and press enter
2
Chess tournaments managment - Tournament
1 - Add tournament
2 - Display tournament
3 - Homepage
```
##### Add Tournament
From *Tournament screen*, enter 1 to add tournament, and answer questions
after that, the *Tournament screen is updated with new tournament

##### Display Tournament
From *Tournament screen*, enter 2 to display tournament.

Depends on the state of the tournament, menu items are displayed: 
Add player, start round, save result.

Read the prompt to know what you can do

The flow is: 
- After create tournament, state is *draft*. 
- After add the maximum number of players, state is *ready*.
- When state is ready, you can start round, state become *in progress*.
- when state is *in progress*, if a round is started, save result can be processed, 
else, an other round can be started 

######  
