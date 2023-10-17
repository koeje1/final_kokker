# import random
#
# class Kokker:
#     def __init__(self):
#         self.initialize_game()
#
#     def initialize_game(self):
#         self.initial_coin = 1000
#         self.coin = self.initial_coin
#         self.min_bet_coin = 10
#         self.max_bet_coin = 10000
#         self.allo_team_A = 2.0
#         self.allo_team_B = 1.5
#         self.allo_team_T = 1.2
#
#     def choose_team(self):
#         while True:
#             self.team_choice = input("배팅할 팀을 선택하세요. (a, b, t(무승부) ): ")
#             if self.team_choice not in ["a", "b", "t"]:
#                 print('올바른 값을 입력해 주세요.')
#                 print(f"현재 잔액: {self.coin}코인")
#                 raise AttributeError("올바른 팀을 입력해 주세요")
#             else:
#                 break
#
#     def validate_bet_amount(self, bet_amount):
#         if bet_amount > self.coin:
#             print("현재 코인보다 많은 코인을 입력할 수 없습니다.")
#             return False
#         elif bet_amount > self.max_bet_coin:
#             print("한 번에 10000코인 이상 입력할 수 없습니다.")
#             return False
#         elif bet_amount < self.min_bet_coin:
#             print("10코인 이상 입력하세요.")
#             return False
#         return True
#
#     def enter_bet_amount(self):
#         while True:
#             try:
#                 bet_amount = int(input("배팅할 코인을 입력하세요 (한 번에 걸 수 있는 최대 코인 10000): "))
#                 if self.validate_bet_amount(bet_amount):
#                     self.bet_amount = bet_amount
#                     break
#             except ValueError:
#                 print("숫자를 입력해 주세요.")
#                 continue
#
#     def play(self):
#         while self.coin > 0:
#             print(f"현재 잔액: {self.coin}코인")
#             self.choose_team()
#             self.enter_bet_amount()
#             self.handle_betting_result()
#             if self.team_choices():
#                 self.win_betting()
#             else:
#                 self.lose_betting()
#
#
#     def lack_coin(self):
#         while self.coin <= 0:
#             print("배팅금액이 부족합니다. 충전 후 이용바랍니다.")
#             break
#
#     def handle_betting_result(self):
#         self.choice = input("정말로 배팅하시겠습니까? (y, n): ")
#         if self.choice == "n":
#             return
#         self.winning_team = random.choice(["a", "b", "t"])
#
#     def team_choices(self):
#         if self.team_choice == self.winning_team:
#             return True
#
#     def win_betting(self):
#         if self.team_choice == "a":
#             self.winnings = self.bet_amount * self.allo_team_A + self.bet_amount
#         elif self.team_choice == "b":
#             self.winnings = self.bet_amount * self.allo_team_B + self.bet_amount
#         elif self.team_choice == "t":
#             self.winnings = self.bet_amount * self.allo_team_T + self.bet_amount
#         self.coin += self.winnings - self.bet_amount
#         if self.winning_team == "t":
#             print("무승부입니다. 배팅에 성공하셨습니다.")
#         else:
#             print(f"{self.winning_team}팀이 이겼습니다. 배팅에 성공하셨습니다.")
#         print(f"베팅에 대한 수익: {self.winnings - self.bet_amount}코인")
#
#     def lose_betting(self):
#         if self.winning_team == "t":
#             print("무승부입니다. 배팅에 실패하셨습니다.")
#         else:
#             print(f"{self.winning_team}가 이겼습니다. 배팅에 실패하셨습니다.")
#         self.coin -= self.bet_amount
#
# if __name__ == '__main__':
#     game = Kokker()
#     game.play()