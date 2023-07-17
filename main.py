class Window:
    def __init__(self):
        pass

class Calcualtor:
    def __init__(self):
        pass

class App:
    def __init__(self):
        pass


difficluty_level = None

def set_leve(name):
    '''
    name: имя кнопки (1, 2, 3 уровни сложности)
    return: None
    '''
    global difficluty_level

    if difficluty_level is None:
        difficluty_level = name



