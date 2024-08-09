Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Comprar víveres"
    Then the to-do list should contain "Comprar víveres"

    
  Scenario: List all tasks in the to-do list
    Given the to-do list containstasks: "Comprar víveres, Pagar facturas"
    When the user lists all tasks
    Then the output should contain: "Comprar víveres, Pagar facturas"


  Scenario: Mark a task as completed
    Given the to-do list contains tasks: "Comprar víveres"
    When the user marks task "Comprar víveres" as completed
    Then the to-do list should show task "Comprar víveres" as completed


  Scenario: Clear the entire to-do list
    Given the to-do listcontains tasks:"Comprar víveres, Pagar facturas"
    When the user clears the to-do list
    Then the to-do list should be empty


  Scenario: Edit an existing task
    Given theto-do list contains tasks:"Pagar facturas"
    When the user edits the task "Pagar facturas" to "Pagar servicios públicos"
    Then the to-do list should contain"Pagar servicios públicos"