# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def hailstone(val):
    count=0
    while val!=1:
         if val%2==0:
            val=val/2
            count+=1
         elif val%2>0:
              val=3*val+1
              count+=1
    return count

# print(hailstone(9))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
