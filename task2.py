import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as la	

img=mpimg.imread('tohoshinki.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]	

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

[r2,g2,b2]=[img[:,:,i]for i in range(3)]
red={'Index':0,'Mat': r2,'Color' : 'Reds', 'img':'Red'}
green={'Index':1,'Mat': g2,'Color' : 'Greens','img':'Green'}
blue={'Index':2,'Mat': b2,'Color' : 'Blues','img':'Blue'}
rgb=[red,green,blue]

for color in rgb:
    plt.imshow(color['Mat'],cmap=color['Color'])
    plt.imsave(color['img'], NewImg)
    plt.show()
    
    #Single Value Decomposition of img
    U,s,V=la.svd(color['Mat'])
    S=np.zeros(color['Mat'].shape,s.dtype)
    
    for i in range(s.size):
        S[i][i]=s[i]
    color['U']=U
    color['eigenvalues']=s
    color['S']=S
    color['V']=V
    
    NewImg=np.zeros_like(img)
    for dimension in (30,200):
        for color in rgb:
            New_S=np.zeros(color['Mat'].shape,s.dtype)
            for i in range (dimension):
                New_S[i][i]=color['eigenvalues'][i]
            NewImg[:,:,color['Index']]=np.dot(np.dot(color['U'],New_S),color['V'])
        plt.imshow(NewImg)
    if(dimension==30):
       plt.imsave('Tohoshinki_lower.jpg',NewImg)
    if(dimension==200):
       plt.imsave('Tohoshinki_better.jpg',NewImg)
    plt.show()
    
    