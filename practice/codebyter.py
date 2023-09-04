def StringChallenge(strParam):

  # code goes here
  alls= '+${2} 5mmmgggfgg'
  alls1 = '+++++* abcdehhhhhh'
  for i in strParam:
    if strParam not in alls1:
      return True
    return False


# keep this function call here
print(StringChallenge(input()))



def StringChallenge(strParam):

  # code goes here
  alls= '$**+*{2} 5mmmgggfgg'
  for i in strParam:
    if i in alls:
      return True
# keep this function call here
print(StringChallenge(input()))