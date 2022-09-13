import random
import time

pu=['下加三间','下加一间','五线','三线','下加4间','下加一线','四间','下加三线','二间','三间','一线','四线','二线','下加二间','一间','下加二线','上加一间']

qin=['6弦3品','4弦空弦','1弦1品','2弦空弦','6弦空弦','5弦3品','1弦空弦','6弦1品','3弦2品','2弦1品','4弦2品','2弦3品','3弦空弦','5弦2品','4弦3品','5弦空弦','1弦3品']

yin=['低音so','中音re','高音fa','中音si','低音mi','中音do','高音mi','低音fa','中音la','高音do','中音mi','高音re','中音so','低音si','中音fa','低音la','高音so']


yinMapping={'低音so':('下加三间','6弦3品'),'中音re':('下加一间','4弦空弦'),'高音fa':('五线','1弦1品'),'中音si':('三线','2弦空弦'),'低音mi':('下加4间','6弦空弦'),'中音do':('下加一线','5弦3品'),
            '高音mi':('四间','1弦空弦'),'低音fa':('下加三线','6弦1品'),'中音la':('二间','3弦2品'),'高音do':('三间','2弦1品'),'中音mi':('一线','4弦2品'),'高音re':('四线','2弦3品'),
            '中音so':('二线','3弦空弦'),'低音si':('下加二间','5弦2品'),'中音fa':('一间','4弦3品'),'低音la':('下加二线','5弦空弦'),'高音so':('上加一间','1弦3品')}


wrongList=set([])

def printPuChoices(answer,number):
    random.shuffle(pu)
    puSetTemp=set(pu)
    puSetTemp.remove(answer)
    puSet=list(puSetTemp)[0:number]
    puSet.append(answer)
    random.shuffle(puSet)
    puChoices={}
    print("五线谱:",end=' ')
    i=0
    for puItem in puSet:
        print('('+chr(97+i)+')' + puItem,end=', ')
        puChoices[chr(97+i)]=puItem
        i=i+1
    return puChoices

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

random.shuffle(yin)
m=0
starttime=time.time()
for key in yin:
    m=m+1
    questionstarttime=time.time()
    while True:
        print('#####')
        print('('+str(m)+')', key)
        print('#####')
        puChoices=printPuChoices(yinMapping[key][0],5)
        print()
        qinChoices=printQinChoices(yinMapping[key][1],5)
        print()
        answer=input('Please input your answer(五线谱吉他):')
        if len(answer) != 2:
            print("Incorrect answer!")
            wrongList.add(key)
        else:
            puAnswer=answer[0:1]
            qinAnswer=answer[1:2]
            mapping=yinMapping[key]
            if puChoices.get(puAnswer)==mapping[0] and qinChoices.get(qinAnswer)==mapping[1]:
                questioncompletetime=(time.time()-questionstarttime)//1
                print('Correct! Good job in '+str(questioncompletetime)+' seconds !')
                break
            else:
                print('Incorrect answer!')
                wrongList.add(key)

spenttime=(time.time()-starttime)//1
print('Test complete in '+ str(spenttime) +' seconds, Pls find wrong list:', wrongList)
