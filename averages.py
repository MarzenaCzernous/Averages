def find_the_best_average(filename):
    
    classes_grades = {}

    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.split(';')
            grades = [float(line[n]) for n in range(3,9)]
            if line[2] in classes_grades:    # line[2] is name of the class in each line
                classes_grades[line[2]].extend(grades)
            else:
                classes_grades[line[2]] = grades

    best_class = ''
    best_average = 0   
    for class_name in classes_grades:
        average = sum(classes_grades[class_name])/len(classes_grades[class_name])
        if average > best_average:
            best_average = average
            best_class = class_name
    return f'Class {best_class} with the best average of grades: {best_average}'

print(find_the_best_average('grades.txt'))



        


