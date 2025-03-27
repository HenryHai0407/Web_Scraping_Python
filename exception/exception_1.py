
class CustomException(Exception):
    def __init__(self,error_message):
        print(f"CustomException log: {error_message}")


def program(a,b):
    try:
        if a == 0 and b == 0:
            print(f"Equation has infinite solution")
            return
        if a == 0:
            raise CustomException("Division for zero")
        x = -b/a
        print(f"Equation has solution: {x}")
    except CustomException:
        print("Equation with no solution")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print(f"End the program")

if __name__ == "__main__":
    program(10,2)