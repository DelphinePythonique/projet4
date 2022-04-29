from controller import Controller


class Router:
    def __init__(self):
        self.controller = Controller()

    def call_controller_method(self, context):

        if "route" not in context:
            return {}

        if context['route'] == 'homepage':
            context = self.controller.index(context)
        elif context['route'] == 'index_players':
            context = self.controller.index_player(context)
        elif context['route'] == 'index_tournaments':
            context = self.controller.index_tournament(context)
        elif context['route'] == 'add_player':
            context = self.controller.add_player(context)
        elif context['route'] == 'update_ranking_player':
            context = self.controller.update_ranking_player(context)
        elif context['route'] == 'add_tournament':
            context = self.controller.add_tournament(context)
        elif context['route'] == 'display_tournament':
            context = self.controller.display_tournament(context)
        elif context['route'] == 'add_player_into_tournament':
            context = self.controller.add_player_into_tournament(context)
        elif context['route'] == 'start_round':
            context = self.controller.start_round(context)
        elif context['route'] == 'save_round':
            context = self.controller.save_round(context)
        else:
            context = {}

        return context
