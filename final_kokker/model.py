class KoccerModel:
    def __init__(self):

        # 최소 및 최대 베팅 코인 설정
        self.min_bet_coin = 10
        self.max_bet_coin = 10000

        # 팀 A, B, 무승부에 대한 배당률 설정
        self.allo_team_A = 2.0
        self.allo_team_B = 1.5
        self.allo_team_T = 1.2

