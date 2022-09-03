"""
Nested Lists

Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""




if __name__ == '__main__':
    records = []
    names = []
    scores = []
    lowests2 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        names.append(name)
        scores.append(score)
    
    scor_uniq = list(set(scores))
    scor_uniq.sort()
    
    while True:
        try:
            lowests2.append(names[scores.index(scor_uniq[1])])
            del names[scores.index(scor_uniq[1])]
            scores.remove(scor_uniq[1])
        except:
            lowests2.sort()
            for i in lowests2:
                print(i)
            break
    
            
    # Without sets nor sort():
    """
    lowest = min(scores)
    del names[scores.index(lowest)]
    scores.remove(lowest)
    
    lowest_2 = min(scores)
    while lowest_2 == lowest:
        del names[scores.index(lowest_2)]
        scores.remove(lowest_2)
        lowest_2 = min(scores)
    
    #
    lowest2 = min(scores)
    lowests2.append(names[scores.index(lowest2)])
    del names[scores.index(lowest2)]
    scores.remove(lowest2)
    
    lowest2_2 = min(scores)
    while lowest2_2 == lowest2:
        lowests2.append(names[scores.index(lowest2_2)])
        del names[scores.index(lowest2_2)]
        scores.remove(lowest2_2)
        lowest2_2 = min(scores)
        
    lowests2.sort()
    
    for i in lowests2:
        print(i)
    """
