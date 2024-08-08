Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Comprar víveres"
    Then the to-do list should contain "Comprar víveres"

    
  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks: "Comprar víveres, Pagar facturas"
    When the user lists all tasks
    Then the output should contain: "Comprar víveres, Pagar facturas"