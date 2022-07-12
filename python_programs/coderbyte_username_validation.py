def CodelandUsernameValidation(strParam):
  if(len(strParam) >4 and len(strParam)<25):
    print(strParam)
    if(strParam[0].isalpha()):
      print("enteretd in to first letter")
      if(strParam[- 1]!='_'):
        print("entered in to last letter")
        return strParam.isdecimal()
  return False 
print(CodelandUsernameValidation(input()))
