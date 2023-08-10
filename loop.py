while True:
    def sum():
        num1 = int(input("add num 1: "))
        num2 = int(input("add num 2: "))
        sum_total = num1 + num2
        print("sum total: ", sum_total)
    #sum()

    def subtract():
        num1 = int(input("add num 1: "))
        num2 = int(input("add num 2: "))
        subtract_total = num1 - num2
        print("Subtract total: ", subtract_total)
    #subtract()

    def multiply():
        num1 = int(input("add num 1: "))
        num2 = int(input("add num 2: "))
        multiply_total = num1 * num2
        print("Multiply total: ", multiply_total)
    #multiply()

    def division():
        num1 = int(input("add num 1: "))
        num2 = int(input("add num 2: "))
        division_total = num1 / num2
        print("Division total: ", division_total)
    #division()

    def  triangle ():
        base_length = int(input("add Base length: "))
        height = int(input("add height: "))
        triangle_area = (base_length * height) / 2
        print("triangle area: ", triangle_area)
    #triangle()

    def circle ():
        radius = int(input("add Radius: "))
        circle_area = 3.14 * (radius ** 2)
        print("circle area: ", circle_area)
    #circle()

    def rectangle ():
        length = int(input("add length: "))
        width = int(input("add width: "))
        rectangle_area = length * width
        print("rectangle area: ", rectangle_area)
    #rectangle ()

    menu = int(input(f"""
                            1_ Sum
                            2_ Subtract
                            3_ Multiply
                            4_ Division
                            5_ Calculate triangle area
                            6_ Calculate circle area
                            7_ Calculate rectangle area
                            8_ Exit"""))
    print(menu)
    if menu == 1:
        print(sum())
    elif menu == 2:
        print(subtract())
    elif menu == 3:
        print(multiply())
    elif menu == 4:
        print(division())
    elif menu == 5:
        print(triangle())
    elif menu == 6:
        print(circle())
    elif menu == 7:
        print(rectangle())
    elif menu == 8:
        print("Exit")
        break
    else:
        print("Invalid Number. Try Again!")
    continue