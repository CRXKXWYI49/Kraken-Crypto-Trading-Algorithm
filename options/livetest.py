from strategy import strategy
import threading

class LiveTest:
    def __init__(self):
        self.running = True

    def execute_strategy(self):
        while self.running:
            strategy(2)

    def check_user_input(self):
        while self.running:
            user_input = input("Enter 's' to stop Live Testing: \n")
            if user_input.strip().lower() == 's':
                self.running = False

    def start(self):
        strategy_thread = threading.Thread(target=self.execute_strategy)
        input_thread = threading.Thread(target=self.check_user_input)
        
        strategy_thread.start()
        input_thread.start()
        
        strategy_thread.join()
        input_thread.join()
        
        print("\nTesting stopped\n")





