"""Functions which helps the locomotive engineer to keep track of the train."""
from itertools import chain

def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """ 
    a,b,c,*rest = each_wagons_id
    updated_wagon_list = [c]+ missing_wagons + rest + [a,b]
    return updated_wagon_list


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
   
    stops = []
    for item in kwargs.values():
        stops.append(item)
    route["stops"] = stops

    return route



def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extended_route = {**route, **more_route_information}
    return extended_route

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [first,second,third] = wagons_rows

    for index in range(len(wagons_rows[0])):
        wagons_rows[index] = [first[index],second[index],third[index]]
    
    return wagons_rows
            

