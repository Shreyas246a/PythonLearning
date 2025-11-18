# List for slicing examples

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("Original List:", nums) #[10, 20, 30, 40, 50, 60, 70, 80, 90]

print("\n1. Slicing the middle portion (index 3 to 6)")
print(nums[3:7]) #40, 50, 60, 70

print("\n2. Last 5 elements using negative index")
print(nums[-5:]) #50, 60, 70, 80, 90

print("\n3. All except first and last")
print(nums[1:-1]) #20, 30, 40, 50, 60, 70, 80

print("\n4. Every 2nd number")
print(nums[::2]) #10, 30 , 50, 70, 90

print("\n5. Every 3rd number starting from index 2")
print(nums[2::3]) #30, 60, 90

print("\n6. Reverse the entire list")
print(nums[::-1]) 

print("\n7. Reverse a portion (index 7 to 2)")
print(nums[7:1:-1]) #20,30, 40, 50, 60, 70, 80

print("\n8. Negative step (skip backward every 2)")
print(nums[8:2:-2])#90, 70, 50

print("\n9. First 4 items but skip every 2nd")
print(nums[:4:2]) #10, 30

print("\n10. Middle items with step of 2 (index 2 to 7)")
print(nums[2:8:2]) #30, 50 , 70

# Real-world examples

students = ["Asha", "Bharath", "Chandu", "Divya", "Gamana", "Harsha"]
print("\n11. Even-indexed students")
print(students[::2]) #ASHA, CHANDU, gAMANA

name = "KODNESTTRAINING"
print("\n12. Last 5 characters of a string")
print(name[-5:]) #iNING

word = "Python"
print("\n13. Reverse a string")
print(word[::-1]) #NOTHOP

msg = "HELLO WORLD"
print("\n14. Alternate characters in a string")
print(msg[::2]) #HLOWRD

date = "2025-11-17"
print("\n15. Extract year from a date string")
print(date[:4]) #2025