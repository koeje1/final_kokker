class KokkerModel:
    def __init__(self):
        # 초기 코인 잔고 설정
        self.coin = 1000

        # 최소 및 최대 베팅 코인 설정
        self.min_bet_coin = 10
        self.max_bet_coin = 10000

        # 팀 A, B, 무승부에 대한 배당률 설정
        self.allo_team_A = 2.0
        self.allo_team_B = 1.5
        self.allo_team_T = 1.2

    def deduct_coin(self, amount):
        # 베팅 금액을 현재 코인 잔고에서 차감하는 메서드
        if self.coin >= amount:
            self.coin -= amount
            return True
        return False

    def add_coin(self, amount):
        # 베팅에 성공한 경우 베팅 금액을 코인 잔고에 추가하는 메서드
        self.coin += amount