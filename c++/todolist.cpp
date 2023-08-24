#include <iostream>
#include <vector>
#include <string>

struct Task {
    std::string description;
    bool completed;

    Task(const std::string& desc) : description(desc), completed(false) {}
};

void addTask(std::vector<Task>& taskList, const std::string& description) {
    taskList.push_back(Task(description));
    std::cout << "Task added: " << description << std::endl;
}

void viewTasks(const std::vector<Task>& taskList) {
    std::cout << "Task List:\n";
    for (size_t i = 0; i < taskList.size(); ++i) {
        std::cout << i + 1 << ". ";
        if (taskList[i].completed) {
            std::cout << "[X] ";
        } else {
            std::cout << "[ ] ";
        }
        std::cout << taskList[i].description << std::endl;
    }
}

void markTaskCompleted(std::vector<Task>& taskList, size_t taskIndex) {
    if (taskIndex < taskList.size()) {
        taskList[taskIndex].completed = true;
        std::cout << "Task marked as completed: " << taskList[taskIndex].description << std::endl;
    } else {
        std::cout << "Invalid task index." << std::endl;
    }
}

void removeTask(std::vector<Task>& taskList, size_t taskIndex) {
    if (taskIndex < taskList.size()) {
        std::cout << "Task removed: " << taskList[taskIndex].description << std::endl;
        taskList.erase(taskList.begin() + taskIndex);
    } else {
        std::cout << "Invalid task index." << std::endl;
    }
}

int main() {
    std::vector<Task> tasks;

    std::cout << "Welcome to the Task Management System!\n";

    while (true) {
        std::cout << "\nOptions:\n";
        std::cout << "1. Add Task\n";
        std::cout << "2. View Tasks\n";
        std::cout << "3. Mark Task as Completed\n";
        std::cout << "4. Remove Task\n";
        std::cout << "5. Exit\n";
        std::cout << "Choose an option: ";

        int choice;
        std::cin >> choice;

        switch (choice) {
            case 1: {
                std::cout << "Enter task description: ";
                std::string description;
                std::cin.ignore(); // Clear newline character from previous input
                std::getline(std::cin, description);
                addTask(tasks, description);
                break;
            }
            case 2:
                viewTasks(tasks);
                break;
            case 3: {
                size_t taskIndex;
                std::cout << "Enter task index to mark as completed: ";
                std::cin >> taskIndex;
                markTaskCompleted(tasks, taskIndex - 1); // Convert to 0-based index
                break;
            }
            case 4: {
                size_t taskIndex;
                std::cout << "Enter task index to remove: ";
                std::cin >> taskIndex;
                removeTask(tasks, taskIndex - 1); // Convert to 0-based index
                break;
            }
            case 5:
                std::cout << "Exiting the program.\n";
                return 0;
            default:
                std::cout << "Invalid choice. Please choose a valid option.\n";
        }
    }

    return 0;
}
