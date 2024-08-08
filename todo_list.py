class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'status': 'Pending'})

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, task):
        for t in self.tasks:
            if t['task'] == task:
                t['status'] = 'Completed'
                break

    def clear_tasks(self):
        self.tasks = []

    def edit_task(self, old_task, new_task):
        for t in self.tasks:
            if t['task'] == old_task:
                t['task'] = new_task
                break


if __name__ == "__main__":
    manager = ToDoListManager()
    manager.add_task("Comprar víveres")
    manager.add_task("Pagar facturas")
    print("Tareas iniciales:")
    print(manager.list_tasks())

    manager.mark_task_completed("Comprar víveres")
    print("Después de marcar 'Comprar víveres' como completada:")
    print(manager.list_tasks())

    manager.edit_task("Pagar facturas", "Pagar servicios públicos")
    print("Después de editar 'Pagar facturas' a 'Pagar servicios públicos':")
    print(manager.list_tasks())

    manager.clear_tasks()
    print("Después de borrar todas las tareas:")
    print(manager.list_tasks())
