def main():
    cel = float(input("Enter value in Celcius: "))
    f = (cel * 1.8) + 32
#     print(f)
    print('%.2f Celcius is equal to = %.2f Degrees Fahrenheit' % (cel, f))



if __name__ == '__main__':
    main()
