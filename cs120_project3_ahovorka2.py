#Alan Hovorka
#10-17-16
#collage function
def collage():
  #Sets up the file locations
  setMediaPath()
  canvas = makeEmptyPicture(700, 515)
  pic = makePicture(getMediaPath("planet2.jpg"))
  sig = makePicture(getMediaPath("sig.jpg"))
  copy(pic, canvas, 0, 0)
  flipVertical(pic, canvas, 699,0)
  pic2 = makePicture(getMediaPath("planet2.jpg"))
  negative(pic2)
  copy(pic2, canvas, 0, 318)
  flipVertical(pic2, canvas, 699,318)
  pic3 = makePicture(getMediaPath("planet2.jpg"))
  sephiaTintAlt(pic3)
  flipHoriz(pic3, canvas, 0, 390)
  flipHorizVert(pic3, canvas, 699, 390)
  #Manages the overlap and graident between pic2 and pic3
  #blend(pic3,pic2,canvas,0,319)
  #blend(pic3,pic2,canvas,350,319)
  pic4 = makePicture(getMediaPath("planet.jpg"))
  #copies a crop of a big sun onto the image that also blends it in
  copyBigSun(pic4, canvas, 328, 1, 0.5)
  sephiaTintAlt(pic4)
  copyBigSun(pic4, canvas, 328, 320, .4)
  chromaSig(sig, canvas, 500, 440)
  show(canvas)
  #explore(canvas)
  #writePictureTo(canvas, "hovorka_the_other_collage.jpg")

#Crops a sun, copies it to the canvas and then blends it into the background
def copyBigSun(source, target, targX, targY,ratio):
  targetX = targX
  for sourceX in range(390,432):
    targetY = targY
    for sourceY in range(55,97):
      px=getPixel(source,sourceX,sourceY)
      tx=getPixel(target,targetX,targetY)
      #blending happens here
      newRed= ratio*getRed(px)+(1.0-ratio)*getRed(tx)
      newGreen = ratio*getGreen(px)+(1.0-ratio)*getGreen(tx)
      newBlue = ratio*getBlue(px)+(1.0-ratio)*getBlue(tx)
      color = makeColor(newRed,newGreen,newBlue)
      setColor(getPixel(target,targetX,targetY),color)
      targetY=targetY+ 1
    targetX=targetX + 1

#Places my signature on to the image
def chromaSig(source, target, targetX, targetY):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      px = getPixel(source, x, y)
      color = getColor(px)
      targ = getPixel(target, x + targetX, y + targetY)
      
      if distance(black, color) < 200: #determines what pixels get recolored
        setColor(targ, white)
            
#Standard Sephia Tinting  
def sephiaTint(pic):
  for px in getPixels(pic):
    red = getRed(px)
    blue=getBlue(px)
    if(red<63):
      red=red*1.1
      blue=blue*0.9
    if(red>62 and red<192):
      red=red*1.15
      blue=blue*0.85
    if(red>191):
      red=red*1.08
      if(red>255):
        red=255
      blue=blue*0.93
    setBlue(px,blue)
    setRed(px,red)

#Alternative Sephia Tinting that accounts for a greater variety of shades of grey
def sephiaTintAlt(pic):
  for px in getPixels(pic):
    red = getRed(px)
    blue=getBlue(px)
    green=getGreen(px)
    if(red>=0 and red<=63):
      red=40
      blue=40
      green=40    
    if(red>=64 and red<=90):
      red=100
      blue=100
      green=100
    if(red>=91 and red<=105):
      red=80
      blue=80
      green=80
    if(red>=106 and red<=119):
      red=111
      blue=111
      green=111
    if(red>=120 and red<=160):
      red=213
      blue=213
      green=213
    if(red>=161 and red<=170):
      red=170
      blue=170
      green=170
    if(red>=171 and red<=178):
      red=150
      blue=150
      green=150      
    if(red>=179 and red<=217):
      red=189
      blue=189
      green=189
    if(red>=218 and red <=230):
      red=202
      blue=202
      green=202
    if(red>=231 and red <=255):
      red=240
      blue=240
      green=240
    setBlue(px,blue)
    setRed(px,red)
    setGreen(px,green)

#inverses the orginial photo's color        
def negative(pic):
  for px in getPixels(pic):
    negColor = makeColor(255 - getRed(px), 255 - getGreen(px), 255 - getBlue(px))
    setColor(px, negColor)

#detects edges
def edge(source):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if y < getHeight(source)-1 and x < getWidth(source)-1:
      sum = getRed(px)+getGreen(px)+getBlue(px)
      botrt = getPixel(source,x+1,y+1)
      sum2 = getRed(botrt)+getGreen(botrt)+getBlue(botrt)
      diff = abs(sum2-sum)
      newcolor = makeColor(diff,diff,diff)
      setColor(px,newcolor)

#Copies our orginial image on to the canvas
def copy(source, target, targX, targY):
  targetX = targX
  for sourceX in range(0,getWidth(source)):
    targetY = targY
    for sourceY in range(0,getHeight(source)):
      px=getPixel(source,sourceX,sourceY)
      tx=getPixel(target,targetX,targetY)
      setColor(tx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1    

#mirrors the orginial photo
def flipVertical(source, target, targX, targY):
  targetX = targX
  for sourceX in range(0,getWidth(source)):
    targetY = targY
    for sourceY in range(0,getHeight(source)):
      px=getPixel(source,sourceX,sourceY)
      tx=getPixel(target,targetX,targetY)
      setColor(tx,getColor(px))
      targetY=targetY + 1
    targetX=targetX - 1   

#blends overlap for photos, calls in two sources and blends them on to the canvas
def blend(source1, source2, target, targX, targY):
  targetX = targX
  for sourceX in range(0,getWidth(source1)):
    targetY = targY
    for sourceY in range(0,72):
      px1=getPixel(source1,sourceX,sourceY)
      px2=getPixel(source2,sourceX,72-sourceY)
      #blending happens here
      newRed= 0.50*getRed(px1)+0.50*getRed(px2)
      newGreen=0.50*getGreen(px1)+0.50*getGreen(px2)
      newBlue = 0.50*getBlue(px1)+0.50*getBlue(px2)
      color = makeColor(newRed,newGreen,newBlue)
      setColor(getPixel(target,targetX,targetY),color)
      targetY=targetY+1
    targetX=targetX+1

#A horizontal mirror function
def flipHoriz(source, target, targX, targY):
  targetX = targX
  for sourceX in  range(0,getWidth(source)):
    targetY = targY
    for sourceY in range(0,getHeight(source)):
      px=getPixel(source,sourceX,sourceY)
      tx=getPixel(target,targetX,targetY)
      setColor(tx,getColor(px))
      targetY=targetY - 1
    targetX=targetX + 1  

#Horizontal and vertical mirror function
def flipHorizVert(source, target, targX, targY):
  targetX = targX
  for sourceX in range(0,getWidth(source)):
    targetY = targY
    for sourceY in range(0,getHeight(source)):
      px=getPixel(source,sourceX,sourceY)
      tx=getPixel(target,targetX,targetY)
      setColor(tx,getColor(px))
      targetY=targetY - 1
    targetX=targetX - 1  

collage()
