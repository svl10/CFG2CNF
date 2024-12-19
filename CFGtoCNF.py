# 'e' is reserve para epsilon
#First variable is the starting non-terminalS
#CNF rules, S -> ε, A -> AB, A -> a
#New start symbol $

def addtupes(tupes:list):

    nonterm = list(dict.fromkeys((input("Input non-terminals (First variable is the starting non-terminal):  ").replace(" ", "").upper())))
    print("non-terminals: ", nonterm)

    while True:
        terminals = list(set(input("Input terminals:  ").replace(" ", "").lower()))
        end = 1
        for i in terminals:
            if i == 'e':
                print("'e' is reserved for Epsilon")
                end = 0
                
        if end == 1:
            break
        
    print("terminals: ", terminals)
    
    strt = nonterm[0]
    # while True:
    #     strt = (input("Input starting non-terminal:  ").upper())
    #     if len(strt) == 1 and strt in nonterm:
    #         break
    #     else:
    #         print("Pls only input 1 starting non-terminal in non-terminals")
    #         continue
    # print("starting state: ", strt)

    while True:
        productions = list()
        for ntrm in nonterm:
        
            hold = [ntrm, tuple((input(f"Input productions for {ntrm} (serperate it by using spaces)")).split())]
            productions.append(hold)
        print(productions)
        
        for x in productions:
            for y in x[1]:
                for z in list(y):
                    if z in terminals or z in nonterm:
                        a = 1
                        continue
                    elif z == 'e':
                        a = 1
                    else:
                        a = 0
                        break
            if a == 0:
                print(f"Some values in {y} in not found in the non-terminals/terminals")
                break
        
        if a == 1:
            break
        
    tupes.append(nonterm)
    tupes.append(terminals)
    tupes.append(strt)
    tupes.append(productions)
            
    return tupes

def step1(tupes): #Eliminate start symbol from RHS
    nonterm = tupes[0]
    strt = tupes[0][0][0]
    prod = tupes[3]
    end = 0
    for i in prod: #check if start is at the right hand side
        for j in i[1]:
            if strt in list(j): #if it is then create $ as the new start state
                prod.append(['$', [strt]])
                nonterm.append('$')
                end = 1
                break
        if end == 1:
            break
        
    if '$' in tupes[0]:
        strt = '$'
        
    tupes[3] = prod
    tupes[2] = strt
    tupes[0] = nonterm
    print('Step 1: ', tupes)
    return tupes

