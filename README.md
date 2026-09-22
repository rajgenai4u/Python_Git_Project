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
Role : Mentor

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
   - Changes: 6 files, 45 insertions(+)
   - Files modified/added: `.gitignore`, `admin.py`, `main.py`, `mentor.py`, `student.py`, `user.py`

4. **Enhancement - `e0da61d` "Added student dashboard access information"**
   - Changes: 1 file, 1 insertion(+)
   - Modified: `student.py` - Added "Access: Learning Dashboard"

5. **Bug fixes - `a7cf5a6` "fixed the erros in python files"**
   - Changes: 5 files, 7 insertions(+), 7 deletions(-)
   - Fixes applied:
     - `user.py`: `init` → `__init__`, fixed f-string quotes
     - `student.py`: added missing colon after `class Student(User)`
     - `mentor.py`: removed trailing colon on import line
     - `admin.py`: corrected indentation in `display_details`
     - `main.py`: fixed syntax error (removed double comma `301,,`)
   - Verified functionality with `python3 main.py` - runs successfully.

6. **Documentation - `8b61114` "Added README documentation"**
   - Changes: 1 file, 82 insertions(+)
   - Added: Comprehensive `README.md` with project structure, usage, and operations.

7. **Update .gitignore - `4b3a44a` "Updated .gitignore"**
   - Changes: 1 file, 4 insertions(+), 2 deletions(-)
   - Updated to properly include `__pycache__/` and `*.pyc`

8. **Update Mentor - `1829645` "Updated Mentor file"**
   - Changes: 1 file, 1 insertion(+), 3 deletions(-)
   - Modified: `mentor.py` - minor formatting adjustment to print statement

## Git Commands Used

```bash
# Repository initialization
git init
git remote add origin git@github.com:rajgenai4u/Python_Git_Project.git

# Check status and changes
git status
git diff
git diff --staged

# Stage and commit changes
git add .
git add <specific-file>
git commit -m "commit message"

# View history
git log --oneline
git log --pretty=format:"%h | %ad | %s" --date=format:"%Y-%m-%d %H:%M"
git log --stat --pretty=format:"%h | %s"

# Push to remote
git push -u origin main
git push origin main
```

## Git Command Transcript (Demonstration)

```bash
# Initialize and add remote (if starting fresh)
git init
git remote add origin git@github.com:rajgenai4u/Python_Git_Project.git

# Check current status
git status
# Output: On branch main, working tree clean

# Check unstaged changes
git diff
# Output: (no changes when clean)

# Stage files
git add README.md
git diff --staged
# Shows staged changes for README.md

# Commit
git commit -m "Update README"

# View commit history
git log --oneline -10
# Output: ad8023c Fix .gitignore content
#          7a23f51 Add Git commands section with examples
#          7c7eece Update README with complete operations and git history
#          1829645 Updated Mentor file
#          4b3a44a Updated .gitignore
#          8b61114 Added README documentation
#          a7cf5a6 fixed the erros in python files
#          e0da61d Added student dashboard access information
#          c1fd660 Created base user class

# View full diff of a commit
git show --stat ad8023c
# Output: ad8023c Fix .gitignore content
#          .gitignore | 1 insertion(+), 3 deletions(-)
#          1 file changed, 1 insertion(+), 3 deletions(-)

# Push to GitHub
git push origin main
```

## Git History

| Commit   | Date                | Description                                    |
|----------|---------------------|------------------------------------------------|
| `1829645`| 2026-09-22 13:51   | Updated Mentor file                            |
| `4b3a44a`| 2026-09-22 13:49   | Updated .gitignore                             |
| `8b61114`| 2026-09-22 13:40   | Added README documentation                     |
| `a7cf5a6`| 2026-09-22 13:34   | fixed the erros in python files                |
| `e0da61d`| 2026-09-22 13:19   | Added student dashboard access information     |
| `c1fd660`| 2026-09-22 13:14   | Created base user class                        |
| `7c7eece`| 2026-09-22 13:53   | Update README with complete operations and git history |

## Final Status

- All files are committed and pushed to remote repository
- Working tree is clean
- Code executes successfully with expected output
- Repository URL: https://github.com/rajgenai4u/Python_Git_Project
