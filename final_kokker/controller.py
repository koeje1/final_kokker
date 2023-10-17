import random
from model import KokkerModel
from view import KokkerView

class KokkerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play_game(self):
        # 게임 진행: 플레이어의 잔고가 0보다 큰 동안 게임을 진행
        while self.model.coin > 0:
            self.view.show_balance(self.model.coin)
            team_choice = self.view.get_team_choice()
            bet_amount = self.view.get_bet_amount()

            if not self.model.deduct_coin(bet_amount):
                # 베팅 금액이 잔고를 초과하면 처음으로
                print("돈이 부족합니다.")
                continue

            confirm = self.view.confirm_bet()
            if confirm == "y":
                # 베팅 확정시, 한 게임 라운드를 플레이
                self.play_round(team_choice, bet_amount)
            else:
                # 베팅 취소시, 베팅 금액을 잔고에 반환
                self.model.add_coin(bet_amount)

    def play_round(self, team_choice, bet_amount):
        # 한 게임 라운드를 진행하는 메서드
        winning_team = random.choice(["a", "b", "t"])
        if team_choice == winning_team:
            winnings = self.calculate_winnings(team_choice, bet_amount)
            self.model.add_coin(winnings)
            self.view.show_result(winning_team, winnings)
        else:
            self.view.show_loss(winning_team)

    def calculate_winnings(self, team_choice, bet_amount):
        # 베팅 결과에 따른 수익을 계산하는 메서드
        if team_choice == "a":
            return bet_amount * self.model.allo_team_A
        elif team_choice == "b":
            return bet_amount * self.model.allo_team_B
        elif team_choice == "t":
            return bet_amount * self.model.allo_team_T
