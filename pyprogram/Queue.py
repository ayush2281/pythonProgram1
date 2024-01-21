#the Queue is linear data type
#stores items in first out(FIFO) manner

# l=[]
# while True:
#     c=int(input('''
#        1 Push Element
#        2 Pop first Element
#        3 front Element
#        4 last Element
#        5 display
#        6 exit
#        '''))
#
#     if c==1:
#         n=input("Enter the value")
#         l.append(n)
#         print(l)
#     elif c==2:
#         if len(l)==0:
#             print("Empty Queue")
#         else:
#             del l[0]
#             print(l)
#
#     elif c==3:
#         if len(l)==0:
#             print("Empty Queue")
#         else:
#             print("first Queue element",l[0])
#     elif c==4:
#         if len(l)==0:
#             print("Empty Queue")
#         else:
#             print("last Queue element",l[-1])
#     elif c==5:
#         print("display Queue",l)
#
#     elif c==6:
#         break;
#     else:
#         print("invallid opr")
#
