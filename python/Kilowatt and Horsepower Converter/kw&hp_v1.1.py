print(" ------------------------------------------------")
print("|                                                |")
print("| Welcome to the Kw and Hp converter by: Lezliee |")
print("|                                                |")
print(" ------------------------------------------------")
print()
print("Do you want to ")
print("a, Convert from kilowatts to horsepower")
print("b, Convert from horsepower to kilowatts")
print("[a/b]")
calculation_type = input()

if calculation_type == "a":
    print("Okay...")
    print("Now input the kilowatt value you want to convert into horsepower")
    val_kw = input()
    conv_hp = int(val_kw) * 1.3596216173
    print("Done!")
    print(val_kw, "kilowatt(s) is", conv_hp, "horsepower!")
    input("Press ENTER to exit")

if calculation_type == "b":
    print("Okay...")
    print("Now input the horsepower value you want to convert into kilowatt(s)")
    val_hp = input()
    conv_kw = int(val_hp) * 0.73549875
    print("Done!")
    print(val_hp, "horsepower is", conv_kw, "kilowatt(s)!")
    input("Press ENTER to exit")
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                Code by: Lezliee
#                                                          (https://github.com/Lezliee)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
