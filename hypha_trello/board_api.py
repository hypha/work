from trello import TrelloClient
from config import *

class Board:

    def __init__(self):
        # API = "9cc1470c039f9f1bf8fe3ce35689a127"
        # TOKEN = "2093b976115e83e07b33321b359aa53a74d612aeec6373218d15796bd78a45b1"
        API = get_credentials()["api"]
        TOKEN = get_credentials()["token"]
        client = TrelloClient(api_key=API,
                              token=TOKEN)
        self.boards = client.list_boards()
#         self.job_board = boards[0]
#         self.onboarding_board = boards[1]
#         self.cards = self.job_board.get_cards() + self.onboarding_board.get_cards()
#
#     def match_card(self):
#         job_num = raw_input("Enter a job to be searched: ")
#         for card in self.cards:
#             match = re.search(job_num, card.name)
#             if match:
#                 return card
#
#     def print_card_info(self):
#         card = self.match_card()
#         comments = card.fetch_comments(force=True)
#         print "\nJOB: ", card.name, "\n"
#         print card.description
#         print "\n\n"
#         for i in comments:
#             print i["date"], ":", i["data"]["text"]
#
# board = Board()
# board.print_card_info()
#
