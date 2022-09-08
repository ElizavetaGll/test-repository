# task 1

def greet_user():
    print("ФСПО 'Отделение Связь и телекоммуникации'")
    print("Специальность: Прикладная информатика")
    print("Группа: ДКЕО-41")


def task_1():
    greet_user()


def greet_user_with_args(userDepartment, userProf, userGroup):
    print(f" {userDepartment.title()}")
    print(f" {userProf.title()}")
    print(f" {userGroup.title()}")


def task_2():
    greet_user_with_args('Отделение Связь и телекоммуникации',
                         'Специальность: Прикладная информатика', 'Группа: ДКЕО-41')

    greet_user_with_args(userDepartment='Отделение Связь и телекоммуникации',
                         userProf='Специальность: Прикладная информатика', userGroup='Группа: ДКЕО-41')


def make_shirt(size='L', text="I love Python"):
    print(f"{size} - {text}")


def exercise_1():
    make_shirt('M', 'test')


def exercise_2():
    make_shirt('L')
    make_shirt('XS', 'test 2')


def get_formatted_group_name(department, group, specialization):
    full_name = f"{department} {group} {specialization}"
    return full_name.title()


def exercise_3():
    result = get_formatted_group_name('Связь и телекоммуникации ', 'Прикладная информатика', 'ДКЕО-41')
    print(result)
