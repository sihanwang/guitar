import random
import time

pu=['下加三间','下加一间','五线','三线','下加4间','下加一线','四间','下加三线','二间','三间','一线','四线','二线','下加二间','一间','下加二线','上加一间']

qin=['6弦3品','4弦空弦','1弦1品','2弦空弦','6弦空弦','5弦3品','1弦空弦','6弦1品','3弦2品','2弦1品','4弦2品','2弦3品','3弦空弦','5弦2品','4弦3品','5弦空弦','1弦3品']

yin=['低音so','中音re','中音fa','中音si','低音mi','中音do','高音mi','低音fa','中音la','高音do','中音mi','高音re','中音so','低音si','低音la','高音fa','高音so']


puMapping={'下加三间':('低音so','6弦3品'),'下加一间':('中音re','4弦空弦'),'五线':('高音fa','1弦1品'),'三线':('中音si','2弦空弦'),'下加4间':('低音mi','6弦空弦'),'下加一线':('中音do','5弦3品'),
            '四间':('高音mi','1弦空弦'),'下加三线':('低音fa','6弦1品'),'二间':('中音la','3弦2品'),'三间':('高音do','2弦1品'),'一线':('中音mi','4弦2品'),'四线':('高音re','2弦3品'),
            '二线':('中音so','3弦空弦'),'下加二间':('低音si','5弦2品'),'一间':('中音fa','4弦3品'),'下加二线':('低音la','5弦空弦'),'上加一间':('高音so','1弦3品')}


wrongList=set([])
def printYinChoices(answer,number):
    random.shuffle(yin)
    yinSetTemp=set(yin)
    yinSetTemp.remove(answer)
    yinSet=list(yinSetTemp)[0:number]
    yinSet.append(answer)
    random.shuffle(yinSet)
    yinChoices={}
    print("五线谱:",end=' ')
    i=0
    for yinItem in yinSet:
        print('('+chr(97+i)+')' + yinItem,end=', ')
        yinChoices[chr(97+i)]=yinItem
        i=i+1
    return yinChoices

def printQinChoices(answer,number):
    random.shuffle(qin)
    qinSetTemp=set(qin)
    qinSetTemp.remove(answer)
    qinSet=list(qinSetTemp)[0:number]
    qinSet.append(answer)
    random.shuffle(qinSet)
    qinChoices={}
    print("吉他:",end=' ')
    i=0
    for qinItem in qinSet:
        print('('+chr(97+i)+')' + qinItem,end=', ')
        qinChoices[chr(97+i)]=qinItem
        i=i+1
    return qinChoices

random.shuffle(pu)
m=0
starttime=time.time()
for key in pu:
    m=m+1
    questionstarttime=time.time()
    while True:
        print('#####')
        print('('+str(m)+')', key)
        print('#####')
        yinChoices=printYinChoices(puMapping[key][0],5)
        print()
        qinChoices=printQinChoices(puMapping[key][1],5)
        print()
        answer=input('Please input your answer(音吉他):')
        if len(answer) != 2:
            print("Incorrect answer!")
            wrongList.add(key)
        else:
            yinAnswer=answer[0:1]
            qinAnswer=answer[1:2]
            mapping=puMapping[key]
            if yinChoices.get(yinAnswer)==mapping[0] and qinChoices.get(qinAnswer)==mapping[1]:
                questioncompletetime=(time.time()-questionstarttime)//1
                print('Correct! Good job in '+str(questioncompletetime)+' seconds !')
                break
            else:
                print('Incorrect answer!')
                wrongList.add(key)

spenttime=(time.time()-starttime)//1
print('Test complete in '+ str(spenttime) +' seconds, Pls find wrong list:', wrongList)
