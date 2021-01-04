import numpy
import cv2
from matplotlib import pyplot as plt

    

disks=[]


def StoreTextToDisk(data):
    
    j=0
    if(len(data)%4>0):
        a=len(data)%4
        while a!=4:
            data.append(0)
            a=a+1
    print(data)
    while j<len(data):
        
        i=3
        while True:
            d1=[0,0,0,0]
            d2=[0,0,0,0]
            d1[3-i]=data[j]
            print("yes")
            j=j+1
            d1[2-i]=data[j]
            j=j+1
            d2[3-i]=data[j]
            j=j+1
            d2[2-i]=data[j]
            j=j+1
            d1[1-i]=d1[3-i]+d1[2-i]
            d1[0-i]=d1[3-i]+d1[2-i]
            d2[1-i]=d2[3-i]+d2[2-i]
            d2[0-i]=d2[3-i]+d2[2-i]
            d=[]
            d.append(d1)
            d.append(d2)  
            disks.append(d)
            i=i-1
            if(j==len(data)):
                break
            if i<0:
                i=3
    
    print(disks)


def DecodeImage(im):
    data=[]
    i=3
    j=0
    d=[]
    p=0
    while True:
        d.append(disks[j][0][3-i])
        d.append(disks[j][0][2-i])
        d.append(disks[j][1][3-i])
        d.append(disks[j][1][2-i])
        p=p+4
        #print("p value")
        #print(p)
        if p==len(im):
            data.append(d)
            d=[]
            p=0
        j=j+1
        if (j==len(disks)):
            break
        #print("j value")
        #print(j)
        i=i-1
        if(i<0):
            i=3
    print(data)
    print("final img is")
    plt.imshow(data)
    



def DecodeText():
    data=[]
    i=3
    j=0
    while True:
        data.append(disks[j][0][3-i])
        data.append(disks[j][0][2-i])
        data.append(disks[j][1][3-i])
        data.append(disks[j][1][2-i])
        j=j+1
        if (j==len(disks)):
            break
        print(j)
        i=i-1
        if(i<0):
            i=3
    
    final=''.join(chr(i) for i in data)
    print(final)
def StoreImageToDisk(data):
    print("image array in numpy form")
    print(data)
    j=0
    
    while j<len(data)*len(data[0]):
        x=0
        y=0
        i=3
        while True:
            d1=[0,0,0,0]
            d2=[0,0,0,0]
            d1[3-i]=data[y][x]
            #print(data[y][x])
            x=x+1
            
            if(x==len(data[0])):
                y=y+1
                x=0
            
            j=j+1
            d1[2-i]=data[y][x]
            #print(data[y][x])
            x=x+1
            if(x==len(data[0])):
                y=y+1
                x=0
            j=j+1
            d2[3-i]=data[y][x]
            #print(data[y][x])
            x=x+1
            if(x==len(data[0])):
                y=y+1
                x=0
            j=j+1
            d2[2-i]=data[y][x]
            #print(data[y][x])
            x=x+1
            if(x==len(data[0])):
                y=y+1
                x=0
            j=j+1
            d1[1-i]=d1[3-i]+d1[2-i] 
            d1[0-i]=d1[3-i]+d1[2-i]
            d2[1-i]=d2[3-i]+d2[2-i]
            d2[0-i]=d2[3-i]+d2[2-i]
            #print(d1)
            #print(d2)
            d=[]
            d.append(d1)
            d.append(d2)  
            disks.append(d)
            i=i-1
            if(j==(len(data)-1)*(len(data[0]-1))):
                #print("break at j")
                break
            
            if i<0:
                i=3
        if(j==(len(data)-1)*(len(data[0]-1))):
                #print("break at j")
                break
    print("image data in disks")
    print(disks)
    
  
