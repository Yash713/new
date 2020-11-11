def isCorrect(s):
    stack=[]
    bracket={'{':'}','(':')','[':']'}

    for char in s:
             if char in ['{','(','[']:
                 stack.append(char)
             else:
                 if stack:
                     top=stack.pop()
                     if bracket[top] != char:
                         return 'False'
                 else:
                    return 'False'
    return "False" if stack else "True"
