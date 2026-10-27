import unittest
import json
from unittest.mock import mock_open, patch
from todo_manager import TodoManager

class TestTodoManager(unittest.TestCase):
    
    def setUp(self):
        """Runs before every individual test to provide a fresh TodoManager instance."""
        self.manager = TodoManager(filepath="fake_tasks.json")

    # --- Core Functionality Tests ---

    def test_add_task_success(self):
        """Test adding a single task increases list size and defaults to incomplete."""
        task = self.manager.add_task("Buy groceries")
        
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(task["description"], "Buy groceries")
        self.assertFalse(task["completed"])

    def test_add_empty_task_raises_error(self):
        """Test that adding an empty or whitespace-only task raises a ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_task("")
            
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_mark_completed_success(self):
        """Test marking an existing task as completed."""
        self.manager.add_task("Write unit tests")
        updated_task = self.manager.mark_completed(0)
        
        self.assertTrue(updated_task["completed"])
        self.assertTrue(self.manager.tasks[0]["completed"])

    def test_mark_completed_out_of_bounds(self):
        """Test marking a task index that doesn't exist raises an IndexError."""
        self.manager.add_task("Walk the dog")
        
        with self.assertRaises(IndexError):
            self.manager.mark_completed(5)
            
        with self.assertRaises(IndexError):
            self.manager.mark_completed(-1)

    def test_delete_task_success(self):
        """Test deleting a task removes it and returns the deleted item."""
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        
        deleted_task = self.manager.delete_task(0)
        
        self.assertEqual(deleted_task["description"], "Task 1")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0]["description"], "Task 2")

    def test_delete_task_out_of_bounds(self):
        """Test deleting an invalid index raises an IndexError."""
        with self.assertRaises(IndexError):
            self.manager.delete_task(0)

    # --- File I/O Mocking Tests ---

    @patch("builtins.open", new_callable=mock_open)
    def test_save_to_file(self, mock_file):
        """Test that tasks are serialized and saved to file correctly."""
        self.manager.add_task("Save me")
        self.manager.save_to_file()
        
        mock_file.assert_called_once_with("fake_tasks.json", "w", encoding="utf-8")
        
        # Capture what was written to file
        written_data = "".join(call.args[0] for call in mock_file().write.call_args_list)
        parsed_json = json.loads(written_data)
        self.assertEqual(parsed_json, [{"description": "Save me", "completed": False}])

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='[{"description": "Loaded task", "completed": true}]')
    def test_load_from_file_success(self, mock_file, mock_exists):
        """Test loading tasks from an existing JSON file."""
        self.manager.load_from_file()
        
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0]["description"], "Loaded task")
        self.assertTrue(self.manager.tasks[0]["completed"])

    @patch("os.path.exists", return_value=False)
    def test_load_from_file_not_found(self, mock_exists):
        """Test loading raises FileNotFoundError when the target file does not exist."""
        with self.assertRaises(FileNotFoundError):
            self.manager.load_from_file()

if __name__ == "__main__":
    unittest.main()