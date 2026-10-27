import json
import os
from typing import List, Dict

class TodoManager:
    def __init__(self, filepath: str = "tasks.json"):
        self.filepath = filepath
        self.tasks: List[Dict[str, str | bool]] = []

    def add_task(self, description: str) -> Dict[str, str | bool]:
        """Adds a new task to the list."""
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty.")
        
        task = {
            "description": description.strip(),
            "completed": False
        }
        self.tasks.append(task)
        return task

    def mark_completed(self, index: int) -> Dict[str, str | bool]:
        """Marks a task at the given 0-based index as completed."""
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")
        
        self.tasks[index]["completed"] = True
        return self.tasks[index]

    def delete_task(self, index: int) -> Dict[str, str | bool]:
        """Removes a task at the given 0-based index."""
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")
        
        return self.tasks.pop(index)

    def save_to_file(self) -> None:
        """Saves current tasks to a JSON file."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4)

    def load_from_file(self) -> None:
        """Loads tasks from a JSON file if it exists."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File '{self.filepath}' does not exist.")
        
        with open(self.filepath, "r", encoding="utf-8") as f:
            self.tasks = json.load(f)