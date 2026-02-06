#recurssion basic (Head recurssion)

count = 0
def demo_testing():
    global count
    if count == 6:
        return
    print("Avinash")
    
    count+=1
    #print(count)
    demo_testing()
    
demo_testing()


#recurssion basic (tail recurssion)

count1=0
def demo_testing_tail():
    global count1
    if count1==4:
        return
    count1+=1
    demo_testing_tail()
    
    print("Sharma")
    
demo_testing_tail()
