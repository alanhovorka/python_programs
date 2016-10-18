#LIGHTEN FUNCTIONS
def lighten(picture):
  for x in range(0,getWidth(picture)):
    for y in range(0,getHeight(picture)):
      px = getPixel(picture,x,y)
      color = getColor(px)
      color = makeLighter(color)
      setColor(px,color)

def lighten2(picture):
  w=getWidth(picture)
  h=getHeight(picture)
  for y in range(0,h):
    for x in range(0,w/2):
      px = getPixel(picture,x,y)
      color = getColor(px)
      color = makeLighter(color)
      setColor(px,color)


def lighten3(picture):
  w=getWidth(picture)
  h=getHeight(picture)
  for x in range(0,w):
    for y in range(0,h/2):
      px = getPixel(picture,x,y)
      color = getColor(px)
      color = makeLighter(color)
      setColor(px,color)

def lighten4(picture):
  w=getWidth(picture)
  h=getHeight(picture)
  for x in range(0,w/2):
    for y in range(0,h/2):
      px = getPixel(picture,x,y)
      color = getColor(px)
      color = makeLighter(color)
      setColor(px,color)

def lighten5(picture):
  w=getWidth(picture)
  h=getHeight(picture)
  for y in range(0,h):
    for x in range(w/2,w):
      px = getPixel(picture,x,y)
      color = getColor(px)
      color = makeLighter(color)
      setColor(px,color)

def lighten6(picture):
  for px in getPixels(picture):
    color = getColor(px)
    color = makeLighter(color)
    setColor(px,color)

#COLOR FUNCTIONS
def decreaseRed(picture):
  for pixels in getPixels(picture):
    setRed(pixels,getRed(pixels)*0.5)

def increaseRed(picture):
  for x in range(0,getWidth(picture)):
  #First time through the loop x is the name for 0, processes the first column of pixels in a picture
    for y in range(0,getHeight(picture)):
    #sets y to 0 so we can process each of the pixels in the first column
      for px=getPixel(picture,x,y)
      #x=0 and y=0
      value=getRed(px)
      setRed(px,value*1.1)

def clearBlue(picture):
  for p in getPixels(picture):
    setBlue(p,0)

def reduceBlue(picture):
  for p in getPixels(picture):
    value=getBlue(p)
    setBlue(p,value*0.7)

def reduceGreen(picture):
  for p in getPixels(picture):
    value=getGreen(p)
    setGreen(p,value*0.7)

def colorChange(picture):
  for px in getPixels(picture):
    newRed = getRed(px)*2
    newGreen = getGreen(px) * 0.5
    newBlue = getBlue(px) * 0.5
    change = newRed+newGreen+newBlue
    setColor(px,makeColor(change,change,change))

def clearRedOnHalf(picture):
  allpixels = getPixels(picture)
  for i in range(0,len(allpixels)/2):
    pixel = allpixels[i]
    setRed(pixel,0)

def color2(picture):
  for p in getPixels(picture):
    value=getBlue(p)
    setBlue(p,value*0.5)
    value=getGreen(p)
    setGreen(p,value*0.3)
    value=getRed(p)
    setRed(p,value*0.8)

def decreaseRedIndexed(picture):
  pixels = getPixels(picture)
  for index in range(0,len(pixels)):
    pixel = pixels[index]
    value = getRed(pixel)
    setRed(pixel,value*0.5)

def clearRedOnHalf(picture):
  allpixels = getPixels(picture)
  for i in range(0,len(allpixels)/2):
    pixel = allpixels[i]
    setRed(pixel,0)

def mixedRedThirds(picture):
  w=getWidth(picture)
  h=getHeight(picture)
  for x in range(0,w):
    for y in range(0,h/3):
      px = getPixel(picture,x,y)
      r=getRed(px)
      setRed(px,r*2)
    for y in range(h/2,h):
      px=getPixel(picture,x,y)
      r=getRed(px)
      setRed(px,r/2)
      
def mixedRedHalves(picture):
  w=getWidth(picture)
  h=getHeight(picture)
  for x in range(0,w/2):
    for y in range(0,h/2):
      px=getPixel(picture,x,y)
      r=getRed(px)
      setRed(px,r*2)
    for y in range(h/2,h):
      px=getPixel(picture,x,y)
      r=getRed(px)
      setRed(px,r/2)

