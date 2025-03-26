import random


class Serializer:
    ''' Interface for serializing data and save/loading the data '''
    def serialize(self):
        pass
    def deserialize(self, bits):
        pass
    def save(self, filename):
        pass
    def load(self, filename):
        pass


class Student(Serializer):
    def __init__(self) -> None:
        self.semesters = []
    def generate_semesters(self, semesters=0, classes=None):
        ''' Generates a random amount of semesters (max 8) and a random amount of classes (max 5) for each semester'''
        self.semesters = []
        if semesters == 0:
            semesters = random.randint(1,8)
        for i in range(semesters):
            sem = Semester()
            if classes is None:
                c = random.randint(1, 5)
            else:
                c = classes[i]
            sem.generate_grades(c)
            self.semesters.append(sem)
    def avg_grades(self):
        ''' Gets total average of all grades '''
        avgs = []
        for sem in self.semesters:
            avgs.append(sem.avg_grades())
        return sum(avgs)/len(avgs)
    def save(self, filename):
        ''' Saves semesters and grades to binary file '''
        with open(filename, 'wb') as fout:
            bits = self.serialize()
            fout.write(bits)
    def load(self, filename):
        ''' Loads student from binary file '''
        self.semesters = []
        with open(filename, 'rb') as fin:
            while True:
                bits = fin.read(5)
                if len(bits) < 5:
                    break
                sem = Semester()
                sem.deserialize(bits)
                if sem.is_valid():
                    self.semesters.append(sem)
    def serialize(self):
        ''' Converts semesters to bytes. Always returns 40 bytes. '''
        sem_to_save = self.semesters
        bits = bytearray()
        for i in range(len(sem_to_save), 8):
            s = Semester()
            sem_to_save.append(s)
        for sem in self.semesters:
            bit = sem.serialize()
            bits.extend(bit)
        return bits
    def __str__(self):
        s = ''
        for sem in self.semesters:
            s += str(sem)
        return s


class Semester(Serializer):
    def __init__(self) -> None:
        self.grades = []
    def generate_grades(self, classes):
        ''' Generates grades for semester '''
        self.grades = []
        for i in range(classes):
            grade = random.randint(0, 100)
            self.grades.append(grade)
    def avg_grades(self):
        ''' Averages grades from semester '''
        return sum(self.grades)/len(self.grades)
    def is_valid(self):
        ''' Checks if semester has any grades '''
        return len(self.grades) > 0
    def serialize(self):
        ''' Serialize this semester into bytes. Always returns 5 bytes. '''
        grades_to_save = self.grades
        for i in range(len(grades_to_save), 5):
            grades_to_save.append(101)
        return bytearray(grades_to_save)
    def deserialize(self, bits): 
        ''' Deserializes bytes into grades '''
        for bit in bits:
            grade = int(bit)
            if grade <= 100:
                self.grades.append(grade)
    def __str__(self) -> str:
        s = ''
        s += 'Grades: '
        s += str(self.grades)
        s += '\n'
        return s
    

if __name__ == '__main__':
    filename = 'student_grades.dat'
    s = Student()
    s.generate_semesters(4,[5,5,5,5])
    print(s, 'Average: ', s.avg_grades())
    s.save(filename)
    print()
    print(f'Saving to {filename}')
    print()
    s2 = Student()
    s2.load(filename)
    print(f'Loading student from {filename}')
    print()
    print(s2, 'Average: ', s2.avg_grades())
