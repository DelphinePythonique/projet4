import re
from datetime import datetime


def inputs_request(inputs_required, context_key, context):
    for field, question_field in inputs_required.items():
        print("\n".join(question_field["question"]))
        if context_key not in context:
            context[context_key] = {}
        if "constraints" in question_field:
            if ">=" in question_field["constraints"]:
                if question_field["constraints"][">="] in context[context_key]:
                    question_field["constraints"][">="] = context[context_key][question_field["constraints"][">="]]
        check_input_is_ok = False
        while not check_input_is_ok:
            check_input_is_ok, value = check_input(question_field, input())
            if not check_input_is_ok:
                print(f"{value}, try again")
            else:
                context[context_key][field] = value
    return context


def check_constraints(constraints_dict, input_value):
    for constraint, value_constraint in constraints_dict.items():
        if "max_nb_car" == constraint:
            if not check_max_nb_car(input_value, value_constraint):
                return False, f"This value must contain {value_constraint} maximum"
        if ">=" == constraint:
            if not check_sup_or_equal(input_value, value_constraint):
                return False, f"This value must be {constraint} {value_constraint}"
        if "format" == constraint:
            if not check_regex(input_value, value_constraint):
                return False, f"This value must respect format {value_constraint}"
        if "choice_ids" == constraint:
            if not check_in(input_value, value_constraint):
                return False, f"This value is not in the list"

    return True, input_value


def check_input(description_dict, input_value):
    status, input_value = check_type(input_value, description_dict["type"])
    if not status:
        return False, f"This value must be {description_dict['type'].__name__} "
    if "not_null" in description_dict:
        if description_dict["not_null"]:
            if check_not_null(input_value):
                return False, "This value must not be null"
    if "constraints" in description_dict:
        resultok, input_value = check_constraints(description_dict["constraints"], input_value)
        if not resultok:
            return False, input_value
    return True, input_value


def check_type(value, type_):
    try:
        typed_value = value
        if type_ == datetime:
            if value.strip() != "":
                datetime.strptime(value, "%d/%m/%Y")
        if type_ == int:
            typed_value = int(value)

    except ValueError:
        return False, typed_value

    return True, typed_value

def check_max_nb_car(value, max_):
    try:
        if isinstance(value, str):
            if len(value) > int(max_):
                return False
    except ValueError:
        return True

    return True


def check_sup_or_equal(value, value_constraint):
    try:
        if isinstance(value, int):
            if int(value) < int(value_constraint):
                return False
        elif isinstance(value, str):
            if value.strip() != "" and value_constraint.strip() != "":
                if datetime.strptime(value, "%d/%m/%Y") < datetime.strptime(value_constraint, "%d/%m/%Y"):
                    return False
    except ValueError:
        return True
    return True


def check_regex(input_value, format):
    return re.search(format, input_value)


def check_in(input_value, choice_list):
    return input_value in choice_list


def check_not_null(value):
    return value == ""
