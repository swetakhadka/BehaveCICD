from behave import given, when, then


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


@given("I have a calculator")
def step_given_calculator(context):
    context.calculator = Calculator()  # Create a Calculator instance


@when("I add {a:d} and {b:d}")
def step_when_add(context, a, b):
    context.result = context.calculator.add(a, b)  # Perform addition


@when("I subtract {a:d} and {b:d}")
def step_when_subtract(context, a, b):
    context.result = context.calculator.subtract(a, b)  # Perform subtraction


@then("the result should be {expected:d}")
def step_then_result(context, expected):
    assert context.result == expected, f"Expected {expected}, but got {context.result}"