def mixedRed(picture):
  w=getWidth(picture)
  h=getHeight(picture)
  for x in range(0,w):
    for y in range(0,h/2):
      px=getPixel(picture,x,y)
      r=getRed(px)
      setRed(px,r/2)
    for y in range(h/2,h):
      px=getPixel(picture,x,y)
      r=getred(px)
      setRed(px,r*2)
   

#can change this to refer to a defined picture)
def turnRedInRange():
  brown=makeColor(57,16,8)
  #or file=“/Users/guzdial/mediasources/barbara.jpg"
  #picture=makePicture(file)
  file=getMediaPath("barbara.jpg")
  picture = makePicture(file)
  for x in range(70,168):
    for y in range(56,190):
      px=getPixel(picture,x,y)
      color=getColor(px)
      if distance(color,brown)<50.0:
        redness=getRed(px)*1.5
        setRed(px,redness)
  show(picture)
  return(picture)
  
#We can copy between pictures if we track the source index variables and 
#the target indx variables, where we pull from and where they go
#This really just replicates the color
#We do this by creating a sourceX and sourceY and targetX and targetY
#This copying is done in increments 


#SHADING
def darken(picture):
  for px in getPixels(picture):
    color = getColor(px)
    color = makeDarker(color)
    setColor(px,color)

def negative(picture):
  for px in getPixels(picture):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255-red,255-green,255-blue)
    setColor(px,negColor)

#Greyscale

def greyScale(picture):
  for p in getPixels(picture):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p,makeColor(intensity,intensity,intensity))

def greyScaleNew(picture):
  for px in getPixels(picture):
    newRed = getRed(px)*0.299
    newGreen = getGreen(px) * 0.587
    newBlue = getBlue(px) * 0.114
    luminance = newRed+newGreen+newBlue
    setColor(px,makeColor(luminance,luminance,luminance))

#SUNSET
def makeSunset2(picture):
  reduceBlue(picture)
  reduceGreen(picture)

def makeSunset(picture):
  for p in getPixels(picture):
    value=getBlue(p)
    setBlue(p,value*0.7)
    value=getGreen(p)
    setGreen(p,value*0.7)




#MIRROR/COPY
def mirrorVertical(picture):
  mirrorPoint=getWidth(picture)/2
  width=getWidth(picture)
  for y in range(0,getHeight(picture)):
    for x in range(0,mirrorPoint):
      leftPixel=getPixel(picture,x,y)
      rightPixel=getPixel(picture,width - x -1,y)
      color = getColor(leftPixel)
      setColor(rightPixel,color)

def mirrorHorizontal(picture):
  mirrorPoint=getHeight(picture)/2
  height=getHeight(picture)
  for x in range(0,getWidth(picture)):
    for y in range(0,mirrorPoint):
      topPixel=getPixel(picture,x,y)
      bottomPixel=getPixel(picture,x,height - y - 1)
      color=getColor(topPixel)
      setColor(bottomPixel,color)


def mirrorBotTop(picture):
  mirrorPoint=getHeight(picture)/2
  height=getHeight(picture)
  for x in range(0,getWidth(picture)):
    for y in range(0,mirrorPoint):
      topPixel=getPixel(picture,x,y)
      bottomPixel=getPixel(picture,x,height - y - 1)
      color = getColor(bottomPixel)
      setColor(topPixel,color)

def mirrorTemple():
  source=makePictu
  for x in range(13,mirrorPoint):
    for y in range(27,97):
      pleft=getPixel(source,x,y)
      pright=getPixel(source,mirrorPoint + mirrorPoint - 1 - x,y)
      setColor(pright,getColor(pleft))
  show(source)
  return source

def copyHalf(picture):
  pixels = getPixels(picture)
  for index in range(0,len(pixels)/2):
    pixel1 = pixels[index]
    color1 = getColor(pixel1)
    pixel2 = pixels[index + len(pixels)/2]
    setColor(pixel2,color1)
  


