import re
class KoccerUser:
    def __init__(self):
        self.players = []
        self.current_players_index = 0
        # 초기 코인 잔고 설정
        self.player_balances = {}

    def initialize_player_balance(self, player_name, initial_balance=1000):
        self.player_balances[player_name] = initial_balance
        # 사용자의 잔액 설정 및 조회 메서드 추가

    def get_num_players(self):
        try:
            return int(input("참여할 플레이어의 수를 입력해 주세요: "))
        except ValueError:
            print("올바른 숫자를 입력해 주세요.")
            return self.get_num_players()

    def get_user_name(self, player_number):
        while True:
            player_input = input(f"플레이어 {player_number}의 이름을 입력하세요: ")
            if self.is_valid_name(player_input):
                self.players.append(player_input)
                self.initialize_player_balance(player_input)
                return player_input

    def is_valid_name(self, player_input):
        # 조건을 충족하는지 확인하는 메서드
        _user_name_length = self.user_name_length(player_input)
        _special_characters = self.special_characters(player_input)
        _user_name_gap = self.user_name_gap(player_input)
        _duplication = self.duplication(player_input)
        if _user_name_length and _special_characters and _user_name_gap and _duplication:
            return True
        return False

    def user_name_length(self, player_input):
        # 이름의 길이를 확인하는 매서드
        if len(player_input) < 6 or len(player_input) >= 11:
            print("오류: 플레이어 이름은 6자 이상 10자 미만이어야 합니다.")
            return False
        return True

    def special_characters(self, player_input):
        # 특수문자를 확인하는 매서드
        if re.search(r'[!#$%^&*()_+{}\[\]:;<>,.?~\\]',player_input):
            print("오류: 플레이어 이름에 특수문자(@제외)는 포함될 수 없습니다.")
            return False
        return True

    def user_name_gap(self, player_input):
        # 공백을 확인하는 매서드
        if " " in player_input:
            print("오류: 공백을 포함한 이름은 허용되지 않습니다.")
            return False
        return True

    def duplication(self, player_input):
        if player_input in self.players:
            print("이름이 이미 사용 중입니다. 다른 이름을 선택하세요.")
            return False
        return True

    def deduct_coin(self, bet_amount, player_name):
        # 베팅 금액을 현재 코인 잔고에서 차감하는 메서드
        if self.player_balances[player_name] >= bet_amount:
            # self.player_balances[player_name] -= bet_amount
            return True
        return False

    def add_coin(self, bet_amount, player_name):
        # 베팅에 성공한 경우 베팅 금액을 코인 잔고에 추가하는 메서드
        self.player_balances[player_name] += bet_amount

    def show_balance(self, player_name):
        # 현재 코인 잔고를 화면에 출력
        print(f"{player_name}님의 현재 잔액: {self.player_balances[player_name]}코인")





