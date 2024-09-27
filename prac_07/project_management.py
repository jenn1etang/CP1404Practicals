"""
CP1404 -
Estimate time: 1hour
Actual time: 9 hours
"""
from project import Project
import datetime
from operator import itemgetter

OPTION = 'LSDFAU'
MENU = '- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n' \
       '- (A)dd new project\n- (U)pdate project\n- (Q)uit'


def main():
    projects = []
    print(MENU)
    choice = str(input('>>> ')).upper()
    while choice != 'Q':
        try:
            if choice not in OPTION or len(choice) > 1:
                print('Invalid choice')
        except ValueError:
            print('Invalid Value')
        else:
            if choice == 'L':
                filename = str(input('Open the file: '))
                load_project(filename, projects)
            elif choice == 'S':
                filename = str(input('File to save: '))
                save_project(filename, projects)
            elif choice == 'D':
                # Make two list of incomplete projects and completed projects
                incomplete_projects = [project for project in projects if not project.is_complete()]
                completed_projects = [project for project in projects if project.is_complete()]
                # Sort the two lists
                incomplete_projects.sort(key = itemgetter('priority'))
                completed_projects.sort(key = itemgetter('priority'))
                # Present incomplete projects and completed projects
                print("Incomplete projects:")
                for project in incomplete_projects:
                    print(f"  {display_project(project)}")
                print("Completed projects:")
                for project in completed_projects:
                    print(f"  {display_project(project)}")
            elif choice == 'F':
                start_date = input("Show projects that start after date (dd/mm/yy): ")
                date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                projects_after_date = []
                for project in projects:
                    if project.start_date >= date:
                        projects_after_date.append(project)
                projects_after_date.sort(key = itemgetter('start_date'))
                for project in projects_after_date:
                    print(display_project(project))
            elif choice == 'A':
                print("Let's add a new project")
                name = str(input("Name: "))
                start_date = input("Start data (dd/mm/yy): ")
                priority = int(input("Priority: "))
                cost_estimate = float(input("Cost estimate: $"))
                percentage_complete = int(input("Percentage Complete: "))
                date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                new_project = Project(name, date.strftime("%d/%m/%Y"), priority, cost_estimate, percentage_complete)
                projects.append(new_project)
            elif choice == 'U':
                # Present projects with position number
                for count, project in enumerate(projects):
                    print(f"{count} {display_project(project)}")
                project_to_update = int(input("Project choice: "))
                # Present chosen project
                print(display_project(projects[project_to_update]))
                # Get new percentage and new priority
                new_percentage = check_integer_input("New Percentage: ")
                new_priority = check_integer_input("New Priority: ")
                # If new percentage or new priority is blank, it's data retain existing values
                if new_percentage != '' and new_percentage != ' ':
                    projects[project_to_update].completion_percentage = int(new_percentage)
                if new_priority != '' and new_priority != ' ':
                    projects[project_to_update].priority = int(new_priority)
            print(MENU)
            choice = str(input('>>> ')).upper()
    print("Thank you for using custom-built project management software.")


def check_integer_input(data_entered):
    is_valid_input = False
    while not is_valid_input:
        value = str(input(data_entered))
        if value.isdigit() or value == '' or value == ' ':
            return value
        else:
            print("Invalid input, must be number")


def display_project(project):
    return f"{project.name}, start: {project['start_date'].strftime('%d/%m/%Y')}, priority {project.priority}, " \
           f"estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%"


def load_project(filename, projects):
    # read the header
    in_file = open(filename, 'r')
    in_file.readline()
    # read the rest of lines
    for line in in_file:
        parts = line.strip().split('\t')
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()


def save_project(filename, projects):
    out_file = open(filename, 'w')
    for project in projects:
        print(project, file = out_file)
    out_file.close()


main()
