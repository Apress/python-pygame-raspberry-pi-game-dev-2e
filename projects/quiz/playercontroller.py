from gpiozero import Button

class PlayerController(object):

    def __init__(self, pins):
        self.buttons = []
        self.score = 0
        for pin in pins:
            self.buttons.append(Button(pin))

    def anyButton(self):
        for button in self.buttons:
            if button.is_pressed:
                return True

        return False
    
    def playerChoice(self):
        index = 0
        for button in self.buttons:
            if button.is_pressed:
                return index
            index = index + 1

        return -1
