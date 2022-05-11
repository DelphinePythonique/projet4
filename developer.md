## Framework

This application follow the MVC ( model, view, controller ) framework.
Among models, we have player, tournament, round, match.

Among object used, we have App -> Router -> Controller -> View -> Specific view. 

These last objects share:
- a context dictionary containing for exemple the route
to follow. 
- the router which contains all the routes, is accessible in each of the objects thanks to a property linked 
at the time of the construction of the object

## Scenario
1) When the application begin, the homepage is requested.
2) the request is forwarded to the router object
3) the router object thanks to  a dictionary *mapping* of correspondence between 
the route and the method of the controller to call, call controller's method.
4) the controller passes, via context, all useful objects to a view dispatcher, which calls the view bound to the route
5) the specific view is displayed, which return user response, like the next route, thank the context 

## HOW TO

## How to add entry menu
1) in router.py add constant into router class which represents route and the number into menu. 
Name's format of these constants is: ACTION_ID
2) in router__init__ method, into *mapping_route_to_controller* add entry for new menu (route), 
the value of entry correspond to controller's method to call
3) add method into controller
4) into view.py, add view method to call function route in mapping_route_to_method dictionary
5) create new specific view with method to call: class MySpecificView

## How to display entry menu, and manage input
in specific view, method display, add these blocks:
in class MySpecificView
``` python
    @property
    def router(self):
        return self._view.router
```
in display method, 
for list items menu available in this view
``` python
        items_menu = {
            self.router.REPORT_PLAYER_ID: "Report players",
            self.router.REPORT_TOURNAMENT_ID: "Report tournaments",
            self.router.HOMEPAGE_ID: "Homepage",
        }
```
create block below to manage input

*exemple input menu*
``` python
  inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": items_menu.keys()},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
```
- lines: list of sentences to display, like a question
- inputs_request: populate context with new keys composed at level 1 
context_key value and level 2 keys into input_required; for exemple context["choice"]["menu"]

*exemple input for populate object's fields*
``` python
inputs_required = {
            "surname": {
                "question": ["Enter surname"],
                "type": str,
                "not_null": True,
                "constraints": {"max_nb_car": 50},
            },
            "first_name": {
                "question": ["Enter first_name"],
                "type": str,
                "not_null": True,
                "constraints": {"max_nb_car": 50},
            },
            "date_of_birth": {"question": ["Enter date_of_birth as DD/MM/YYYY"], "type": datetime},
            "gender": {
                "question": ["Enter gender (m for masculine, f for feminine, o for other)"],
                "type": str,
                "constraints": {"max_nb_car": 1, "format": "^[f|m|o]$"},
            },
            "ranking": {"question": ["Enter ranking"], "type": int, "not_null": True, "constraints": {">=": 0}},
        }

        print("Enter player informations")
        context = inputs_request(inputs_required, context_key="player", context=context)
```



