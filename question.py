def text (str):
  words_list = str.split()
  output = []
  outputStr = ''
  for i, word in enumerate(words_list):
    outputStr += word 
    outputStr += " "
    
    if len(outputStr) > 140:
      output.append(outputStr)
      outputStr = " " 
    if len(outputStr) < 140 and i == len(words_list):
      print(i)
      output.append(outputStr)
  return output


print(text('It is a long established fact that a reader will be distracted. Hey It is a long established fact that a reader will be distracted, hey It is a long established fact that a reader will be distracted, hey th It is a long established fact that a reader will be distracted, hey end'))

  # for i in range(0, len(str), 140):
  #   output.append(str[i:i+140])
  #   print('the 140th char', str[i+140])
  # print(words_list)
  # return output