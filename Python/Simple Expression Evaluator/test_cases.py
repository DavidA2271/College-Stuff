from main import main


def run_test_cases():
    main("3+5+2+6")
    print()
    main("3+5*2-6/3")
    print()
    main("3*(5+2)/6")
    print()
    main("3+5^2+6")
    print()
    main("9/0")
    print()
    main("(4+2+5*6")
    print()
    main("4+2)+5*6")
    print()
    main("a+b")
    print()


if __name__ == "__main__":
    run_test_cases()