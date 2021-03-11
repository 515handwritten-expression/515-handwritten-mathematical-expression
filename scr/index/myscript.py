# -*- coding: utf-8 -*-
import os

def my_func():
    # print 'in test 1, unproductive'
    cwd = os.getcwd() + "/results/"
    print(cwd)

    completeName1 = "calculationResult.txt"
    completeName2 = "MathJaxResult.txt"      

    with open(os.path.join(cwd ,completeName1), "w") as file1:
        toFile = "4"
        file1.write(toFile)
        file1.close()

    with open(os.path.join(cwd ,completeName2), "w") as file2:
        toFile2 = "2^{2}"
        file2.write(toFile2)
        file2.close()


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    my_func()