def RecoverImage():
    i=3
    x=0
    y=0
    while True:
        if( disks[y][0][0]==0 and disks[y][0][1]==0 and disks[y][0][2]==0 and disks[y][0][3]==0):
            i=i-1
            if i<0:
                i=3
            y=y+1
            continue
        
        if(  (disks[y][0][1-i]==disks[y][0][0-i]) and disks[y][0][3-i]==0 ):
            disks[y][0][3-i]=disks[y][0][1-i]-disks[y][0][2-i]
        if(  (disks[y][0][1-i]==disks[y][0][0-i]) and disks[y][0][2-i]==0   ):
            disks[y][0][2-i]=disks[y][0][1-i]-disks[y][0][3-i]
        
        if(  (disks[y][0][1-i]!=disks[y][0][0-i]) and disks[y][0][1-i]==0 ):
            disks[y][0][1-i]=disks[y][0][0-i]
        if(  (disks[y][0][1-i]!=disks[y][0][0-i]) and disks[y][0][0-i]==0 ):
            disks[y][0][0-i]=disks[y][0][1-i]
        
        i=i-1
        y=y+1
        if i<0:
            i=3
        if y==len(disks):
            break
        
    i=3
    x=0
    y=0
    while True:
        if( disks[y][1][0]==0 and disks[y][1][1]==0 and disks[y][1][2]==0 and disks[y][1][3]==0):
            i=i-1
            if i<0:
                i=3
            y=y+1
            continue
        
        if(  (disks[y][1][1-i]==disks[y][1][0-i]) and disks[y][1][3-i]==0 ):
            disks[y][1][3-i]=disks[y][1][1-i]-disks[y][1][2-i]
        if(  (disks[y][1][1-i]==disks[y][1][0-i]) and disks[y][1][2-i]==0 ):
            disks[y][1][2-i]=disks[y][1][1-i]-disks[y][1][3-i]
        
        if(  (disks[y][1][1-i]!=disks[y][1][0-i]) and disks[y][1][1-i]==0 ):
            disks[y][1][1-i]=disks[y][1][0-i]
        if(  (disks[y][1][1-i]!=disks[y][1][0-i]) and disks[y][1][0-i]==0 ):
            disks[y][1][0-i]=disks[y][1][1-i]
        
        i=i-1
        y=y+1
        if i<0:
            i=3
        if y==len(disks):
            break
    print(disks)
    
def  DeleteImageDisk(p):
    i=0
    
    while True:
        disks[i][0][p]=0
        disks[i][1][p]=0
        i=i+1
        if (i==len(disks)):
            break
    #print(disks)


def RecoverText():
    i=3
    x=0
    y=0
    while True:
        if( disks[y][0][0]==0 and disks[y][0][1]==0 and disks[y][0][2]==0 and disks[y][0][3]==0):
            i=i-1
            if i<0:
                i=3
            y=y+1
            continue
        
        if(  (disks[y][0][1-i]==disks[y][0][0-i]) and disks[y][0][3-i]==0 ):
            disks[y][0][3-i]=disks[y][0][1-i]-disks[y][0][2-i]
        if(  (disks[y][0][1-i]==disks[y][0][0-i]) and disks[y][0][2-i]==0   ):
            disks[y][0][2-i]=disks[y][0][1-i]-disks[y][0][3-i]
        
        if(  (disks[y][0][1-i]!=disks[y][0][0-i]) and disks[y][0][1-i]==0 ):
            disks[y][0][1-i]=disks[y][0][0-i]
        if(  (disks[y][0][1-i]!=disks[y][0][0-i]) and disks[y][0][0-i]==0 ):
            disks[y][0][0-i]=disks[y][0][1-i]
        
        i=i-1
        y=y+1
        if i<0:
            i=3
        if y==len(disks):
            break
        
    i=3
    x=0
    y=0
    while True:
        if( disks[y][1][0]==0 and disks[y][1][1]==0 and disks[y][1][2]==0 and disks[y][1][3]==0):
            i=i-1
            if i<0:
                i=3
            y=y+1
            continue
        
        if(  (disks[y][1][1-i]==disks[y][1][0-i]) and disks[y][1][3-i]==0 ):
            disks[y][1][3-i]=disks[y][1][1-i]-disks[y][1][2-i]
        if(  (disks[y][1][1-i]==disks[y][1][0-i]) and disks[y][1][2-i]==0 ):
            disks[y][1][2-i]=disks[y][1][1-i]-disks[y][1][3-i]
        
        if(  (disks[y][1][1-i]!=disks[y][1][0-i]) and disks[y][1][1-i]==0 ):
            disks[y][1][1-i]=disks[y][1][0-i]
        if(  (disks[y][1][1-i]!=disks[y][1][0-i]) and disks[y][1][0-i]==0 ):
            disks[y][1][0-i]=disks[y][1][1-i]
        
        i=i-1
        y=y+1
        if i<0:
            i=3
        if y==len(disks):
            break
    print(disks)

    

def  DeleteTextDisk(p):
    i=0
    
    while True:
        disks[i][0][p]=0
        disks[i][1][p]=0
        i=i+1
        if (i==len(disks)):
            break
    print(disks)

    
    
print("Type 1 for text\nType 2 for image\n")
i=int(input("Enter"))
if i==1:
    n=input("ENTER  : ")
    l=[]
    for q in n:
        l.append(ord(q))
    StoreTextToDisk(l)
    
    p=int(input("enter disk to be deleted:"))
    DeleteTextDisk(p)
    
    n=int(input("press 1 to recover:"))
    
    
    if n==1:
        RecoverText()
        DecodeText()
    
        
    
    
if i==2:
        
    im=cv2.imread("sample p.jpg",0)
    StoreImageToDisk(im)
    """n=int(input("press 1 to recover:"))
    if n==1:
        DecodeImage(im)
"""
    p=int(input("disk to erase:"))
    
    DeleteImageDisk(p)
    DecodeImage(im)
    q=int(input("press 1 for recover image"))
    if q==1:
        RecoverImage()
        
    DecodeImage(im)