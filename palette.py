from PIL import Image, ImageDraw, ImageFont
colors = [(3,197,201),(255,59,255),(19,24,46),(10,132,255)]  # turquoise, magenta, dark, blue
w,h = 800,400
img = Image.new('RGB',(w,h),(8,12,24))
draw = ImageDraw.Draw(img)

# draw four vertical swatches
seg = w//4
for i,c in enumerate(colors):
    draw.rectangle([i*seg,0,(i+1)*seg,h], fill=c)

# save
img.save('palette.png')
print("Saved palette.png")
