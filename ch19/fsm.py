class FsmManager:
    def __init__(self):
        self.currentState = None

    def update(self):
        if (self.currentState != None):
            self.currentState.update()

    def changeState(self, newState):
        if (self.currentState != None):
            self.currentState.exit()

        self.currentState = newState
        self.currentState.enter()
            
class StateOne:
    def __init__(self, fsm):
        self.count = 5
        self.fsm = fsm
        self.nextState = None

    def enter(self):
        print("Entering State One")

    def exit(self):
        print("Exiting State One")

    def update(self):
        print("Hello from StateOne!")
        self.count -= 1
        if (self.count == 0):
            fsm.changeState(self.nextState)

class StateTwo:
    def __init__(self, fsm):
        self.count = 5
        self.fsm = fsm
        self.nextState = None

    def enter(self):
        print("Entering State Two")

    def exit(self):
        print("Exiting State Two")

    def update(self):
        print("Hello from StateTwo!")
        self.count -= 1
        if (self.count == 0):
            fsm.changeState(self.nextState)

class StateQuit:
    def __init__(self, fsm):
        self.fsm = fsm

    def enter(self):
        print("Entering Quit")

    def exit(self):
        print("Exiting Quit")
    
    def update(self):
        print("Quitting...")
        exit()

fsm = FsmManager()
stateOne = StateOne(fsm)
stateTwo = StateTwo(fsm)
stateQuit = StateQuit(fsm)

stateOne.nextState = stateTwo
stateTwo.nextState = stateQuit

fsm.changeState(stateOne)

while True:
    fsm.update()







