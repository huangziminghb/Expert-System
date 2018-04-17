import re
#第一级
Rule1_cond="if(Ra=50)and(明显可见刀痕)"
Rule1_conc="then(方法：铸造、锻压、粗车、粗铣、醋刨、钻孔)and(属性：粗加工面)and(适用范围：一般不常用)"

Rule2_cond="if(Ra=25)and(可见刀痕)"
Rule2_conc="then(方法：铸造、锻压、粗车、粗铣、醋刨、钻孔)and(属性：粗加工面)and(适用范围：钻孔表面、倒角、端面、沉孔、要求较低的非接触面)"

Rule3_cond="if(Ra=12.5)and(微可见刀痕)"
Rule3_conc="then(方法：铸造、锻压、粗车、粗铣、醋刨、钻孔)and(属性：粗加工面)and(适用范围：钻孔表面、倒角、端面、沉孔、要求较低的非接触面)"


#第二级
Rule4_cond="if(Ra=6.3)and(可见加工痕迹)"
Rule4_conc="then(方法：精车、精铣、精刨、精镗、铰孔、粗磨)and(属性：半精加工面)and(适用范围：要求较低的静止接触面)"

Rule5_cond="if(Ra=3.2)and(微见加工痕迹)"
Rule5_conc="then(方法：精车、精铣、精刨、精镗、铰孔、粗磨)and(属性：半精加工面)and(适用范围：要求紧贴的静止接触面以及较低配合面)"

Rule6_cond="if(Ra=1.6)and(看不见加工痕迹)"
Rule6_conc="then(方法：精车、精铣、精刨、精镗、铰孔、粗磨)and(属性：半精加工面)and(适用范围：有相对运动的零件接触面)"


#第三级
Rule7_cond="if(Ra=0.8)and(可辨加工痕迹方向)"
Rule7_conc="then(方法：精磨、抛光、金刚石车、精铰、精拉)and(属性：粗加工面)and(适用范围：要求很好密合的、相对运动速度较高的接触面，如滑动导轨面、高速工作的滑动轴承)"

Rule8_cond="if(Ra=0.4)and(微辨加工痕迹方向)"
Rule8_conc="then(方法：粗加工面、精磨、抛光、金刚石车、精铰、精拉)and(属性：粗加工面)and(适用范围：要求很好密合的、相对运动速度较高的接触面，如滑动导轨面、高速工作的滑动轴承)"

Rule9_cond="if(Ra=0.2)and(不可辨加工痕迹方向)"
Rule9_conc="then(方法：精磨、抛光、金刚石车、精铰、精拉)and(属性：粗加工面)and(适用范围：要求很好密合的、相对运动速度较高的接触面，如滑动导轨面、高速工作的滑动轴承)"


#第四级
Rule10_cond="if(Ra=0.1)and(暗光泽面)"
Rule10_conc="then(方法：精磨、抛光、研磨)and(属性：光加工面)and(适用范围：精密量具的表面，极重要零件的摩擦面，如气缸的内表面、精密机床的主轴颈、坐标镗床的主轴颈等)"

Rule11_cond="if(Ra=0.05)and(亮光泽面)"
Rule11_conc="then(方法：精磨、抛光、研磨)and(属性：光加工面)and(适用范围：精密量具的表面，极重要零件的摩擦面，如气缸的内表面、精密机床的主轴颈、坐标镗床的主轴颈等)"

Rule12_cond="if(Ra=0.025)and(镜状光泽面)"
Rule12_conc="then(方法：精磨、抛光、研磨)and(属性：光加工面)and(适用范围：精密量具的表面，极重要零件的摩擦面，如气缸的内表面、精密机床的主轴颈、坐标镗床的主轴颈等)"

Rule13_cond="if(Ra=0.012)and(雾状光泽面)"
Rule13_conc="then(方法：精磨、抛光、研磨)and(属性：光加工面)and(适用范围：精密量具的表面，极重要零件的摩擦面，如气缸的内表面、精密机床的主轴颈、坐标镗床的主轴颈等)"

Rule14_cond="if(Ra=0.006)and(镜面)"
Rule14_conc="then(方法：精磨、抛光、研磨)and(属性：光加工面)and(适用范围：精密量具的表面，极重要零件的摩擦面，如气缸的内表面、精密机床的主轴颈、坐标镗床的主轴颈等)"







ifPattern=re.compile("^if")
thenPattern=re.compile("^then")

parenthesePattern=re.compile("\((.*?)\)")

############Rule1#################
print("\n")
print("Rule1:")
matchif1=ifPattern.match(Rule1_cond)      
if matchif1:
        print("match if succeed")
        matchcond1=parenthesePattern.findall(Rule1_cond)
        if matchcond1:
            print("match condition succeed")
            print(matchcond1)
            