def copyHalf1(picture):
  pixels = getPixels(picture)
  for index in range(0,len(pixels)/8):
    pixel1 = pixels[index]
    color1 = getColor(pixel1)
    pixel2 = pixels[index + len(pixels)/64]
    setColor(pixel2,color1)

def mirrorHalf(picture):
  pixels = getPixels(picture)
  target = len(pixels) - 1
  for index in range(0,len(pixels)/2):
    pixel1 = pixels[index]
    color1 = getColor(pixel1)
    pixel2 = pixels[target]
    setColor(pixel2,color1)
    target = target - 1

def copyHalfrev(picture):
  pixels = getPixels(picture)
  for index in range(0,len(pixels)/2):
    pixel1 = pixels[index + len(pixels)/2]
    color1 = getColor(pixel1)
    pixel2 = pixels[index]
    setColor(pixel2,color1)

def copyBarb():
  barbf=getMediaPath("barbara.jpg")
  barb = makePicture(barbf)
  canvasf = getMediaPath("640x480.jpg")
  canvas = makePicture(canvasf)
  targetX = 0
  for sourceX in range(0,getWidth(barb)):
    targetY=0
    for sourceY in range(0,getHeight(barb)):
      #this does the actual copying
      color=getColor(getPixel(barb,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      #begin incrementing
      targetY = targetY + 1
    targetX = targetX + 1
    #Doesn't name itself, it's evaluating, incrementing
  show(barb)
  show(canvas)
  return canvas

def copyBarb2():
  #set the source and target pics
  barbf=getMediaPath("barbara.jpg)
  barb=makePicture(barbf)
  #BLANK CANVAS/TARGET CANVAS, INSERT NAME
  canvasf=getMediaPath(" ")
  canvas=makePicture(canvasf)
  #begin copying
  sourceX=0
  for targetX in range(0,getWidth(barb)):
    sourceY=0
    for targetY in range(0,getHeight(barb)):
      color=getColor(getPixel(barb,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      sourceY=sourceY + 1
    sourceX=sourceX + 1
  show(barb)
  show(canvas)
  return canvas
  
def copyBarbMidway():
#set up source/targets
  barbf=getMediaPath("barbara.jpg)
  barb=makePicture(barbf)
  #BLANK CANVAS/TARGET CANVAS, INSERT NAME
  canvasf=getMediaPath(" ")
  canvas=makePicture(canvasf)
  targetX=100
  for sourceX in range(0,getWidth(barb)):
    targetY = 100
    for sourceY in range(0,getHeight(barb)):
      color=getColor(getPixel(barb,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY=targetY + 1
    tarrgetX = targetX + 1
  show(barb)
  show(canvas)
  return canvas
  

def copyBarb1():
  barbf=getMediaPath("barbara.jpg")
  src = makePicture(barbf)
  canvas = makeEmptyPicture(1000,1000)
  targetX = 100
  for sourceX in range(0,getWidth(src)):
    targetY = 200
    for sourceY in range(0,getHeight(src)):
      color = getColor(getPixel(src,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY +1 
    targetX = targetX + 1
  show(src)
  show(canvas)
  return canvas

def cropHorse():
  barbf=getMediaPath("horse.jpg")
  src = makePicture(barbf)
  canvas = makeEmptyPicture(1000,1000)
  targetX = 100
  for sourceX in range(104,267):
    targetY = 200
    for sourceY in range(114,422):
      color = getColor(getPixel(src,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY +1 
    targetX = targetX + 1
  show(src)
  show(canvas)
  return canvas

#alternate copying method
def copyHorseFace2():
  src=makePicture("horse.jpg")
  canvas = makeEmptyPicture(1000,1000)
  sourceX = 104
  for targetX in range(100,100+163):
    sourceY = 114
    for targetY in range(200,200+308):
      color = getColor(getPixel(src,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      sourceY=sourceY + 1
    sourceX = sourceX + 1
  show(canvas)
  return canvas

def copyBarb2():
  barbf=getMediaPath("barbara.jpg")
  src = makePicture(barbf)
  canvas = makeEmptyPicture(1000,1000)
  targetX = getHeight(canvas)/2 - getHeight(src)/2
  for sourceX in range(0,getWidth(src)):
    targetY = getWidth(canvas)/2 - getWidth(src)/2
    for sourceY in range(0,getHeight(src)):
      color = getColor(getPixel(src,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY +1 
    targetX = targetX + 1
  show(src)
  show(canvas)
  return canvas

#left to right color mirror
def mirrorVerticalRed1(source):
  mirrorPoint=getWidth(source)/2
  width=getWidth(source)
  for y in range(0,getHeight(source)):
    for x in range(0,mirrorPoint):
      leftPixel=getPixel(source,x,y)
      rightPixel=getPixel(source,width - x - 1,y)
      r=getRed(leftPixel)
      setRed(rightPixel,r)

#right to left color mirror
def mirrorVerticalRed1(source):
  mirrorPoint=getWidth(source)/2
  width=getWidth(source)
  for y in range(0,getHeight(source)):
    for x in range(0,mirrorPoint):
      leftPixel=getPixel(source,x,y)
      rightPixel=getPixel(source,width - x - 1,y)
      r=getRed(rightPixel)
      setRed(leftPixel,r)

def mirrorHorizontal(source):
  mirrorPoint=getHeight(source)/2
  height=getHeight(source)
  for x in range(0,getWidth(source)):
    for y in range(0,mirrorPoint):
      topPixel=getPixel(source,x,y)
      #option 1: bottomPixel=getPixel(source,x,height-y-1)
      #option 2: bottomPixel=getPixel(source,x,mirrorPoint+y)
      #option 3: bottomPixel=getPixel(source,x,mirrorPoint-y)
      color=getColor(bottomPixel)
      setColor(topPixel,color)

def copyAnyPic(src,canvas,x,y):
  targetX = x
  for sourceX in range(0,getWidth(src)):
    targetY = y
    for sourceY in range(0,getHeight(src)):
      srcPixel = getPixel(src,sourceX,sourceY)
      trgPixel = getPixel(canvas,targetX,targetY)
      setColor(trgPixel,getColor(srcPixel))
      targetY = targetY + 1
    targetX = targetX + 1


def copyPicDifferent(src,canvas,x,y):
  targetX = x
  for sourceX in range(0,getWidth(src)):
    targetY = y
    for sourceY in range(0,getWidth(src)):
      srcPixel = getPixel(src,sourceX,sourceY)
      trgPixel = getPixel(canvas,int(targetX),int(targetY))
      setColor(trgPixel,getColor(srcPixel))
      targetY=targetY + 1.5
    targetX = targetX + 1.5

def copyHorseFaceSmall():
  # Set up the source and target pictures
  src = makePicture("horse.jpg")
  canvas = makeEmptyPicture(163,308)
  # Now, do the actual copying
  targetX = 0
  for sourceX in range(104,267):
    targetY = 0
    for sourceY in range(114,422):
      color = getColor(getPixel(src,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY), color)
      targetY = targetY + 1
    targetX = targetX + 1
  show(canvas)
  return canvas
  
def copyHorseFaceSmallBlack():
  hcol = makeColor(216,169,143)
  # Set up the source and target pictures
  src = makePicture("horse.jpg")
  canvas = makeEmptyPicture(163,308)
  # Now, do the actual copying
  targetX = 0
  for sourceX in range(104,267):
    targetY = 0
    for sourceY in range(114,422):
      color = getColor(getPixel(src,sourceX,sourceY))
      if distance(color,hcol) < 40:
        setColor(getPixel(canvas,targetX,targetY), black)
      else:
        setColor(getPixel(canvas,targetX,targetY), color)
    targetY = targetY + 1
  targetX = targetX + 1
  show(canvas)
  return canvas

def copy1(source, target, targX, targY):
  targetX = targX
  for sourceX in range(0,getWidth(source)):
    targetY = targY
    for sourceY in
      range(0,getHeight(source)):
        px=getPixel(source,sourceX,sourceY)
        tx=getPixel(target,targetX,targetY)
        setColor(tx,getColor(px))
        targetY=targetY + 1
      targetX=targetX + 1

def flipHorseSideways():
  # Set up the source and target pictures
  src = makePicture("horse.jpg")
  canvas = makeEmptyPicture(1000,1000)
  # Now, do the actual copying
  targetX = 0
  for sourceX in range(0,getWidth(src)):
    targetY = 0
    for sourceY in range(0,getHeight(src)):
      color = getColor(getPixel(src,sourceX,sourceY))
      # Change is here
      setColor(getPixel(canvas,targetY,targetX), color)
      targetY = targetY + 1
    targetX = targetX + 1
  show(canvas)
  return canvas
  
def rotateHorseSideways():
  # Set up the source and target pictures
  src = makePicture("horse.jpg")
  canvas = makeEmptyPicture(1000,1000)
  # Now, do the actual copying
  targetX = 0
  width = getWidth(src)
  for sourceX in range(0,getWidth(src)):
    targetY = 0
    for sourceY in range(0,getHeight(src)):
      color = getColor(getPixel(src,sourceX,sourceY))
      # Change is here
      setColor(getPixel(canvas,targetY,width - targetX - 1), color)
      targetY = targetY + 1
    targetX = targetX + 1
  show(canvas)
  return canvas


#CHROMAKEY

def chromakey(source):
  for px in getPixels(source):
    x=getX(px)
    y=getY(px)
    if(getGreen(px)+getBlue(px)<getRed(px)):
      setColor(px,makeColor(0,0,255))


#POSTERIZE
def posterize(picture):
  for px in getPixels(picture):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    if(red<64):
      setRed(px,31)
    if(red>53 and red<128):
      setRed(px,95)
    if(red>191 and red<256):
      setRed(px,223)
    if(green<64):
      setGreen(px,31)
    if(green>53 and green<128):
      setGreen(px,95)
    if(green>191 and green<256):
      setGreen(px,223)
    if(blue<64):
      setBlue(px,31)
    if(blue>53 and blue<128):
      setBlue(px,95)
    if(blue>191 and blue<256):
      setBlue(px,223)

#gray posterize      
def grayPosterize(picture):
  for px in getPixels(picture):
    r = getRed(px)
    g = getGreen(px)
    b = getBlue(px)
    luminance=(r+g+b)/3
    if luminance<64:
      setColor(px,black)
    if luminance>=64:
      setColor(px,white)

#sephia
def sephiaTint(picture):
  #convertimage to greyscale with
  #greyScaleNew(picture) <-- referencing an exiting program, need to write it for it to work
  for px in getPixels(picture):
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
#edge detection
def edge(source):
  for px in getPixels(source):
    x=getX(px)
    y=getY(px)
    if y<getHeight(source)-1 and x<getWidth(source)-1:
      sum=getRed(px)+getGreen(px)+getBlue(px)
      botrt=getPixel(source,x+1,y+1)
      sum2=getRed(botrt)+getGreen(botrt)+getBlue(botrt)
      diff=abs(sum2-sum)
      newcolor=makeColor(diff,diff,diff)
      setColor(px,newcolor)


#COLLAGES

def createCollage():
  flower1=makePicture(getMediaPath("flower1.jpg"))
  print flower1
  flower2=makePicture(getMediaPath("flower2.jpg"))
  print flower2
  canvas=makePicture(getMediaPath("640x480.jpg"))
  print canvas
  #First picture, at left edge
  targetX=0
  for sourceX in range(0,getWidth(flower1)):
    targetY=getHeight(canvas)-getHeight(flower1)-5
    for sourceY in range(0,getHeight(flower1)):
      px=getPixel(flower1,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  #Second picture, 100 pixels over
  targetX=100
  for sourceX in range(0,getWidth(flower2)):
    targetY=getHeight(canvas)-getHeight(flower2)-5
    for sourceY in range(0,getHeight(flower2)):
      px=getPixel(flower2,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
  targetX=targetX + 1
  negative(flower1)
  targetX=200
  for sourceX in range(0,getWidth(flower1)):
    targetY=getHeight(canvas)-getHeight(flower1)-5
    for sourceY in range(0,getHeight(flower1)):
      px=getPixel(flower1,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  #Fourth picture, flower2 with no blue
  clearBlue(flower2)
  targetX=300
  for sourceX in range(0,getWidth(flower2)):
    targetY=getHeight(canvas)-getHeight(flower2)-5
    for sourceY in range(0,getHeight(flower2)):
      px=getPixel(flower2,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  #Fifth picture, flower1, negated with decreased red
  decreaseRed(flower1)
  targetX=400
  for sourceX in range(0,getWidth(flower1)):
    targetY=getHeight(canvas)-getHeight(flower1)-5
    for sourceY in range(0,getHeight(flower1)):
      px=getPixel(flower1,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  show(canvas)
  return(canvas)

#Generalized code for collages next, don't call this code
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

#call this code
def createCollage2():
  flower1=makePicture(getMediaPath("flower1.jpg"))
  print flower1
  flower2=makePicture(getMediaPath("flower2.jpg"))
  print flower2
  canvas=makePicture(getMediaPath("640x480.jpg"))
  print canvas
  #First picture, at left edge
  copy(flower1,canvas,0,getHeight(canvas)- getHeight(flower1)-5)
  #Second picture, 100 pixels over
  copy(flower2,canvas,100,getHeight(canvas)- getHeight(flower2)-5)
  #Third picture, flower1 negated
  negative(flower1)
  copy(flower1,canvas,200,getHeight(canvas)- getHeight(flower1)-5)
  #Fourth picture, flower2 with no blue
  clearBlue(flower2)
  copy(flower2,canvas,300,getHeight(canvas)- getHeight(flower2)-5)
  #Fifth picture, flower1, negated with decreased red
  decreaseRed(flower1)
  copy(flower1,canvas,400,getHeight(canvas)- getHeight(flower2)-5)
  return canvas
  

def createCollage2():
  flower1=makePicture(getMediaPath("flower1.jpg"))
  print flower1
  flower2=makePicture(getMediaPath("flower2.jpg"))
  print flower2
  canvas=makePicture(getMediaPath("640x480.jpg"))
  print canvas
  #First picture, at left edge
  copy1(flower1,canvas,0,getHeight(canvas)- getHeight(flower1)-5)
  #Second picture, 100 pixels over
  copy1(flower2,canvas,100,getHeight(canvas)- getHeight(flower2)-5)
  #Third picture, flower1 negated
  negative(flower1)
  copy1(flower1,canvas,200,getHeight(canvas)- getHeight(flower1)-5)
  #Fourth picture, flower2 with no blue
  clearBlue(flower2)
  copy1(flower2,canvas,300,getHeight(canvas)- getHeight(flower2)-5)
  #Fifth picture, flower1, negated with decreased
  red
  decreaseRed(flower1)
  copy1(flower1,canvas,400,getHeight(canvas)- getHeight(flower2)-5)
  return canvas



#MISC
def section():
  pic = makeEmptyPicture(100,100)
  pixels = getPixels(picture)
  for i in range(0,len(pixels)/4):
    px = pixels[i]
    setColor(px,red)
  for i in range(3*(len(pixels)/4),len(pixels)):
    px = pixels[i]
    setColor(px,red)
  return pic

def moonColoredFlowers():
  #need to setMediaPath
  arch = makePicture("arch.jpg")
  moon = makePicture("moon-surface.jpg")
  for p in getPixels(arch):
    c = getColor(p)
    #Test
    #1 if distance(c,red)<200:
    #2 if getRed(p) > 100 and getBlue(p)+getGreen(p)<100:
    #3 if getRed(p) > 150 and getBlue(p)+getGreen(p)<200:
    #4 if getRed(p) > getBlue(p)+getGreen(p):
      x = getX(p)
      y = getY(p)
      moonpixel = getPixelAt(moon,x,y)
      mooncolor = getColor(moonpixel)
      setColor(p,mooncolor)
  return arch
  



def yellowbox1(picture):
  start=clock()
  for px in getPixels(picture):
    x=getX(px)
    y=getY(px)
    if 1- <= x <20 and 10<= y <20:
      setColor(px,yellow)
  print "Time:",clock()-start
  
def yellowbox2(picture):
  start=clock()
  for x in range(10,20):
    for y in rangge(10,20):
      setColor(getPixel(picture,x,y),yellow)
  print "Time:",clock()-start
