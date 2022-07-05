import logging as lg

lg.basicConfig(filename="Guessgame.log",level=lg.INFO,format="%(asctime)s %(name)s %(levelname)s %(message)s")



class Guessgame:

    lg.info("Guessgame is started")
    def interface(self):
        """
        Docstring:
        This function will print the interface of the game on the console
        """
        try:
            print("------------------------------------------------------------------")
            print("Lets play a game")
            print("I will keep a number in my mind and you have to guess that number.")
            print("The number will be from 1 to 20.")
            print("You will have 5 tries to guess it.")
            print("------------------------------------------------------------------")

        except Exception as e:
            lg.info(e)
            print(e)

    def logic(self):
        """
        Docstring:
        This function is the logic of the game.
        """
        # no is the list of numbers from 1 to 20
        no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        # importing random f
        import random
        # num will store a coise of number from no list
        num = random.choice(no)
        # Using for loop for 5 tries
        for i in range(1, 5 + 1):
            try:
                guess = int(input("Guess the number :"))
                lg.info(f"User has guessed a number {guess}")
                if num == guess:
                    print(f"You have guess the right number congrats the number was {num}")
                    print(f"And the attempt was {i}")
                    lg.info("User has entered a right guess no of attempt {},no was{}".format(i,num))
                    break
                elif guess > num:
                    print("The number is a smaller number than this")
                elif guess < num:
                    print("The number is a greater number than this")
                else:
                    if i > 4:
                        print(f"You have {i} tries left")
                        lg.info("User has entered a wrong guess no of attempt {}".format(i))
                    else:
                        print("Game over you lost the number was {}".format(num))
            except Exception as e:
                lg.info(e)
                print("You have enterd a wrong input",e)

    def __str__(self):
        return "This is a guessgame class"


def main():
    start = Guessgame()
    start.interface()
    start.logic()


if __name__ == '__main__':
    main()
