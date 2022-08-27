import unittest


class TestMethods(unittest.TestCase):

    def assert_equals(self,a,b):
        self.assertEqual(a,b)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

def number(arg,n):
    if arg:
        return arg[0](n,arg[1])
    else:
        return n

def zero(arg=False):
    return number(arg,n=0)
def one(arg=False):
    return number(arg,n=1)
def two(arg=False):
    return number(arg,n=2)
def three(arg=False):
    return number(arg,n=3)
def four(arg=False):
    return number(arg,n=4)
def five(arg=False):
    return number(arg,n=5)
def six(arg=False):
    return number(arg,n=6)
def seven(arg=False):
    return number(arg,n=7)
def eight(arg=False):
    return number(arg,n=8)
def nine(arg=False):
    return number(arg,n=9)

def plus(a=False,b=False):
    if b is not False:
        return(a + b)
    else:
        return plus, a
def minus(a=False,b=False):
    if b is not False:
        return(a - b)
    else:
        return minus, a
def times(a=False,b=False):
    if b is not False:
        return(a * b)
    else:
        return times, a
def divided_by(a=False,b=False):
    if b is not False:
        return(int(a // b))
    else:
        return divided_by, a


if __name__ == '__main__':
    # five()
    # print(times(five()))
    print(seven(times(five())))
    print(seven(divided_by(five())))

    test = TestMethods()
    test.assert_equals(seven(times(five())), 35)



