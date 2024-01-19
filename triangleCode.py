def decode(message_file):

# Read in text file
    with open(message_file, "r") as f:
        textList = (f.readlines())

# add number and word to 2d list
    text2D = []

    for x in textList:
        text2D.append([int(x.split()[0]), x.split()[1]])
    
# sort list
    sortedList = sorted(text2D, key=lambda item: item[0])

# find correct words using pyramid rules. 
    answerList = []
    pyramidLevel = 1
    i = 0

    while i < len(sortedList):
        answerList.append(sortedList[i][1]) # add word to answer List
        pyramidLevel += 1        # increases pyramid level
        # adds pyramid level to previous index. 
        i = pyramidLevel + i        # this will result in only adding the last item of each level to the answer list. 


    return " ".join(answerList)

#The following code works as follows: 
#It accepts the file name with the parameter message_file. This is used to read in the contents of the text file. It uses the #readlines method to return a list comprised of each line of this text file. 
#Then, this is separated out into a 2D list with the first value of each item being the number (parsed as an integer) and the #second value being the word. 
#This 2D list is then sorted using the number from each pair. 
#Finally, the final list of decoded words is appended to answeList using a while loop, and the answer is joined using spaces and #returned. 

# print(decode("input.txt"))

def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

print(create_staircase([1, 2, 3, 4, 5, 6]))