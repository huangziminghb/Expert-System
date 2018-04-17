import re
import sys

ifPattern = re.compile("^If")
thenPattern = re.compile("^Then")
parenthesePattern = re.compile("\((.*?)\)")
ruleBase=[]

with open('Rules.txt', 'r') as FileReader:
    lines = FileReader.readlines()

for i in range(0, len(lines)-1):
    matchIf = ifPattern.match(lines[i])
    matchThen = thenPattern.match(lines[i+1])
    if matchIf:
        if matchThen:
            matchCond = parenthesePattern.findall(lines[i])
            matchConc = parenthesePattern.findall(lines[i+1])
            rule1 = (tuple(matchCond), tuple(matchConc))
            ruleBase.append(rule1)

while 1==1:
    cond=input('请输入所需粗糙度（Ra=**）或表面外观（可见刀痕、可见加工痕迹等等），按CTRL+C退出:\n')
    temp=0
    for i in range(0,len(ruleBase)-1):
        theRule=ruleBase[i]
        if cond in theRule[0]:
            print('加工要求为：',theRule[0])
            print('加工方法为：',theRule[1],'\n')
            temp=1
    if 0==temp:
        print('输入的条件不在规则库中！')