import unittest
# Run file thru Terminal  => python -m unittest Task1.py

class MyClass(object):

    def __init__(self):
        return

    def getListWithoutDelimeters(self, arr):
        pole=arr
        for item in pole:
            if item.isnumeric()==False:
                if item != ",":
                    modify=pole.replace(item,',')
                    pole=modify
        pole2 = pole.split(',')
        return pole2


    def sumNumbers(self, arr):
        summa = 0
        for item in arr:
            if item.isnumeric() == True:
                if int(item) < 1000:
                    summa = summa + int(item)
        return summa


    def add(self,val):
        if (len(val)==0):
            return 0
        if (len(val)>=1):
            pole2=self.getListWithoutDelimeters(val)
            return self.sumNumbers(pole2)



class TddInPythonExample(unittest.TestCase):

    def test_when_Null(self):
        calc = MyClass()
        res1=calc.add("")
        self.assertEqual(0, res1)

    def test_when_One_Number(self):
        calc = MyClass()
        res2=calc.add("1")
        self.assertEqual(1, res2)

    def test_when_Two_Number(self):
        calc = MyClass()
        res3 = calc.add("1,2")
        self.assertEqual(3, res3)

    def test_when_More_Number(self):
        calc = MyClass()
        res4 = calc.add("1,3,5,2")
        self.assertEqual(11, res4)

    def test_when_Two_Numbers(self):
        calc = MyClass()
        res5 = calc.add("10,20")
        self.assertEqual(30, res5)

    def test_when_New_Lines(self):
        calc = MyClass()
        res6 = calc.add("1\n2,3")
        self.assertEqual(6, res6)

    def test_when_Delimiters(self):
        calc = MyClass()
        res7 = calc.add("//[:]\n1;20***3%")
        self.assertEqual(24, res7)

    def test_when_1000_Number_with_Delimiters_Ignored(self):
        calc = MyClass()
        res8 = calc.add("//[:]\n2,1001")
        self.assertEqual(2, res8)

    def test_when_1000_Number_with_Delimiters_Ignored2(self):
        calc = MyClass()
        res8 = calc.add("//[:]\n2,1001=$20000")
        self.assertEqual(2, res8)

if __name__ == '__main__':
    unittest.main()