def step2(tupes): #Eliminate null
    print('Step 2: ')
    prod = tupes[3]
    hasepsilon = list()
    hasepsilonwithextraproductions = list()
    
    lprod = list()
    newprod = list()
    newprod.extend(range(len(prod)))
    
    #initial
    #find if epsilon is present
    epsilonispresent = 0
    for i in prod:
        for j in i[1]:
            if j == 'e' and len(i[1]) == 1:
                hasepsilon.append(i[0])
                hasepsilon = list(set(hasepsilon))
                epsilonispresent = 1
            
            elif j == 'e' and len(i[1]) >= 2:
                hasepsilonwithextraproductions.append(i[0])
                hasepsilonwithextraproductions = list(set(hasepsilonwithextraproductions))
                epsilonispresent = 1
    
    if epsilonispresent == 0:
        print('There is no epsilon.')
        print(tupes)
        return tupes
    
    nontermpos = 0
    for i in prod:
        rprod = list()
        for j in i[1]:
            copyofj = j
            for k in hasepsilonwithextraproductions: #check if non-terms with epsilon is present in production
                numofnontermepsilon = list(j).count(k)
                position = 0

                if numofnontermepsilon >= 2: #if there is a production that has multiple nonterminal with an epsilon value
                    rprod.append(j)
                    for l in range(numofnontermepsilon):
                        oldrprodbutsplit = list(j)
                        position = list(j).index(k, position)
                        #print(position)
                        oldrprodbutsplit.pop(position)
                        #print(oldrprodbutsplit)
                        rprod.append(''.join(oldrprodbutsplit))
                        position += 1
                    copyofj = copyofj.replace(k, '')
                    rprod.append(copyofj)
                
                elif numofnontermepsilon == 1 and len(j) > 1: #if there is an epsilon only result
                    rprod.append(j)
                    copyofj = copyofj.replace(k, '')
                    rprod.append(copyofj)
                    
                elif numofnontermepsilon == 1:
                    copyofj = copyofj.replace(k, 'e')
                    rprod.append(copyofj)
                
                else:
                    rprod.append(copyofj)
                        
                
                
            
            for k in hasepsilon: #check if non-terms with epsilon is present in production
                numofnontermepsilon = list(j).count(k)
                position = 0
                
                if numofnontermepsilon >= 2: #if there is
                    rprod.append(j)
                    for l in range(numofnontermepsilon):
                        oldrprodbutsplit = list(j)
                        position = list(j).index(k, position)
                        #print(position)
                        oldrprodbutsplit.pop(position)
                        #print(oldrprodbutsplit)
                        rprod.append(''.join(oldrprodbutsplit))
                        position += 1
                    copyofj = copyofj.replace(k, '')
                    rprod.append(copyofj)
                
                elif numofnontermepsilon == 1 and len(j) > 1:
                    copyofj = copyofj.replace(k, '')
                    rprod.append(copyofj)
                    
                elif numofnontermepsilon == 1:
                    copyofj = copyofj.replace(k, 'e')
                    rprod.append(copyofj)
                        
                
                else:
                    rprod.append(j)
                    continue
        rprod = list(set(rprod))
        newprod[nontermpos] = [i[0], rprod]
        nontermpos += 1
    #print('dasd', newprod)
            
    #print('has epsilon: ', hasepsilon)

    for z in range(100):
        nontermpos = 0
        for i in newprod:
            rprod = list()
            for j in i[1]:
                copyofj = j
                for k in hasepsilonwithextraproductions: #check if non-terms with epsilon is present in production
                    numofnontermepsilon = list(j).count(k)
                    position = 0

                    if numofnontermepsilon >= 2: #if there is
                        rprod.append(j)
                        for l in range(numofnontermepsilon):
                            oldrprodbutsplit = list(j)
                            position = list(j).index(k, position)
                            #print(position)
                            oldrprodbutsplit.pop(position)
                            #print(oldrprodbutsplit)
                            rprod.append(''.join(oldrprodbutsplit))
                            position += 1
                        copyofj = copyofj.replace(k, '')
                        rprod.append(copyofj)
                    
                    elif numofnontermepsilon == 1 and len(j) > 1:
                        rprod.append(j)
                        copyofj = copyofj.replace(k, '')
                        rprod.append(copyofj)
                        
                    elif numofnontermepsilon == 1:
                        rprod.append(j)
                        copyofj = copyofj.replace(k, 'e')
                        rprod.append(copyofj)
                            
                    
                    
                    
                for k in hasepsilon: #check if non-terms with epsilon is present in production
                    numofnontermepsilon = list(j).count(k)
                    #print(j, 'count', numofnontermepsilon)
                    position = 0
                    
                    if numofnontermepsilon >= 2: #if there is
                        rprod.append(j)
                        for l in range(numofnontermepsilon):
                            oldrprodbutsplit = list(j)
                            position = list(j).index(k, position)
                            #print(position)
                            oldrprodbutsplit.pop(position)
                            #print(oldrprodbutsplit)
                            rprod.append(''.join(oldrprodbutsplit))
                            position += 1
                        copyofj = copyofj.replace(k, '')
                        rprod.append(copyofj)
                    
                    elif numofnontermepsilon == 1 and len(j) > 1:
                        copyofj = copyofj.replace(k, '')
                        rprod.append(copyofj)
                        
                    elif numofnontermepsilon == 1:
                        copyofj = copyofj.replace(k, 'e')
                        rprod.append(copyofj)
                            
                    
                    else:   
                        rprod.append(copyofj)
                        continue
                rprod.append(copyofj)
            rprod = list(set(rprod))
            #print(rprod)
            newprod[nontermpos] = [i[0], rprod]
            nontermpos += 1
        
            
        for i in newprod:
            for j in i[1]:
                if j == 'e' and len(i[1]) == 1:
                    hasepsilon.append(i[0])
                    hasepsilon = list(set(hasepsilon))
                    epsilonispresent = 1
            
                elif j == 'e' and len(i[1]) >= 2:
                    hasepsilonwithextraproductions.append(i[0])
                    hasepsilonwithextraproductions = list(set(hasepsilonwithextraproductions))
    

    #removing the remaining epsilon
    anothernewprod = list()
    countpos = 0
    for i in newprod:
        anotherrprod = list()
        for j in i[1]:
            if j == 'e':
                continue
            else:
                anotherrprod.append(j)
        
        anotherrprod = list(set(anotherrprod))
        anothernewprod.insert(countpos, [i[0], anotherrprod])
        countpos += 1
    newprod = list()
    
    for s in anothernewprod:
        if s[0] in hasepsilon:
            continue
        else:
            newprod.append(s)
        
    print('oldprod: ', prod)                
    print('newprod: ', newprod)           
    print('has epsilon: ', hasepsilon)
    print('has epsilon with extra productions: ', hasepsilonwithextraproductions)
    terms = tupes[0].copy()
    newterm = list()
    for i in terms:
        if i in hasepsilon:
            continue
        else:
            newterm.append(i)
    tupes[0] = newterm
    tupes[3] = newprod.copy()
    print(tupes[1])
    return tupes
                
                        

