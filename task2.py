# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 23:25:31 2016

@author: Admin
"""

import matplotlib.pyplot as plt
	import matplotlib.image as mpimg
	import numpy as np
	

	img=mpimg.imread('Lenna.tiff')
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

