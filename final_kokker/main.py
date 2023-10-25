from model import KoccerModel
from view import KoccerView
from user import KoccerUser
from controller import KoccerController

if __name__ == '__main__':
    model = KoccerModel()
    view = KoccerView()
    user = KoccerUser()
    controller = KoccerController(model, view, user)

    controller.start()
