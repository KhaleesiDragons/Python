import unittest
# Run file thru Terminal  => python -m unittest PythonTask.py

class MyClass(object):

    def __init__(self):
        return

    def sumNumbers(self, arr):
        summa = 0
        for item in arr:
            if item!='':
                if int(item)<1000:
                    summa = summa + int(item)
        return summa


    def add(self,val):
        if (len(val)==0):
            return 0
        if (len(val)>=1):
            arr=val.split(',')
            res=self.sumNumbers(arr)
            return res

    def removeDelimeters(self,delimeter, line):
        result=line.replace(delimeter,',')
        return result

    def when_Delimiters(self,lines):
        arr1 = [ "\n" , "//" , "[:]" , ";" , "***","%"]
        pole = lines
        for item in arr1:
            modify_arr=self.removeDelimeters(item, pole)
            pole=modify_arr
        return self.add(pole)


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
        res6 = calc.when_Delimiters("1\n2,3")
        self.assertEqual(6, res6)

    def test_when_Delimiters(self):
        calc = MyClass()
        res7 = calc.when_Delimiters("//[:]\n1;20***3%")
        self.assertEqual(24, res7)

    def test_when_1000_Number_with_Delimiters_Ignored(self):
        calc = MyClass()
        res8 = calc.when_Delimiters("//[:]\n2,1001")
        self.assertEqual(2, res8)

if __name__ == '__main__':
    unittest.main()

