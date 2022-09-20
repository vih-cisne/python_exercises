def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):

    if ticket_type == 1:
        #make a copy of the list or update this list?
        express_queue.append(person_name)

        return express_queue
    
    elif ticket_type == 0:
        normal_queue.append(person_name)

        return normal_queue
    """
    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """


def find_my_friend(queue, friend_name):
    
    return queue.index(friend_name)
    """
    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """


def add_me_with_my_friends(queue, index, person_name):

    queue.insert(index, person_name)

    return queue
    """
    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """


def remove_the_mean_person(queue, person_name):

    queue.remove(person_name)

    return queue
    """
    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """
    


def how_many_namefellows(queue, person_name):
    count = 0

    for person in queue:
        if person == person_name:
            count += 1
    
    return count
    """
    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """


def remove_the_last_person(queue):
    last_person = queue.pop()

    return last_person
    """
    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    


def sorted_names(queue):
    sorted_list = sorted(queue)
    
    return sorted_list
    """
    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
