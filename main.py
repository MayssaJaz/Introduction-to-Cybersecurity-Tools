from getout import getout
from menu import menu
from welcome_hacker_flag import welcome_hacker
from login import signin, signup


def main():
    print("\n──────────────────Welcome hacker──────────────────\n")
    welcome_hacker()

    print("\n\n──────────────────Identify yourself──────────────────\n")
    print("\t1. Login")
    print("\t2. Register")
    choice = int(input("\nYour choice : "))
    if choice == 1:
        print("login")
        test = signin()
        if (test == False):
            getout()
        else:
            menu(test)

        # if login correct => go to menu
    elif choice == 2:
        print("register")
        signup()
        # after registration => go to login
    else:
        getout()


if __name__ == '__main__':
    main()
