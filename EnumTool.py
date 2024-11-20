import sys
from socialrecon import reconinput
from webvuln import Webvuln
from color import Color
import os

# Clear the screen
os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen based on the OS

def main():
    print(Color.CYAN + """
  ____________________________________________________________________________________________________________________________________________________________        
  |\____________/\_________/\____/\__/\__/\___________/\__________/\_____________/\_____/___/_____\______/_____/_____\_____/_______\__________/\__/______/___\                                                                                                                                                          |
  |  $$$$$$$$$$\   $$$$$$$|       $$$|   $$$       $$$    $$$$$$$$\               $$$$$$$   $$$$$$$$$$$$$                                      $$$           | 
  |  $$$$$$$$$$/   $$$$$$$|       $$$|   $$$       $$$    $$$$$$$$/              $$$$$$$$   $$$$$$$$$$$$$                                      $$$           |
  |  $$$           $$$  \$$$      $$$|   $$$       $$$    $$$   $$$             $$$   $$$        $$$         $$$$$$$$            $$$$$$$$      $$$           |   
  |  $$$           $$$   \$$$     $$$|   $$$       $$$    $$$    $$$           $$$    $$$        $$$       $$$      $$$        $$$      $$$    $$$           |
  |  $$$$$$$$$$\   $$$    \$$$    $$$|   $$$       $$$    $$$     $$$         $$$     $$$        $$$      $$$        $$$      $$$        $$$   $$$           |
  |  $$$$$$$$$$/   $$$     \$$$   $$$|   $$$       $$$    $$$      $$$       $$$      $$$        $$$     $$$          $$$    $$$          $$$  $$$           |
  |  $$$           $$$      \$$$  $$$|   $$$       $$$    $$$       $$$     $$$       $$$        $$$     $$$          $$$    $$$          $$$  $$$           |
  |  $$$           $$$       \$$$ $$$|   $$$       $$$    $$$        $$$   $$$        $$$        $$$      $$$        $$$      $$$        $$$   $$$           |
  |  $$$$$$$$$$\   $$$        \$$$$$$|   $$$       $$$    $$$         $$$ $$$         $$$        $$$       $$$      $$$        $$$      $$$    $$$           |
  |  $$$$$$$$$$/   $$$         \$$$$$|   $$$$$$$$$$$$$    $$$         /$$$$$\         $$$        $$$         $$$$$$$$            $$$$$$$$      $$$$$$$$$$$$$ |
  |/___\_/_\____/_/___\________/_____\___/___\_______\____\__/________/_____\_________/__\______/___\_______\________\___________\_______\____/_____________\|
    """)
    print(Color.YELLOW + "                                           Created By : Sakib Sheikh and Naved Shaikh")
    print(Color.YELLOW + "                                                     Roll No.: 732 & 731")
    print(Color.GREEN + """
                \nSelect From Available Modules 
           
           1. Information gathering,
           2. Web vulnerability scanning,
           3. Exit 
    """) 
    print(Color.RED + "         Note: On both modules, type 'tools' to find tools.")
    
    while True:
        try:
            module_choice = int(input(Color.GREEN + "Enter Module >> "))
            if module_choice == 1:
                reconinput()

            elif module_choice == 2:
                Webvuln()
            
            elif module_choice == 3:
                print(Color.RED + "Exiting Program...")
                sys.exit(3)

            else:
                print(Color.RED + "Invalid input. Please choose 1 or 2.")

        except ValueError:
            print(Color.RED + "Invalid input. Please enter a number." + Color.RESET)
        
        except KeyboardInterrupt:
            print(Color.RED + "\nProgram Interrupted by user." + Color.RESET)
            sys.exit(1)
        
        except Exception as e:
            print(Color.RED + f"An error occurred: {e}" + Color.RESET)
            sys.exit(1)

if __name__ == "__main__":
    main()
