#reverse the string

a="testing"

def reverse_string(s):
    return s[::-1]  

print("Reversed string:",reverse_string(a))

# manual method
def reverse_string_manual(s):
    str_r=""
    for ch in a:
        print(ch)
        str_r=ch+str_r
    return str_r

print("Reversed string (manual method):",reverse_string_manual(a))