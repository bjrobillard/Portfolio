import math

def ladder_length(building_height, ladder_angle):
    # Convert angle from degrees to radians
    angle_radians = math.radians(ladder_angle)
    
    # Calculate the length of the ladder using trigonometry
    ladder_length = building_height / math.sin(angle_radians)
    
    # Round the result up to the nearest integer
    ladder_length = math.ceil(ladder_length)
    
    return ladder_length


def main():
    building_height, ladder_angle = input().split()  # Height of the building in meters

    length = ladder_length(int(building_height), int(ladder_angle))
    print(round(length))

if __name__ == "__main__":
    main()