matchthen1=thenPattern.match(Rule1_conc)
if matchthen1:
        print("match then succeed")
        matchconc1=parenthesePattern.findall(Rule1_conc)
        if matchconc1:
            print("match chonclusion succeed")
            print(matchconc1)

rule1=(tuple(matchcond1),tuple(matchconc1))
print(rule1)

############Rule2#################
print("\n")
print("Rule2:")
matchif2=ifPattern.match(Rule2_cond)    
if matchif2:
        print("match if succeed")
        matchcond2=parenthesePattern.findall(Rule2_cond)
        if matchcond2:
            print("match condition succeed")
            print(matchcond2)
            
matchthen2=thenPattern.match(Rule2_conc)
if matchthen2:
        print("match then succeed")
        matchconc2=parenthesePattern.findall(Rule2_conc)
        if matchconc2:
            print("match chonclusion succeed")
            print(matchconc2)

rule2=(tuple(matchcond2),tuple(matchconc2))
print(rule2)


############Rule3#################
print("\n")
print("Rule3:")
matchif3=ifPattern.match(Rule3_cond)    
if matchif3:
        print("match if succeed")
        matchcond3=parenthesePattern.findall(Rule3_cond)
        if matchcond3:
            print("match condition succeed")
            print(matchcond3)
            
matchthen3=thenPattern.match(Rule3_conc)
if matchthen3:
        print("match then succeed")
        matchconc3=parenthesePattern.findall(Rule3_conc)
        if matchconc3:
            print("match chonclusion succeed")
            print(matchconc3)

rule3=(tuple(matchcond3),tuple(matchconc3))
print(rule3)



############Rule4#################
print("\n")
print("Rule4:")
matchif4=ifPattern.match(Rule4_cond)    
if matchif4:
        print("match if succeed")
        matchcond4=parenthesePattern.findall(Rule4_cond)
        if matchcond4:
            print("match condition succeed")
            print(matchcond4)
            
matchthen4=thenPattern.match(Rule4_conc)
if matchthen4:
        print("match then succeed")
        matchconc4=parenthesePattern.findall(Rule4_conc)
        if matchconc4:
            print("match chonclusion succeed")
            print(matchconc4)

rule4=(tuple(matchcond4),tuple(matchconc4))
print(rule4)


############Rule5#################
print("\n")
print("Rule5:")
matchif5=ifPattern.match(Rule5_cond)    
if matchif5:
        print("match if succeed")
        matchcond5=parenthesePattern.findall(Rule5_cond)
        if matchcond5:
            print("match condition succeed")
            print(matchcond5)
            
matchthen5=thenPattern.match(Rule5_conc)
if matchthen5:
        print("match then succeed")
        matchconc5=parenthesePattern.findall(Rule5_conc)
        if matchconc5:
            print("match chonclusion succeed")
            print(matchconc5)

rule5=(tuple(matchcond5),tuple(matchconc5))
print(rule5)


############Rule6#################
print("\n")
print("Rule6:")
matchif6=ifPattern.match(Rule6_cond)    
if matchif6:
        print("match if succeed")
        matchcond6=parenthesePattern.findall(Rule6_cond)
        if matchcond6:
            print("match condition succeed")
            print(matchcond6)
            
matchthen6=thenPattern.match(Rule6_conc)
if matchthen6:
        print("match then succeed")
        matchconc6=parenthesePattern.findall(Rule6_conc)
        if matchconc6:
            print("match chonclusion succeed")
            print(matchconc6)

rule6=(tuple(matchcond6),tuple(matchconc6))
print(rule6)




############Rule7#################
print("\n")
print("Rule7:")
matchif7=ifPattern.match(Rule7_cond)    
if matchif7:
        print("match if succeed")
        matchcond7=parenthesePattern.findall(Rule7_cond)
        if matchcond7:
            print("match condition succeed")
            print(matchcond7)
            
matchthen7=thenPattern.match(Rule7_conc)
if matchthen7:
        print("match then succeed")
        matchconc7=parenthesePattern.findall(Rule7_conc)
        if matchconc7:
            print("match chonclusion succeed")
            print(matchconc7)

rule7=(tuple(matchcond7),tuple(matchconc7))
print(rule7)



############Rule8#################
print("\n")
print("Rule8:")
matchif8=ifPattern.match(Rule8_cond)    
if matchif8:
        print("match if succeed")
        matchcond8=parenthesePattern.findall(Rule8_cond)
        if matchcond8:
            print("match condition succeed")
            print(matchcond8)
            
matchthen8=thenPattern.match(Rule8_conc)
if matchthen8:
        print("match then succeed")
        matchconc8=parenthesePattern.findall(Rule8_conc)
        if matchconc8:
            print("match chonclusion succeed")
            print(matchconc8)

rule8=(tuple(matchcond8),tuple(matchconc8))
print(rule8)


