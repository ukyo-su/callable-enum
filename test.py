from callable_enum import CallableEnum, register


def test_call():
    class Test(CallableEnum):
        @register("A")
        def A(self):
            return self.value

        @register("B")
        def B(self):
            return "B"

    assert Test.A() == "A"
    assert Test.B() == "B"


def test_value():
    class Test(CallableEnum):
        @register(3)
        def A(self):
            pass

        @register(2)
        def B(self):
            pass

    assert Test.A.value == 3
    assert Test.B.value == 2
