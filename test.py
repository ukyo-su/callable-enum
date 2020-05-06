from callable_enum import CallableEnum, member_with_value, member


def test_call():
    class Test(CallableEnum):
        @member
        def A(self):
            return "A"

        @member
        def B(self):
            return "B"

    assert Test.A() == "A"
    assert Test.B() == "B"


def test_call_arg():
    class Test(CallableEnum):
        @member_with_value(1)
        def ADD1(self, x):
            return self.value + x

        @member_with_value(2)
        def SUB2(self, x):
            return x - self.value

    assert Test.ADD1(1) == 2
    assert Test.SUB2(2) == 0


def test_value():
    class Test(CallableEnum):
        @member_with_value(3)
        def A(self):
            pass

        @member_with_value(2)
        def B(self):
            pass

    assert Test.A.value == 3
    assert Test.B.value == 2
