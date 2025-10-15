import sqlite3

db = sqlite3.connect('app.db')
cr = db.cursor()
cr.execute("Create Table if not exists Skills(name text , progress text , user_id text)")


def commit_and_close():
    db.commit()
    db.close()
    print('Database Is Closed...')
    print('#'*50)


def show_skills():
    print('#' * 50)
    user_id = input('Enter Your ID Please: ').strip()
    cr.execute(f"select * from skills where user_id = '{user_id}'")
    skills = cr.fetchall()
    print(f'You Have {len(skills)} Skill\\s')
    for skill in skills:
        print(f'Skill Name => {skill[0]} , Skill Progress => {skill[1]}%')
    commit_and_close()

def add_skill():
    print('#' * 50)
    user_id = input('Enter Your ID Please: ').strip()
    skill_name = input('Enter Skill Name Please: ').strip().capitalize()

    cr.execute(
        f"select name from skills where name = '{skill_name}' and  user_id = '{user_id}'")
    skill = cr.fetchone()

    if skill == None:
        skill_progress = input('Enter Skill Progress Please: ').strip()
        cr.execute(
            f"insert into skills(name,progress,user_id) values('{skill_name}','{skill_progress}','{user_id}')")
        print('Skill Added...')
    else:
        print('You Can\'t Add It.')
        choice = input('Do You Want To Update It (y/n)? ').strip().lower()
        if choice == 'y':
            new_progress = input('Enter New Progress Please: ').strip()
            cr.execute(
                f"update skills set progress ='{new_progress}' where name ='{skill_name}' and user_id = '{user_id}'")
            print('Skill Progress Updated...')

        else:
            print('See You Later.')

    commit_and_close()

def delete_skill():
    print('#' * 50)
    user_id = input('Enter Your ID Please: ').strip()
    skill_name = input('Enter Skill Name Please: ').strip().capitalize()

    skills_list = []
    cr.execute(f"select name from skills where user_id = '{user_id}'")
    skills = cr.fetchall()

    for skill in skills :
        skills_list.append(skill[0])

    if skill_name in skills_list:
        cr.execute(f"delete from skills where name = '{skill_name}' and user_id = '{user_id}'")
        print('Skill Deleted...')
    else:
        print('This Skill Already Deleted.')

    commit_and_close()

def update_skill_progress():
    print('#' * 50)
    user_id = input('Enter Your ID Please: ').strip()
    skill_name = input('Enter Skill Name Please: ').strip().capitalize()
    new_progress = input('Enter New Progress Please: ').strip()
    cr.execute(f"update skills set progress ='{new_progress}' where name ='{skill_name}' and user_id = '{user_id}'")
    print('Skill Progress Updated...')
    commit_and_close()



input_message = """
What Do You Want?
s => Show All Skills
a => Add New Skill
d => Delete Skill
u => Update Skill Progress
q => Quit Application
    : """

user_input = input(input_message).strip().lower()
commands_list = ['s' ,'a' ,'d' ,'u' ,'q']


if user_input in commands_list:

    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skill()
    elif user_input == "d":
        delete_skill()
    elif user_input == "u":
        update_skill_progress()
    else:
        print("Quit Application")
        commit_and_close()

        
else:
    print(f'Sorry Command {user_input} Doesn\'t Exists..')
