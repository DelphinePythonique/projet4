## Framework

This application follow the MVC ( model, view, controller ) framework.
Among models, we have player, tournament, round, match
Among object used, we have App -> Router -> Controller -> View -> Specific view. 

These last objects share a context dictionnary containing for exemple the route
to follow and specific view or objects to display. 

## Scenario
1) When the application begin, the homepage is requested.
2) the request is forwarded to the router object
3) the router object thanks to  a dictionary *mapping* of correspondence between 
the route and the method of the controller to call, call controller method's
4) 

## HOW TO

## How to add entry menu
1) in router.py add 2 constants into router class: one for the route and other for the number into menu. 
Name's format of these constants is: ACTION and ACTION_ID
2) Router__init__ method, into *mapping_route_to_controller* add entry for new menu (route), 
the value of entry correspond to controller's method to call
3) add method into controller
4) into view.py,  
   1) add entry into mapping_route_id_to_route dictionnary 
   2) and view method to call function route in mapping_route_to_method dictionnary
   3) create new specific view with method to call
