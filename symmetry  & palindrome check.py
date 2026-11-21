# 13.symmetrical or palindrome 
def check_string(s):
 n = len(s)

    #symmetrical check
 if n % 2 == 0:
        first_half = s[:n//2]
        second_half = s[:n//2:]
 else:
        first_half = s[:n//2]
        second_half = s[:n//2+1:]

 if first_half == second_half:
        print("symmetical")
 else:
        print("Not symmetrical")

# palindrome check
 if s == s[::-1]:
    print("palindrome")
 else:
    print("Not palindrome")

#Test 
check_string("madam")
check_string("abbbaabbba")

# palindrom : read the same forwad and backward. 
# eg : "level","121".

#symmetrical string : first half repeat the second half in  same order 
#eg : "yoyo","abab".