#!/usr/bin/env python3

import os
import sys

BANNER = r"""
============================================
              KRISHAN-X
============================================
          Security Tools Launcher
             Version 1.0
============================================
"""

def pause():
    input("\nPress Enter to continue...")

def clear():
    os.system("clear")

def main():
    while True:
        clear()
        print(BANNER)
        print("[1] Repository information")
        print("[2] Security learning")
        print("[3] Local system information")
        print("[4] Project files")
        print("[0] Exit")
        print()

        choice = input("KRISHAN-X Choose : ").strip()

        if choice == "1":
            clear()
            print(BANNER)
            print("KRISHAN-X")
            print("Customized distribution based on DarkFly-Tool.")
            print("Original attribution and license are retained.")
            pause()

        elif choice == "2":
            clear()
            print(BANNER)
            print("Security Learning")
            print("-----------------")
            print("• Web security fundamentals")
            print("• Linux/Termux fundamentals")
            print("• Network security concepts")
            print("• Defensive security testing")
            print("• Authorized lab practice")
            pause()

        elif choice == "3":
            clear()
            print(BANNER)
            os.system("uname -a")
            print()
            os.system("python3 --version")
            pause()

        elif choice == "4":
            clear()
            print(BANNER)
            os.system("find . -maxdepth 2 -type f | sort")
            pause()

        elif choice == "0":
            clear()
            print("Exiting KRISHAN-X...")
            sys.exit(0)

        else:
            print("\nInvalid option.")
            pause()

if __name__ == "__main__":
    main()
