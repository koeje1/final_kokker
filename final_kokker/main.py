from model import KokkerModel
from view import KokkerView
from controller import KokkerController

if __name__ == '__main__':
    model = KokkerModel()
    view = KokkerView()
    controller = KokkerController(model, view)
    controller.play_game()