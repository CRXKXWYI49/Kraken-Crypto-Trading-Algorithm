from options.livetest import LiveTest
from options.backtest import *
from options.livetrading import *


if __name__ == '__main__':

    print("\nLaunched Program\n")


    def display_menu():
        print("Select an Option\n")
        print("1 Backtest Algorithm")
        print("2 Livetest Algorithm")
        print("3 Start Live Trading")
        print("0 Exit\n")

    def main():
        while True:
            display_menu()

            try:
                choice = input()
            except EOFError:
                pass

            if choice == "1":
                print("\nStarting Back-testing...\n")
                # Add logic 

            elif choice == "2":
                print("\nStarting Live-testing...\n")
                live_test = LiveTest()
                live_test.start()


            elif choice == "3":
                verification = input("\nAre you sure? Y/N\n\n")
                if verification.strip().lower() == "y":
                    print("\nStarting Live Trading...\n")
                else: 
                    print("\nLive Trading Terminated\n")

            elif choice == "0":
                print("\nExiting Program\n")
                break

            else:
                print("Invalid Input (select a number between 0-3)")

    main()