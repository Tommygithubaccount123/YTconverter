import converter

def length_tests():
    assert (converter.length(60)=="0:01:00")

if __name__ == "__main__":
    print("1. Length function")

    choice = input("Enter number: ")
    while (choice != "1"):
        choice = input("Enter number: ")
    
    if (choice == "1"):
        length_tests()