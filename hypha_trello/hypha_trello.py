import re
from board_api import Board


def flatten_list(l):
    return [item for sublist in l for item in sublist]


def hypha_boards():
    return Board().boards[1:]


def cards():
    return flatten_list([list.list_cards() for list in lists()])


def lists():
    return flatten_list([board.all_lists() for board in hypha_boards()])


def comments(card): #take match_card()
    return card.fetch_comments(force=True)


def match_card(query):
    lcards = []
    for card in cards():
        match = re.search(query, card.name, flags=re.IGNORECASE)
        if match:
            lcards.append(card)
            return lcards


def match_list(qlist):
    # qlist = raw_input("Enter a list to be searched: ")
    for l in lists():
        match = re.search(qlist, l.name, flags=re.IGNORECASE)
        if match:
            return l


def get_card(l):
    return l.list_cards()


def comments_dict(qlist):
    com_dict = {}
    planned = match_list(qlist).list_cards()
    for card in planned:
        for c in comments(card):
            if card.name not in com_dict:
                com_dict[card.name] = [c["data"]["text"]]
            else:
                com_dict[card.name].append(c["data"]["text"])
    return com_dict

def match_estimate(comm):
    search = "Estimate\s*:\s*(\d?\.?\d?)h"
    est = []
    for i in comm:
        match = re.search(search, i, flags=re.IGNORECASE)
        if match:
            est.append(float(match.group(1)))
    return est


def match_remain(comm):
    search = "Remaining\s*:\s*(\d?\.?\d?)h"
    est = []
    for i in comm:
        match = re.search(search, i, flags=re.IGNORECASE)
        if match:
            est.append(float(match.group(1)))
    return est


def cal_estimates(qlist):
    com_dict = comments_dict(qlist)
    planned_hours = []
    for c in com_dict:
        remain = match_remain(com_dict[c])
        estimate = match_estimate(com_dict[c])

        if remain:
            planned_hours.extend(remain)
        elif estimate:
            planned_hours.extend(estimate)
    return planned_hours


def print_card_info():
    query = raw_input("Enter job number to be searched: ")
    matched_cards = match_card(query)
    if matched_cards:
        for card in matched_cards:
            c = card.fetch_comments(force=True)
            print "\nJOB: ", card.name, "\n"
            print card.description
            print "\n\n"
            for i in c:
                print i["date"], ":", i["data"]["text"]
    else:
        print "No such job"


def main():
    while True:
        print "Enter choice number:\n"
        print "1: Enter job to be searched"
        print "2: See total hours planed\n"
        choice = raw_input()
        if int(choice) == 1:
            print_card_info()
        else:
            if int(choice) == 2:
                print "\n\nTotal planned hours are: ", sum(cal_estimates("Planned")),"\n\n"

if __name__ == "__main__":
    main()