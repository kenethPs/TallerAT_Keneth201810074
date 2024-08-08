from behave import given, when, then
from todo_list import ToDoListManager


@given('the to-do list is empty')
def step_given_empty_list(context):
    context.manager = ToDoListManager()


@when('the user adds a task "{task}"')
def step_when_add_task(context, task):
    context.manager.add_task(task)


@then('the to-do list should contain "{task}"')
def step_then_check_task(context, task):
    tasks = [t['task'] for t in context.manager.list_tasks()]
    assert task in tasks


@given('the to-do list contains tasks: "{tasks}"')
def step_given_tasks(context, tasks):
    task_list = tasks.split(", ")
    context.manager = ToDoListManager()
    for task in task_list:
        context.manager.add_task(task)


@when('the user lists all tasks')
def step_when_list_tasks(context):
    context.listed_tasks = context.manager.list_tasks()


@then('the output should contain: "{tasks}"')
def step_then_check_output(context, tasks):
    expected_tasks = tasks.split(", ")
    actual_tasks = [t['task'] for t in context.listed_tasks]   
    for expected_task in expected_tasks:
        assert expected_task in actual_tasks, f"Task '{expected_task}' not found in {actual_tasks}"



@when('the user marks task "{task}" as completed')
def step_when_mark_completed(context, task):
    context.manager.mark_task_completed(task)


@then('the to-do list should show task "{task}" as completed')
def step_then_check_completed(context, task):
    tasks = context.manager.list_tasks()
    for t in tasks:
        if t['task'] == task:
            assert t['status'] == 'Completed'
            break


@when('the user clears the to-do list')
def step_when_clear_list(context):
    context.manager.clear_tasks()


@then('the to-do list should be empty')
def step_then_check_empty(context):
    assert len(context.manager.list_tasks()) == 0


@when('the user edits the task "{old_task}" to "{new_task}"')
def step_when_edit_task(context, old_task, new_task):
    context.manager.edit_task(old_task, new_task)
