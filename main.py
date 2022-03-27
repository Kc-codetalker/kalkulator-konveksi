import kalkulator_lusin as dozen
import kalkulator_payroll as payroll

def main():
    print("""=====================================
** Welcome to Konveksi Calculator! **
=====================================""")
    mode = input("""Please enter one of the numbers below for which mode do you want to use.
    (1) Payroll calculator ("gajian")
    (2) Dozen calculator
    (0) Exit
>>>> """)
    try:
        mode = int(mode)
    except:
        print("Mode input should be a number!")
        return

    if (mode == 0):
        print("Exitting...")
    elif (mode == 1):
        print("You chose Payroll calculator.")
        payroll.payroll_calc_runner()
    elif (mode == 2):
        print("You chose Dozen calculator.")
        dozen.dozen_calc_runner()
    else:
        print("Please choose one of the available numbers.")

if __name__ == '__main__':
    main()