import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab

img = ImageGrab.grab()


plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()