A simple Python program to manage skills using SQLite — allows users to add, update, delete, and view their skills.

# 🧠 Skills Manager (SQLite & Python)

##  Description
A simple Python program to manage skills using SQLite.  
It allows users to add, update, delete, and view their skills through a command-line interface.

---

##  Technologies Used
-  Python  
-  SQLite (Built-in Database)

---

##  Features
- Add new skills for a specific user.  
- View all saved skills with their progress.  
- Update progress of an existing skill.  
- Delete skills easily.  
- Prevent adding duplicate skills for the same user.

---

##  How to Run
1. Make sure Python is installed on your system.  
2. Download or clone the project to your local machine.  
3. Run the script:
   ```bash
   python main.py
---
## Follow the menu options:
- `s` → Show all skills  
- `a` → Add a new skill  
- `u` → Update skill progress  
- `d` → Delete a skill  
- `q` → Quit the application

---
## Database Info
- **Database file:** `app.db`  
- **Table:** `skills`  
- **Fields:**  
  - `name` → Text (Skill name)  
  - `progress` → Text (Skill progress in %)  
  - `user_id` → Text (User identifier)

---
## Example Output
```What Do You Want?
-s => Show All Skills
-a => Add New Skill
-d => Delete Skill
-u => Update Skill Progress
-q => Quit Application
: s

You Have 2 Skill\s
-Skill Name => Python , Skill Progress => 90%
-Skill Name => Arduino , Skill Progress => 70%
```
---
🧑‍💻 Author
Developed by Abdelaziz 
