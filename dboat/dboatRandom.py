import itertools
import random
import copy
import math

def calculate_total_torque(left_seats, right_seats):
    left_right_torque = 0
    front_back_torque = 0

    for i in range(10):
        # temporarily left/right logic
        left_right_torque += (left_seats[i] - right_seats[i]) * (1 + math.sqrt((4.5 - abs(i-4.5))))
        front_back_torque += (left_seats[i] + right_seats[i]) * (-4.5 + i)
    
    return (front_back_torque * front_back_torque + left_right_torque * left_right_torque)

def find_optimal_seating(left_weights, right_weights):
    # Initialize variables to store the best solution
    best_seating = None
    min_total_torque = float('inf')

    # Run 30 times for random middle seats
    for i in range(30):
        left_seating_arrangement = [0] * 10
        right_seating_arrangement = [0] * 10
        # Select random weights for seats 4-7 for both left and right

        count = 0

        templeft = copy.deepcopy(left_weights)
        tempright = copy.deepcopy(right_weights)

        for j in range(3,7):

            leftrand = random.randint(0, 9-count)
            left_seating_arrangement[j] = templeft[leftrand]
            del templeft[leftrand]

            rightrand = random.randint(0, 9-count)
            right_seating_arrangement[j] = tempright[rightrand]
            del tempright[rightrand]
            count += 1
        
        # Get two 6! long lists of the left and right possible remaining seat orders
        all_left_nonrand = list(itertools.permutations(range(len(templeft))))
        all_right_nonrand = list(itertools.permutations(range(len(tempright))))

        # Iterate through all seating arrangements
        for left_permutation in all_left_nonrand:
            permut_left_seating = copy.deepcopy(left_seating_arrangement)
            for k in range(0, 3):
                permut_left_seating[k] = templeft[left_permutation[k]]
            for k in range(3, 6):
                permut_left_seating[k+4] = templeft[left_permutation[k]]
                for right_permutation in all_right_nonrand:
                    permut_right_seating = copy.deepcopy(right_seating_arrangement)
                    for l in range(0, 3):
                        permut_right_seating[l] = tempright[right_permutation[l]]
                    for l in range(3, 6):
                        permut_right_seating[l+4] = tempright[right_permutation[l]]
                    # total_torque = calculate_total_torque(left_seating_arrangement, right_seating_arrangement, left_weights, right_weights)
                    total_torque = calculate_total_torque(permut_left_seating, permut_right_seating)
                    # Update the best solution if the current arrangement is better
                    if total_torque < min_total_torque:
                        min_total_torque = total_torque
                        best_seating = [permut_left_seating, permut_right_seating]
        print(best_seating)
        print(calculate_total_torque(best_seating[0], best_seating[1]))
    return best_seating


def main():
    # weights of paddlers, first array left paddlers, second array right paddlers
    paddler_weights = [[70, 75, 80, 180, 90, 98, 101.23, 125.4, 112, 113.7],[50, 60, 80, 110, 120, 54, 58, 80, 110, 140]]

    # Find the optimal seating arrangement
    optimal_seating = find_optimal_seating(paddler_weights[0], paddler_weights[1])

    print("Optimal Seating Arrangement:", optimal_seating)
    print("Total Torque:", calculate_total_torque(optimal_seating[0], optimal_seating[1]))

if __name__ == "__main__":
    main()