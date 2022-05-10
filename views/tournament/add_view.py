from datetime import datetime

import router
from models.tournament import Tournament
from utils.input_utils import inputs_request


class TournamentAddView:
    def display(self, context):
        # with view asks for the entry of the information of the new tournament and return save message with index tournament

        print("Enter tournament informations")
        inputs_required = {
            "name": {
                "question": ["Enter name"],
                "type": str,
                "not_null": True,
                "constraints": {"max_nb_car": 50},
            },
            "place": {
                "question": ["Enter place"],
                "type": str,
                "not_null": True,
                "constraints": {"max_nb_car": 50},
            },
            "description": {
                "question": ["Enter description"],
                "type": str,
                "not_null": False,
                "constraints": {"max_nb_car": 200},
            },
            "begin_date": {"question": ["Enter begin date as DD/MM/YYYY"], "type": datetime},
            "end_date": {
                "question": ["Enter end date as DD/MM/YYYY"],
                "type": datetime,
                "constraints": {">=": "begin_date"},
            },
            "time_control": {
                "question": [f"Enter time control among {Tournament.TYPE_OF_TIME_CONTROL}"],
                "type": str,
                "constraints": {"choice_ids": Tournament.TYPE_OF_TIME_CONTROL},
            },
        }

        context = inputs_request(inputs_required, context_key="tournament", context=context)
        context["route_id"] = router.Router.INDEX_TOURNAMENT_ID
        return context
