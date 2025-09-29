#EH 1st lists notes
import random
bruh = ["elijah", "urmom", "larose", "dirky the turkey", "urdad", False, 3.14, 1123]

print(bruh[5])
print(random.choice(bruh,))
print(f"the list is {len(bruh)} characters long")
print(bruh)
bruh[0] = "eric"
bruh[1:3] = ["bruh", "okay"]
bruh.pop()
bruh.pop(3)
bruh.remove(3.14)
#bruh.clear()
#bruh.append("andrew")
bruh.insert(1, 3.14)
bruh.extend([3.141592653589793238634626])
print(bruh)

chunky_peanut_butter_with_extra_peanuts_board = [[1,2,3],
                                                [4,5,6],
                                                [7,8,9]

                                                        ]

veggies = {"spinach", "kale", "bruh", "carrot"}