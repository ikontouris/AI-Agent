
from functions.run_python_file import run_python_file

test1 = run_python_file("calculator", "main.py")
test2 = run_python_file("calculator", "main.py", ["3 + 5"])
test3 = run_python_file("calculator", "tests.py")
test4 = run_python_file("calculator", "../main.py")
test5 = run_python_file("calculator", "nonexistent.py")
test6 = run_python_file("calculator", "lorem.txt")


tests = [test1,test2,test3,test4,test5,test6]
for t in tests:
    print(t)
