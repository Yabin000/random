import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image


durian = Image.open("durian.jpg").resize((250, 250))
sit = Image.open("sit_on_knee.jpg").resize((250, 250))

fig, ax = plt.subplots(figsize=(8,6))

ax.imshow(durian) 
ax.imshow(sit, alpha=0.5) 

plt.show()
