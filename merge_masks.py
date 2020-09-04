#Importing all the packages
import numpy as np
from skimage import io
import os
import matplotlib.pyplot as plt

print("hello world")
#Path for original mask
left_mask_path ='ManualMask/leftMask'
right_mask_path = 'ManualMask/rightMask'

def list_mask(file_path):
  img = []
  for filename in sorted(os.listdir(file_path)):
    mask= io.imread(file_path +'/' + filename)
    img.append(mask)
    print(filename)
  img= np.array(img)
  return img

#Call for the function to load the manual mask
left_mask = list_mask(left_mask_path)
right_mask = list_mask(right_mask_path)

#Viewing the data from the loaded mask
plt.subplot(1,2,1)
plt.imshow(left_mask[137])
plt.subplot(1,2,2)
plt.imshow(right_mask[137])

len(right_mask)

#Defining function to merge the manual masks
def merge_mask(left_mask, right_mask):
  img=[]
  for i in range(138):
    merged_image= left_mask[i] + right_mask[i]
    img.append(merged_image)
  img=np.array(img)
  return img

#Call for function
merged_images= merge_mask(left_mask, right_mask)

plt.imshow(merged_images[137])

#Saving the merged mask to the MergedMask directory
save_path = 'ManualMask/MergedMask'
for i in range(138):
  io.imsave(save_path + '/' + f"m_{str(i).zfill(4)}.png", merged_images[i]  ) #.zfill(4) to make files 0000,0001

#Loading the saved mask to check the merged manual masks
a= io.imread('ManualMask/MergedMask/m_0030.png')

plt.imshow(a)