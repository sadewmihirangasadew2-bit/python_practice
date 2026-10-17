tasks = []

while True :

    print("=== To do list manager ====")

    print("1.enter a task")

    print("2.view a task")

    print("3.delete a task")

    print("4.Exit")

    choice = input("Enter your choice :")

    if choice == "1":

        task = input("enter your task :")
        tasks.append(task)

    if choice == "2":

        print(tasks)

    if choice == "3":

        if len(tasks) == 0:
            print("there are no tasks to delete")

        else:
            print(tasks)
            delete = int(input("enter the task number you wish to delete :"))

            if delete >= 1 and delete <= len(tasks):
                tasks.pop(delete - 1)
                print("tasks deleted")
            else:
                print("invalid task number")
        
    if choice == "4":

        print("goodbye!")
        break
        