############Rule9#################
print("\n")
print("Rule9:")
matchif9=ifPattern.match(Rule9_cond)    
if matchif9:
        print("match if succeed")
        matchcond9=parenthesePattern.findall(Rule9_cond)
        if matchcond9:
            print("match condition succeed")
            print(matchcond9)
            
matchthen9=thenPattern.match(Rule9_conc)
if matchthen9:
        print("match then succeed")
        matchconc9=parenthesePattern.findall(Rule9_conc)
        if matchconc9:
            print("match chonclusion succeed")
            print(matchconc9)

rule9=(tuple(matchcond9),tuple(matchconc9))
print(rule9)



############Rule10#################
print("\n")
print("Rule10:")
matchif10=ifPattern.match(Rule10_cond)    
if matchif10:
        print("match if succeed")
        matchcond10=parenthesePattern.findall(Rule10_cond)
        if matchcond10:
            print("match condition succeed")
            print(matchcond10)
            
matchthen10=thenPattern.match(Rule10_conc)
if matchthen10:
        print("match then succeed")
        matchconc10=parenthesePattern.findall(Rule10_conc)
        if matchconc10:
            print("match chonclusion succeed")
            print(matchconc10)

rule10=(tuple(matchcond10),tuple(matchconc10))
print(rule10)


############Rule11#################
print("\n")
print("Rule11:")
matchif11=ifPattern.match(Rule11_cond)    
if matchif11:
        print("match if succeed")
        matchcond11=parenthesePattern.findall(Rule11_cond)
        if matchcond11:
            print("match condition succeed")
            print(matchcond11)
            
matchthen11=thenPattern.match(Rule11_conc)
if matchthen11:
        print("match then succeed")
        matchconc11=parenthesePattern.findall(Rule11_conc)
        if matchconc11:
            print("match chonclusion succeed")
            print(matchconc11)

rule11=(tuple(matchcond11),tuple(matchconc11))
print(rule11)


############Rule12#################
print("\n")
print("Rule12:")
matchif12=ifPattern.match(Rule12_cond)    
if matchif12:
        print("match if succeed")
        matchcond12=parenthesePattern.findall(Rule12_cond)
        if matchcond12:
            print("match condition succeed")
            print(matchcond12)
            
matchthen12=thenPattern.match(Rule12_conc)
if matchthen12:
        print("match then succeed")
        matchconc12=parenthesePattern.findall(Rule12_conc)
        if matchconc12:
            print("match chonclusion succeed")
            print(matchconc12)

rule12=(tuple(matchcond12),tuple(matchconc12))
print(rule12)



############Rule13#################
print("\n")
print("Rule13:")
matchif13=ifPattern.match(Rule13_cond)    
if matchif13:
        print("match if succeed")
        matchcond13=parenthesePattern.findall(Rule13_cond)
        if matchcond13:
            print("match condition succeed")
            print(matchcond13)
            
matchthen13=thenPattern.match(Rule11_conc)
if matchthen13:
        print("match then succeed")
        matchconc13=parenthesePattern.findall(Rule13_conc)
        if matchconc13:
            print("match chonclusion succeed")
            print(matchconc13)

rule13=(tuple(matchcond13),tuple(matchconc13))
print(rule13)



############Rule14#################
print("\n")
print("Rule14:")
matchif14=ifPattern.match(Rule14_cond)    
if matchif14:
        print("match if succeed")
        matchcond14=parenthesePattern.findall(Rule14_cond)
        if matchcond14:
            print("match condition succeed")
            print(matchcond14)
            
matchthen14=thenPattern.match(Rule14_conc)
if matchthen14:
        print("match then succeed")
        matchconc14=parenthesePattern.findall(Rule14_conc)
        if matchconc14:
            print("match chonclusion succeed")
            print(matchconc14)

rule14=(tuple(matchcond14),tuple(matchconc14))
print(rule14)





#定义规则库
Rulebase=[]
print("\n","空规则库：",Rulebase)

Rulebase.append(rule1)
#print(Rulebase)
Rulebase.append(rule2)
#print(Rulebase)
Rulebase.append(rule3)
#print(Rulebase)
Rulebase.append(rule4)
#print(Rulebase)
Rulebase.append(rule5)
#print(Rulebase)
Rulebase.append(rule6)
#print(Rulebase)
Rulebase.append(rule7)
#print(Rulebase)
Rulebase.append(rule8)
#print(Rulebase)
Rulebase.append(rule9)
#print(Rulebase)
Rulebase.append(rule10)
#print(Rulebase)
Rulebase.append(rule11)
#print(Rulebase)
Rulebase.append(rule12)
#print(Rulebase)
Rulebase.append(rule13)
#print(Rulebase)
Rulebase.append(rule14)
print("\n","所有规则：",Rulebase)






