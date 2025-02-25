#! /usr/bin/env python3

# def main():
#     callouts = int(input())
#     nameORcallout = []
#     for i in range(callouts):
#         nameORcallout.append(input())

#     presentStudents = []
#     for i in range(len(nameORcallout)-1):
#         if nameORcallout[i+1] == "Present!":
#             presentStudents.append(nameORcallout[i])
#         else:
#             None

#     difference = list(set(nameORcallout).difference(presentStudents))
#     difference = [x for x in difference if x != "Present!"]
#     sortedDiff = sorted(difference)

#     if len(sortedDiff) == 0:
#         print("No Absences")
#     else:
#         for i in range(len(sortedDiff)):
#             print(sortedDiff[i])

# if __name__ == "__main__":
#     main()


def main():
    callouts = int(input())
    nameORcallout = [input() for _ in range(callouts)]
    
    presentStudents = [nameORcallout[i] for i in range(len(nameORcallout)-1) if nameORcallout[i+1] == "Present!"]
    
    sortedDiff = sorted(set(nameORcallout) - set(presentStudents) - {"Present!"})
    
    if sortedDiff:
        print(*sortedDiff, sep='\n')
    else:
        print("No Absences")

if __name__ == "__main__":
    main()
