import random
from datetime import datetime, timedelta

class DataGenerator:
    def __init__(self, num_classrooms=5, num_classes=15):
        self.num_classrooms = num_classrooms
        self.num_classes = num_classes

    def generate_classrooms(self):
        """Generates a list of classrooms with unique IDs and capacities."""
        classrooms = []
        for i in range(1, self.num_classrooms + 1):
            classrooms.append({
                "Classroom_ID": i,
                "Classroom_Name": f"Room {chr(64 + i)}",  # Room A, Room B, etc.
                "Capacity": random.randint(20, 100)  # Random capacity between 20 and 100
            })
        return classrooms

    def generate_classes(self):
        """Generates a list of classes with unique IDs, names, durations, start, and end times."""
        class_names = ["Math", "History", "CS", "Physics", "Art", "Biology", "Chemistry", "English", "Music", "Economics"]
        classes = []
        for i in range(1, self.num_classes + 1):
            name = f"{random.choice(class_names)} {random.randint(100, 400)}"
            duration = random.randint(1, 3)  # Duration between 1 and 3 hours
            start_time, end_time = self.random_time_slot(duration)
            classes.append({
                "Class_ID": i,
                "Class_Name": name,
                "Duration": duration,
                "Start_Time": start_time.strftime("%I:%M %p"),
                "End_Time": end_time.strftime("%I:%M %p")
            })
        return classes

    def random_time_slot(self, duration):
        """Generates a random time slot based on a given duration."""
        # Randomly choose a start time between 8:00 AM and 3:00 PM
        start_hour = random.randint(8, 15 - duration)
        start_time = datetime.strptime(f"{start_hour}:00", "%H:%M")
        end_time = start_time + timedelta(hours=duration)
        return start_time, end_time

    def generate_classroom_timeslots(self):
        """Generates a list of time slots for each classroom."""
        timeslots = []
        for i in range(1, self.num_classrooms + 1):
            num_slots = random.randint(1, 3)
            available_hours = random.sample(range(8, 18), num_slots)
            for hour in sorted(available_hours):
                start_time = datetime.strptime(f"{hour}:00", "%H:%M")
                end_time = start_time + timedelta(hours=random.randint(2, 4))  # Each slot lasts 2-4 hours
                timeslots.append({
                    "Classroom_ID": i,
                    "Available_Start_Time": start_time.strftime("%I:%M %p"),
                    "Available_End_Time": end_time.strftime("%I:%M %p")
                })
        return timeslots

    def generate_datasets(self):
        """Generates datasets for classrooms, classes, and time slots as lists of dictionaries."""
        classrooms = self.generate_classrooms()
        classes = self.generate_classes()
        timeslots = self.generate_classroom_timeslots()
        return classrooms, classes, timeslots


def display_datasets(classrooms, classes, timeslots):
    """Displays the generated datasets for students to see."""
    print("Classrooms:")
    for room in classrooms:
        print(room)

    print("\nClasses:")
    for cls in classes:
        print(cls)

    print("\nTime Slots:")
    for slot in timeslots:
        print(slot)


def is_schedule_valid(schedule, classrooms, classes, timeslots):
    """Checks if the provided schedule is valid."""
    classroom_ids = {room['Classroom_ID'] for room in classrooms}

    # Create a mapping of class start and end times
    class_time_map = {cls['Class_ID']: (cls['Start_Time'], cls['End_Time']) for cls in classes}

    # Check for classroom validity and time conflicts
    for classroom_id, scheduled_classes in schedule.items():
        if classroom_id not in classroom_ids:
            print(f"Error: Classroom ID {classroom_id} not found.")
            return False

        # Check for class time conflicts
        scheduled_times = []
        for class_id in scheduled_classes:
            if class_id not in class_time_map:
                print(f"Error: Class ID {class_id} not found.")
                return False

            # Convert time strings to datetime objects for comparison
            start_time, end_time = class_time_map[class_id]
            start_dt = datetime.strptime(start_time, "%I:%M %p")
            end_dt = datetime.strptime(end_time, "%I:%M %p")

            # Check for conflicts
            for (existing_start, existing_end) in scheduled_times:
                if start_dt < existing_end and end_dt > existing_start:
                    print(f"Conflict detected in Classroom {classroom_id} between classes {class_id} and another class.")
                    return False

            scheduled_times.append((start_dt, end_dt))

    return True


def student_schedule_algorithm(classrooms, classes, timeslots):
    """
    TODO: Implement the scheduling algorithm.
    The function should return a dictionary with Classroom_ID as keys and a list of Class_IDs as values.
    
    Example:
    schedule = {
        1: [101, 102],  # Classroom 1 has classes 101 and 102
        2: [103],       # Classroom 2 has class 103
        3: [104, 105]   # Classroom 3 has classes 104 and 105
    }
    """
    # Placeholder implementation — students need to complete this
    return {}


def test_schedule_algorithm():
    """Framework for testing student algorithms."""
    # Generate datasets
    data_gen = DataGenerator(num_classrooms=3, num_classes=10)
    classrooms, classes, timeslots = data_gen.generate_datasets()

    # Display generated datasets for reference
    display_datasets(classrooms, classes, timeslots)

    # Run the student scheduling algorithm
    schedule = student_schedule_algorithm(classrooms, classes, timeslots)
    print(f"\nStudent's Schedule: {schedule}")

    # Validate the student's schedule
    if is_schedule_valid(schedule, classrooms, classes, timeslots):
        print("\nThe schedule is valid and conflict-free!")
    else:
        print("\nThe schedule has conflicts. Please review the implementation.")


# Run the test framework to generate datasets and test the student's function
test_schedule_algorithm()

