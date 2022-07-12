
'''
string = input()
counter = 0
for i in string:
    if i in '(':
        counter +=1
    elif i in ')':
        counter -=1
        if counter <0:
            print('string is invalid')
            break
if counter ==0:
    print('string is valid')
else:
    print('string is invalid')
'''



'''
#using counter
def is_balanced(input_string):

    counter = 0
    for i in input_string:
        if i =='(':
            counter +=1
        elif i==')':
            counter -=1
            if counter <0:
                return False
    return counter==0

input_string = input()
print(is_balanced(input_string))
'''

'''
#using stack

def bal(input_string):
    stack = []
    for i in input_string:
        if i=='(':
            stack.append('(')
        else:
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                return False
    return len(stack)==0

input_string = input()
print(bal(input_string))
'''

def is_bal(input_string):
    '''
    d = {'(':')','[':']','{':'}'}
    stack = []
    for i in input_string:
        if i in '([{':
            stack.append(i)
        elif i in ')}]':
            if len(stack)==0:
                return False

            o = stack.pop()
            if d[o]!=i:
                return False
    return len(stack)==0
    '''
    stack = []
    for c in input_string:
        if c in '({[':
            print(')}]'['({['.index(c)])
            stack.append(')}]'['({['.index(c)])
            print(stack)
        elif stack and stack[-1] == c:
            stack.pop()
        else:
            return False
    return len(stack) == 0
input_string = input()
print(is_bal(input_string))









