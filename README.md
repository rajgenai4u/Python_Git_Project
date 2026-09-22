# Python Git Project

A simple Python inheritance project demonstrating a base `User` class with `Student`, `Mentor`, and `Admin` subclasses.

## Repository

- GitHub: https://github.com/rajgenai4u/Python_Git_Project

## Project Structure

| File       | Description                                          |
|------------|------------------------------------------------------|
| `main.py`  | Entry point - creates sample users and prints details |
| `user.py`  | Base `User` class (id, name, email)                  |
| `student.py` | `Student` subclass (Role: Student, Learning Dashboard access) |
| `mentor.py` | `Mentor` subclass (Role: Mentor)                     |
| `admin.py` | `Admin` subclass (Role: Admin)                       |
| `.gitignore` | Ignores `__pycache__/`, `.env`, `.vscode/`, `.pyc` |

## How to Run

```bash
python3 main.py
```

## Sample Output

```
 ID: 101
 Name: Rajesh
 Email: rajesh@gmail.com
Role: Student
Access: Learning Dashboard

 ID: 201
 Name: Parimala
 Email: parimala@gmail.com
Role: Mentor

 ID: 301
 Name: Ritik
 Email: ritik@gmail.com
Role: Admin
```

## Operations Performed

1. **Repository initialization**
   - Created the project directory and initialized a Git repository with `git init`.
   - Added the remote origin: `git@github.com:rajgenai4u/Python_Git_Project.git`.

2. **Initial project files created**
   - Created `.gitignore` to exclude `__pycache__/`, `.env`, `.vscode/`, and `.pyc` files.
   - Created the base `User` class in `user.py`.
   - Created `Student`, `Mentor`, and `Admin` subclasses.
   - Created `main.py` to demonstrate the inheritance hierarchy.

3. **First commit - `c1fd660` "Created base user class"**
   - Added 6 files, 45 insertions.

4. **Enhancement - `e0da61d` "Added student dashboard access information"**
   - Added "Access: Learning Dashboard" line to `student.py` (1 insertion).

5. **Bug fixes - `a7cf5a6` "fixed the erros in python files"**
   - Fixed syntax errors across all Python files (7 insertions, 7 deletions):
     - `user.py`: `init` -> `__init__`, fixed `f-string` quotes
     - `student.py`: added missing colon after `class Student(User)`
     - `mentor.py`: removed trailing colon on `from user import User`
     - `admin.py`: replaced misplaced `print()` with correct indentation in `display_details`
     - `main.py`: removed double comma (`301,,` -> `301,`)
   - Verified with `python3 main.py` (runs successfully).

6. **Push to GitHub**
   - Pushed the `main` branch to `origin` at https://github.com/rajgenai4u/Python_Git_Project.

## Git History

| Commit   | Date       | Description                                    |
|----------|------------|------------------------------------------------|
| `c1fd660`| 2026-09-22 | Created base user class                        |
| `e0da61d`| 2026-09-22 | Added student dashboard access information     |
| `a7cf5a6`| 2026-09-22 | Fixed the errors in python files               |