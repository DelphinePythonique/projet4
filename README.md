# Projet4: Tool to manage chess tournaments

## Goals: 
Ultimately, our goal will be to manage chess tournament

version: 1.0.2

## Summary

[Install](#install)

[Use](#use)

[Contribute](contribute.md)

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
 pip install -r requirements.txt
```
- Install dev dependencies
``` bash
 pip install -r requirements_dev.txt
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
2  - Manage players
3  - Manage tournaments
11 - Reports
Enter the number of the action to be perform and press enter
```

#### Manage Players  
From *home screen*, enter the number corresponding to *Manage players*, here 2 and press [enter] ; *Players screen* is displayed; 
on top, there is menu, and below players list
``` bash
Chess tournaments managment - Players
PLAYERS
id#  |first name                                        |surname                                           |ranking|
====================================================================================================
1    |Delphine                                          |Lemire                                            |1      
====================================================================================================
4 - Add player
5 - Update Ranking
1 - Homepage
====================================================================================================

```

##### Add player
From *Players screen*, enter the number corresponding to *Add player* and press [enter], and answer questions
after that, the *Players screen is updated with new player

##### Add update ranking
From *Players screen*, enter the number corresponding to *Update ranking* and press [enter]
After that, the prompt asks you to enter the player id, (*i.e 13 for Jim*), do this
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
From *Home screen*, enter the number corresponding to *Manage tournaments* and press [enter].
The screen below is displayed.
``` bash
Chess tournaments managment - Tournament
====================================================================================================
Tournaments
1:Tournoi des 6 nations (draft)
====================================================================================================
6 - Add Tournament
7 - Display tournament
1 - Homepage
====================================================================================================
Enter the number of the action to be perform and press enter

```
##### Add Tournament
From *Tournament screen*, enter 1 to add tournament, press [enter], and answer questions
after that, the *Tournament screen is updated with new tournament

##### Display Tournament
From *Tournament screen*, enter 2 and press [enter] to display tournament.

Depends on the state of the tournament, menu items are displayed: 
Add player, start round, save result.

Read the prompt to know what you can do

The flow is: 
- After create tournament, state is *draft*. 
- After add the maximum number of players, state is *ready*.
- When state is ready, you can start round, state become *in progress*.
- when state is *in progress*, if a round is started, save result can be processed, 
else, an other round can be started 

#### Reports

From *home screen*, enter the number corresponding to *Reports*, here 11 ; *Reports screen* is displayed
``` bash
Chess tournaments managment
12 - Report players
13 - Report tournaments
1 - Homepage
Enter the number of the action to be perform and press enter

```
##### Report players
From *Report screen*, enter the number corresponding to *Report Players*, here 12.
``` bash
Chess tournaments managment
12 - Report players
13 - Report tournaments
1 - Homepage
Enter the number of the action to be perform and press enter
12
What sort order do you want; 1: by alphapetic surname, 2: by ranking?
```
Indicate if you want sorted players by surname (1) or ranking (2), press [enter]
``` bash
hess tournaments managment
id#  |first name                                        |surname                                           |ranking|
====================================================================================================
1    |Delphine                                          |Lemire                                            |1      
2    |Theo                                              |Dupond                                            |5      
====================================================================================================
11 - Report menu
Enter the number of the action to be perform and press enter
```
##### Report tournaments
From *Report screen*, enter the number corresponding to *Report Tournaments*, here 13.
``` bash
Chess tournaments managment 
1:Tournoi des 6 nations (draft)
====================================================================================================
14 - Report rounds of tournament
15 - Report matchs of tournament 
16 - Report players of tournament
11 - Report menu
====================================================================================================
Enter the number of the action to be perform and press enter
```
##### Report tournament's rounds
``` bash
Chess tournaments managment - Rounds of tournament tournament of 20/05/2022
11 - Menu Report
13 - Report Tournament
Enter the number of the action to be perform and press enter
Round Round 1 start
Round Round 2 draft
Round Round 3 draft
Round Round 4 draft

```
##### Report tournament's matchs
``` bash
Chess tournaments managment - Matchs of tournament tournament of 20/05/2022
====================================================================================================
11 - Menu Report
13 - Report Tournament
====================================================================================================
Enter the number of the action to be perform and press enter
#    |Player1                                                                 |Player2                                                               
     |surname                                           |ranking   |result    |surname                                           |ranking   |result    
1    |joueurA-20                                        |20        |0         |joueurA-30                                        |30        |0         
2    |joueurB-30                                        |30        |0         |joueurA-50                                        |50        |0         
3    |joueurA-100                                       |100       |0         |joueurB-100                                       |100       |0         
4    |joueurC-100                                       |100       |0         |joueurD-100                                       |100       |0      
```
##### Report tournament's players
``` bash
Chess tournaments managment 
1:tournament of 20/05/2022 (in_progress)
2:tournament of 20/05/2022 (ready)
3:tournoi 3 round (in_progress)
4:tournoi 0 round (ready)
5:tournament of 20/05/2022 (ready)
6:test 0 round* (closed)
7:tournament of 20/05/2022 (in_progress)
8:tournament of 20/05/2022 (ready)
====================================================================================================
14 - Report rounds of tournament
15 - Report matchs of tournament 
16 - Report players of tournament
11 - Report menu
====================================================================================================
Enter the number of the action to be perform and press enter
16
From which tournaments do you want to display the rounds, enter the tournament ID?
1
What sort order do you want; 1: by alphapetic surname, 2: by ranking?

```
indicate the key to sort the players
``` bash
Chess tournaments managment - Rounds of tournament tournament of 20/05/2022
id#  |first name                                        |surname                                           |ranking|
====================================================================================================
4    |Delphine                                          |joueurA-20                                        |20     
3    |Remi                                              |joueurA-30                                        |30     
6    |Remi                                              |joueurB-30                                        |30     
5    |Jean                                              |joueurA-50                                        |50     
1    |Delphine                                          |joueurA-100                                       |100    
2    |Jean                                              |joueurB-100                                       |100    
7    |Delphine                                          |joueurC-100                                       |100    
8    |Jean                                              |joueurD-100                                       |100    
====================================================================================================
11 - Menu Report
13 - Report Tournament
====================================================================================================
Enter the number of the action to be perform and press enter

```