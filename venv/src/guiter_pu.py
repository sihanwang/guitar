import random

pu=['下加三间','下加一间','五线','三线','下加4间','下加一线','四间','下加三线','二间','三间','一线','四线','二线','下加二间','一间','下加二线','上加一间']

qin=['6弦3品','4弦空弦','1弦1品','2弦空弦','6弦空弦','5弦3品','1弦空弦','6弦1品','3弦2品','2弦1品','4弦2品','2弦3品','3弦空弦','5弦2品','4弦3品','5弦空弦','1弦3品']

yin=['低音5','中音2','高音4','中音7','低音3','中音1','高音3','低音4','中音6','高音1','中音3','高音2','中音5','低音7','中音4','低音6','高音5']

puMapping={'下加三间':('低音5','6弦3品'),'下加一间':('中音2','4弦空弦'),'五线':('高音4','1弦1品'),'三线':('中音7','2弦空弦'),'下加4间':('低音3','6弦空弦'),'下加一线':('中音1','5弦3品'),
            '四间':('高音3','1弦空弦'),'下加三线':('低音4','6弦1品'),'二间':('中音6','3弦2品'),'三间':('高音1','2弦1品'),'一线':('中音3','4弦2品'),'四线':('高音2','2弦3品'),
            '二线':('中音5','3弦空弦'),'下加二间':('低音7','5弦2品'),'一间':('中音4','4弦3品'),'下加二线':('低音6','5弦空弦'),'上加一间':('高音5','1弦3品')}


wrongList=set([])
def printAllYin():
    i=0
    random.shuffle(yin)
    yinChoices={}
    print("音:",end=' ')
    for yinItem in yin:
        print('('+chr(97+i)+')' + yinItem,end=', ')
        yinChoices[chr(97+i)]=yinItem
        i=i+1
    return yinChoices

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


random.shuffle(pu)

for key in pu:
    while True:
        print('#####')
        print(key)
        print('#####')
        yinChoices=printAllYin()
        print()
        qinChoices=printAllQin()
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
                print("Correct! Good job!")
                break
            else:
                print("Incorrect answer!")
                wrongList.add(key)


print('Test complete. Pls find wrong list:', wrongList)