def clean(tupes): #Eliminate useless productions
    oldterm = tupes[1].copy()
    strt = tupes[2]
    prod = tupes[3]
    reachableNT = list(strt)
    reachableT = list()
    #print(strt)
    #for start
    for x, z in prod:
        if x == strt:
            for i in z:
                for j in list(i):
                    if j.isupper():
                        reachableNT.append(j)
                        #print(j)
                    elif j.islower():
                        reachableT.append(j)
                
    for z in range(len(prod)):
        for i in range(len(prod)):
            if prod[i][0] in reachableNT:
                for k in prod[i][1]:
                    for j in list(k):
                        if j.isupper():
                            reachableNT.append(j)
                        elif j.islower():
                            reachableT.append(j)
                            
    reachableNT = list(set(reachableNT))
    reachableT = list(set(reachableT))
    reachable = reachableT + reachableNT
    
    print('\nreachable: ', reachable)


    #removing unreachable
    newprod = list()
    newnonterm = list()
    newterm = list()

    for i in range(len(prod)):
        
        if prod[i][0] in reachableNT:
            term = prod[i][0]
            newnonterm.append(term)
            holdrprod = list()
            for z in prod[i][1]:
                holdrprod.append(z)
                
        else:
            continue
        newprod.append([term, holdrprod])
    
    for i in oldterm:
        if i in reachableT:
            newterm.append(i)
    

    tupes[0] = newnonterm
    tupes[1] = newterm
    tupes[3] = newprod
    #print(tupes)
    return tupes
    
                        
    
def step3(tupes): #Eliminate unit productions
    print('Step 3: ')
    prod = tupes[3]
    print('Old Prod: ', prod)
    newprod = list()
    oldprod = prod.copy()
    copyofprod = prod.copy()
    for z in range(200):
        newprod = list()
        for i in range(len(prod)):
            holdprod = prod[i]
            holdleft = holdprod[0]
            holdright = holdprod[1]
            holdlistright = list()
            for j in range(len(holdright)):
                onefromright = holdright[j]
                
                if onefromright.isupper() and len(onefromright) == 1:
                    #print(onefromright)
                    for k in prod:
                        if onefromright == k[0]:
                            for l in k[1]:
                                if l == onefromright:
                                    continue
                                else:
                                    holdlistright.append(l)
                                    
                                    
                else:
                    holdlistright.append(onefromright)
            
            holdlistright = list(set(holdlistright))
            newprod.append([holdleft, holdlistright])
            
        prod = newprod.copy()
    tupes[3] = prod
    #print(tupes[1])
    clean(tupes)
    print('New Productions: ', prod)
    return tupes
    

def step4(tupes): #Eliminate productions that have more than 2 Non-terminals
    print('Step 4: ')
    nonterm = tupes[0].copy()
    newterm = list()
    prod = tupes[3].copy()
    newprod = list()
    nontermsample = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i, j in prod:
        #print(i)
        #print(j)
        holdprodr = list()
        for k in j:
            numberofnonterms = 0

            for l in list(k):
                if l.isupper():
                    numberofnonterms += 1
            #print(numberofnonterms)
            if numberofnonterms > 2:
                for s in nontermsample:
                    if s not in nonterm:
                        addnonterm = s
                        break
                nonterm.append(addnonterm)
                holdrprod = k[:2]
                if [addnonterm, [holdrprod]] not in newprod:
                    newprod.append([addnonterm, [holdrprod]])
                    
                
                #print(holdrprod)
                holdprodr.append(str(addnonterm + '' + k[2:]))
            else:
                holdprodr.append(k)
        newprod.append([i, holdprodr])
        
    for z in range(100):
        anothernewprod = list()
        for i, j in newprod:
            #print(i)
            #print(j)
            holdprodr = list()
            for k in j:
                numberofnonterms = 0

                for l in list(k):
                    if l.isupper():
                        numberofnonterms += 1
                #print(numberofnonterms)
                if numberofnonterms > 2:
                    for s in nontermsample:
                        if s not in nonterm:
                            addnonterm = s
                            break
                    nonterm.append(addnonterm)
                    holdrprod = k[:2]
                    if [addnonterm, [holdrprod]] not in anothernewprod:
                        anothernewprod.append([addnonterm, [holdrprod]])
                        
                    
                    #print(holdrprod)
                    holdprodr.append(str(addnonterm + '' + k[2:]))
                else:
                    holdprodr.append(k)
            anothernewprod.append([i, holdprodr])
        
        newprod = anothernewprod.copy()
    print('Old Productions: ', prod)    
    print('New Productions: ', newprod)
    #print(nonterm)
    tupes[0] = nonterm
    tupes[3] = newprod
    #print(tupes[1])
    return tupes
                                

