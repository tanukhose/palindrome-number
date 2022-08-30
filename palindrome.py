# def ifPalindrome(string):
#     if string == "":  # BASE CASE CONDITION
#         return True
#     elif len(string) == 1:  # BASE CASE CONDITION
#         return True
#     elif string[0] == string[len(string)-1]:  # RECURSION
#         return ifPalindrome(string[1:][:-1])
#     else:
#         return False
# a=ifPalindrome("nitin")
# print(a)

# name=['n','i','t','i','n']
# i=0
# b=''
# a=''
# while i<len(name):
#     b+=name[i]
#     i=i+1
# i=1
# while i<=len(name):
#     a+=name[-i]
#     i=i+1
# print(a)    
# if b==a:
#     print(a,"palindrome")
# else:
#     print("not palindrome")


a=["nitin","tanu","12321"]
i=0
while i<len(a):
    j=0
    b=''
    c=''
    while j<len(a[i]):
        b+=a[i][j]
        j+=1
    # print(b)
    j=1
    while j<=len(a[i]):
        c+=a[i][-j]
        j+=1
    # print(c)
    i+=1
    if b==c:
        print(b,"palindrome")
    else:
        print(b,"not")

  


def fa(a):
    if a==1:
        return 1
    return a*fa(a-1)
print(fa(5))




def pal(a):
    b=a[::-1]
    v=a
    if b==v:
        return 'PAL'
    else:
        return 'NOT'
u=input("enter the:-")
print(pal(u))


