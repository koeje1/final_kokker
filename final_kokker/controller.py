import random
import re
from model import KoccerModel
from view import KoccerView
from user import KoccerUser

class KoccerController:
    def __init__(self, model, view, user):
        self._model = model
        self._view = view
        self._user = user
        self.players = []
        self.previous_game = None

    def start(self):
        self._view.show_welcome_message()
        num_players = self._user.get_num_players()
        for i in range(num_players):
            player_name = self._user.get_user_name(i + 1)
            self.players.append(player_name)
            self._user.show_balance(player_name)

        while True:
            current_player = self.players[self._user.current_players_index]
            self._user.show_balance(current_player)

            if self._user.player_balances[current_player] <= 0:
                self._view.game_over(self._user.player_balances[current_player], current_player)
                return

            team_choice, bet_amount = self.get_player_bet_choice(current_player)
            confirm = self._view.confirm_bet()

            if confirm == "y":
                if self._user.deduct_coin(bet_amount, current_player):
                    self.play_round(team_choice, bet_amount, current_player)
                    self._user.current_players_index = (self._user.current_players_index + 1) % len(self.players)
            elif confirm == "n":
                continue

    def get_player_bet_choice(self, current_player):
        while True:
            team_choice = self._view.get_team_choice(current_player)
            bet_amount = self._view.get_bet_amount()

            if self._user.deduct_coin(bet_amount, current_player):
                return team_choice, bet_amount
            else:
                print("돈이 부족합니다. 다시 시도하세요.")

    def play_round(self, team_choice, bet_amount, current_player):
        # todo : 임시로 팀을 a, b, t 로 정의함, 나중에 실제 데이터를 적용시킬 예정
        choices_team = random.choice(["a", "b", "t"])
        if team_choice == choices_team:
            winnings = self.calculate_winnings(team_choice, bet_amount)
            self._user.player_balances[current_player] += winnings
            self._view.show_result(choices_team, winnings)
        elif team_choice != choices_team:
            self._user.player_balances[current_player] -= bet_amount
            self._view.show_loss(choices_team)

    def calculate_winnings(self, team_choice, bet_amount):
        if team_choice == "a":
            return bet_amount * self._model.allo_team_A
        elif team_choice == "b":
            return bet_amount * self._model.allo_team_B
        elif team_choice == "t":
            return bet_amount * self._model.allo_team_T
        else:
            raise Exception("없는 팀입니다. 현재팀 구성을 다시한번 확인하세요")