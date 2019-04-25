from PreprocessingCodes.interpolation import interpolation
from FeatureExtractionCodes.features import features
from test_code import predictStrokeLabel
import matplotlib.pyplot as plt

def strokeSeg(content):
 strokesList = []
 tempStrokeList = []
 strokeLabelsList = []
# folderPath = r'C:\Users\Sanya\PycharmProjects\Online_Indic_Handwriting_Recognition'
# fileName = input('Enter the file name:')
# path =   fileName

#with open('Krish.txt', 'r', encoding='utf8') as f:
    #content = f.readlines()

# content=44(1).txt
# print(content)
 content = [z.strip().split(',') for z in content]
# print(content)
 for item in content:
    if (item[2] == '0'):
        item[0] = float(item[0])
        item[1] = float(item[1])
        item[2] = float(item[2])
        tempStrokeList.append(item)
    else:
        strokesList.append(tempStrokeList)
        tempStrokeList = []

# print(strokesList[1])
 for stroke in strokesList:
    s = interpolation(stroke)
    final_features = features(s)
    strokeLabel = predictStrokeLabel(final_features)
    #print(strokeLabel)
    strokeLabelsList.append(strokeLabel)

 strokeLabelsList.sort()
#print(strokeLabelsList)
 strLabel = '.'.join(str(e) for e in strokeLabelsList)
 print(strLabel)

 fo = open("hindifinal.txt", "r",encoding="utf8")

 #letter = "पुनः पय।स करें।"
 letter= ["Try"]
 for i in fo:
  i=i.rstrip() #returns each line as string removing the last \n character
  if strLabel == i:
     letter[0] =next(fo)
    # print(next(fo), end='')
     break


 fo.close()

# compareLabel(strokeLabelsList)
# return strokeLabelsList
 #list=[1,2]
 return letter

#print(letter)
