class KokkerView:
    def show_balance(self, coin):
        # 현재 코인 잔고를 화면에 출력
        print(f"현재 잔액: {coin}코인")

    def get_team_choice(self):
        # 플레이어에게 팀 선택을 요청하고 선택된 팀을 반환
        while True:
            bet_team =input("배팅할 팀을 선택하세요. (a, b, t(무승부) ): ")
            if bet_team in ['a', 'b', 't']:
                return bet_team
            else:
                print("올바른 값을 입력해 주세요.")


    def get_bet_amount(self):
        while True:
            try:
                # 플레이어에게 베팅할 코인 양을 입력받고 반환
                bet_amount = int(input("배팅할 코인을 입력하세요 (한 번에 걸 수 있는 최대 코인 10000): "))
                return bet_amount
            except ValueError:
                print("숫자를 입력해 주세요.")

    def confirm_bet(self):
        # 플레이어에게 베팅 확정 여부를 묻고 응답을 반환
        return input("정말로 배팅하시겠습니까? (y, n): ")

    def show_result(self, winning_team, winnings):
        # 베팅 결과를 출력
        if winning_team == "t":
            print("무승부입니다. 배팅에 성공하셨습니다.")
        else:
            print(f"{winning_team}팀이 이겼습니다. 배팅에 성공하셨습니다.")
        print(f"베팅에 대한 수익: {winnings}코인")

    def show_loss(self, winning_team):
        # 베팅 실패 결과를 출력
        if winning_team == "t":
            print("무승부입니다. 배팅에 실패하셨습니다.")
        else:
            print(f"{winning_team}가 이겼습니다. 배팅에 실패하셨습니다.")
