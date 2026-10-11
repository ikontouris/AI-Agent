
from functions.write_file import write_file

test1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
test2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
test3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")


tests = [test1,test2,test3]
for t in tests:
    print(t)