def step5(tupes): #Eliminate productions that have more than 1 Terminals
    print('Step 5: ')
    nonterms = tupes[0]
    newprod = list()
    prod = tupes[3]
    hasnonterm = 0
    hasterm = 0
    nontermsample = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for i, j in prod:
        updatedrprod = list()
        for k in j:
            holdrprod = list()
            position = 0
            copyofk = k
            hasterm = 0
            hasnonterm = 0
            holdterm = ''
            holdnonterm = ''
            for l in list(k):
                if l.isupper():
                    holdnonterm = l
                    hasnonterm += 1
                elif l.islower():
                    holdterm = l
                    hasterm += 1
            
            if hasterm >= 1 and hasnonterm >= 1:
                for x in nontermsample:
                    if x not in nonterms:
                        newterm = x
                        nonterms.append(newterm)
                        break
                holdrprod.append(holdterm)
                newprod.append([newterm, holdrprod])
                #print(k)
                updatedrprod.append(k.replace(holdterm, newterm, 1))
                #print(updatedrprod)
                #print(k, 'ssss', holdrprod)
                
            else:
                updatedrprod.append(k)
        
        newprod.append([i, updatedrprod])
    
    for z in range(100):
        anothernewprod = list()
        for i, j in newprod:
            updatedrprod = list()
            for k in j:
                holdrprod = list()
                position = 0
                copyofk = k
                hasterm = 0
                hasnonterm = 0
                holdterm = ''
                holdnonterm = ''
                for l in list(k):
                    if l.isupper():
                        holdnonterm = l
                        hasnonterm += 1
                    elif l.islower():
                        holdterm = l
                        hasterm += 1
                
                if hasterm >= 1 and hasnonterm >= 1:
                    for x in nontermsample:
                        if x not in nonterms:
                            newterm = x
                            nonterms.append(newterm)
                            break
                    holdrprod.append(holdterm)
                    anothernewprod.append([newterm, holdrprod])
                    #print(k)
                    updatedrprod.append(k.replace(holdterm, newterm, 1))
                    #print(updatedrprod)
                    #print(k, 'ssss', holdrprod)
                
                elif hasterm >=2:
                    for x in nontermsample:
                        if x not in nonterms:
                            newterm = x
                            nonterms.append(newterm)
                            break
                    holdrprod.append(holdterm)
                    anothernewprod.append([newterm, holdrprod])
                    #print(k)
                    updatedrprod.append(k.replace(holdterm, newterm, 1))
                    #print(updatedrprod)
                
                elif hasnonterm >= 3:
                    for x in nontermsample:
                        if x not in nonterms:
                            newterm = x
                            nonterms.append(newterm)
                            break
                    holdrprod.append(k[:2])
                    anothernewprod.append([newterm, holdrprod])
                    updatedrprod.append(k.replace(k[:2], newterm, 1))
                    
                else:
                    updatedrprod.append(k)
            
            anothernewprod.append([i, updatedrprod])
        newprod = anothernewprod.copy()
    print('Old Productions: ', prod)
    print('New productions: ',newprod)
    tupes[0] = nonterms.copy()
    tupes[3] = newprod.copy()
    #print(tupes[1])
    return tupes
                
def CFGtoCNF(tupes):
    tupes = step1(tupes) #Eliminate start symbol from RHS
    tupes = step2(tupes) #Eliminate null
    tupes = step3(tupes) #Eliminate unit and useless productions and 
    tupes = step4(tupes) #Eliminate productions that have more than 2 Non-terminals
    tupes = step5(tupes) #Eliminate productions that have more than 1 Terminals
    
    return tupes

def result(tupes):
    print()
    print('Non-terminals: ', tupe[0])
    print('Terminalls: ', tupe[1])
    print('Start: ', tupe[2])
    print('Productions: ', tupe[3])
    
    return 0

tupe = list()
addtupes(tupe)
result(tupe)
CFGtoCNF(tupe)
result(tupe)
