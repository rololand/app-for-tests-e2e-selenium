class CalculatorTests:
    def test_navigate_to_app(self, app):
        app.task_list_menu_button.click()

    def test_add_three_new_task(self, app):
        app.add_new_task("Task 3")
        app.add_new_task("Task 4")
        app.add_new_task("Task 5")
        list_of_tasks = app.get_list_of_tasks()
        assert list_of_tasks == ["Task 5", "Task 4", "Task 3", "Task 1", "Task 2"]

    def test_mark_as_done_two_tasks(self, app):
        app.mark_as_done("Task 1")
        list_of_tasks = app.get_list_of_tasks()
        assert list_of_tasks == ["Task 5", "Task 4", "Task 3", "Task 2", "Task 1"]
        assert app.is_mark_as_done("Task 1")
        app.mark_as_done("Task 4")
        list_of_tasks = app.get_list_of_tasks()
        assert list_of_tasks == ["Task 5", "Task 3", "Task 2", "Task 4", "Task 1"]
        assert app.is_mark_as_done("Task 4")

    def test_delete_task(self, app):
        app.delete_task("Task 3")
        list_of_tasks = app.get_list_of_tasks()
        assert list_of_tasks == ["Task 5", "Task 2", "Task 4", "Task 1"]

    def test_add_new_task_and_mark_as_done(self, app):
        app.add_new_task("Task 6")
        list_of_tasks = app.get_list_of_tasks()
        assert list_of_tasks == ["Task 6", "Task 5", "Task 2", "Task 4", "Task 1"]
        app.mark_as_done("Task 6")
        list_of_tasks = app.get_list_of_tasks()
        assert list_of_tasks == ["Task 5", "Task 2", "Task 6", "Task 4", "Task 1"]

    def test_delete_done_task(self, app):
        app.delete_done_task("Task 4")
        list_of_tasks = app.get_list_of_tasks()
        assert list_of_tasks == ["Task 5", "Task 2", "Task 6", "Task 1"]