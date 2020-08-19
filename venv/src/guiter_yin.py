import random

pu=['下加三间','下加一间','五线','三线','下加4间','下加一线','四间','下加三线','二间','三间','一线','四线','二线','下加二间','一间','下加二线','上加一间']

qin=['6弦3品','4弦空弦','1弦1品','2弦空弦','6弦空弦','5弦3品','1弦空弦','6弦1品','3弦2品','2弦1品','4弦2品','2弦3品','3弦空弦','5弦2品','4弦3品','5弦空弦','1弦3品']

yin=['低音5','中音2','高音4','中音7','低音3','中音1','高音3','低音4','中音6','高音1','中音3','高音2','中音5','低音7','中音4','低音6','高音5']

yinMapping={'低音5':('下加三间','6弦3品'),'中音2':('下加一间','4弦空弦'),'高音4':('五线','1弦1品'),'中音7':('三线','2弦空弦'),'低音3':('下加4间','6弦空弦'),'中音1':('下加一线','5弦3品'),
            '高音3':('四间','1弦空弦'),'低音4':('下加三线','6弦1品'),'中音6':('二间','3弦2品'),'高音1':('三间','2弦1品'),'中音3':('一线','4弦2品'),'高音2':('四线','2弦3品'),
            '中音5':('二线','3弦空弦'),'低音7':('下加二间','5弦2品'),'中音4':('一间','4弦3品'),'低音6':('下加二线','5弦空弦'),'高音5':('上加一间','1弦3品')}

wrongList=set([])
def printAllPu():
    i=0
    random.shuffle(pu)
    puChoices={}
    print("五线谱:",end=' ')
    for puItem in pu:
        print('('+chr(97+i)+')' + puItem,end=', ')
        puChoices[chr(97+i)]=puItem
        i=i+1
    return puChoices

def printAllQin():
    i=0
    random.shuffle(qin)
    qinChoices={}
    print("吉他:",end=' ')
    for qinItem in qin:
        print('('+chr(97+i)+')' + qinItem,end=', ')
        qinChoices[chr(97+i)]=qinItem
        i=i+1
    return qinChoices


random.shuffle(yin)

for key in yin:
    while True:
        print('#####')
        print(key)
        print('#####')
        puChoices=printAllPu()
        print()
        qinChoices=printAllQin()
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
                print("Correct! Good job!")
                break
            else:
                print("Incorrect answer!")
                wrongList.add(key)


print('Test complete. Pls find wrong list:', wrongList)