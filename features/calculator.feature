Feature: Calculator operations

  Scenario: Add two numbers
    Given I have a calculator
    When I add 2 and 3
    Then the result should be 5
    Given I have a calculator
    When I subtract 3 and 2
    Then the result should be 1

#  Scenario: Subtract two numbers
#    Given I have a calculator
#    When I subtract 3 and 2
#    Then the result should be 1

