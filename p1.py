#1
def palindrome ():
    yield "m"
    yield "a"
    yield "d"
    yield "a"
    yield "m"

itr= palindrome()
for i in palindrome():
    print(i)
print("palindrome done")


#2
def reverseString(text):
    index = -1


# Loop from last index until half of the index
    for i in range(len(text) - 1, int(len(text) / 2), -1):
       if text[i].isalpha():
          temp = text[i]
          while True:
            index += 1
            if text[index].isalpha():
                text[i] = text[index]
                text[index] = temp
                break
    return text


        # Driver code
string = "ab@#cd!ef"
print("Input string: ", string)
string = reverseString(list(string))
print("Output string: ", "".join(string))

#3
lst = ["a","b","n","a","b","c","d","b","c","d","o","p"]
d={}
for items in lst:
    if items in d:
        d[items]+=1

    else:
        d[items]=1
for key,value in d.items():
    print(f"{key}: {value}")


#4

    import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)


#5
def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList


lis = [1,2,[3,4,[5,6]],7,8,[9,10]]
print('List', lis)


#6

def sum (x,y):
    return int(x)+int(y)
x=list(str(input("enter no")))
y=list(str(input("enter no")))

z=list(map(sum,x,y))
temp=0
for i in z:
    temp=temp+i

print("output",temp)


