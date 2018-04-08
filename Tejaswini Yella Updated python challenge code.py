
#Main Function

# The final correctio_angle obtained should be rotated in anti-clockwise direction if 35.06963 degrees it means -35.06963 degrees if minus represent anti clockwise direction.

#Implemented test cases if rectangle is left tilted,if rectangle is right tilted,
#Implemented test cases if rectangle is 90 degrees to axis, if rectangle is straight with width parallel to x axis

def find_correction_angle(binary_image):

   #imported image and math libraries
   from PIL import Image
   import math

   #Opened the binary image
   im = Image.open(binary_image)

   #Accessed the pixel data of binary image and obtained the complete image pixels in list format
   pixels = list(im.getdata())
   width, height = im.size
   pixels = [pixels[i * width:(i + 1) * width] for i in range (height)]

   #Prepared a pixellist which has left boundary points of rectangular image
   pixelList=[]
   for i in range(0,len(pixels)):
     for j in range(0,len(pixels[i])):
        if pixels[i][j]!=0:
            pixelList.append([i,j])
            break



   #checking if the image is left tilted or right tilted or 90 degrees straight
   count1=0
   count2=0

   y1=pixelList[0][1]
   for i in range(0,len(pixelList)):
       if pixelList[i][1]<y1:
           y1=pixelList[i][1]
           count1=count1+1
       if pixelList[i][1]>y1:
           y1=pixelList[i][1]
           count2=count2+1


   # if the rectangle is left tilted or right tilted i.e 2nd half more than 1st half of boundary
   if count2>count1 or count1>count2:

       # initialized  the the x1 and y1
       y1=pixelList[0][1]
       x2=pixelList[0][0]

         #looping through the pixel list to find 1st point i.e min column and max row
       for i in range(0,len(pixelList)):
         if pixelList[i][1]<=y1:
           y1=pixelList[i][1]
           x1=pixelList[i][0]
        #looping through the pixel list to find 2nd point i.e the max row and the column value

         if pixelList[i][0]>=x2:
           x2=pixelList[i][0]
           y2=pixelList[i][1]


   #calculated the slope of the line
       m=(y2-y1)/(x2-x1)

   #correction angle in degrees
       correction_angle=math.degrees(math.atan(m))

       if count2>count1:

       #if the image is left tilted the obtained correction angle is the angle the image to be rotated anti-clockwise
         correction_angle=90-correction_angle

       if count1>count2:
       #if the image is right tilted the obtained correction angle is the angle the image to be rotated anti-clockwise
         correction_angle=180-correction_angle

   #if the rectangle is not tilted then checking whether width is parallel to x axis or y axis
   if count1==0 and count2==0:
     pixelList1=[]
     for i in range(0,len(pixels)):
       for j in range(0,len(pixels[i])):
        if pixels[i][j]!=0:
            pixelList1.append([i,j])
     c1=0
     c2=0
     x=pixelList[0][0]
     for i in range(0,len(pixelList1)):
         if pixelList1[i][0]==x:
            c1=c1+1

     for i in range(0,len(pixelList)):
       c2=c2+1


    # if width isparallel to y axis rotating 90 degrees
     if c2>c1 :
        correction_angle=90

    # if width is parallel to x axis no rotation is required
     if c1>c2:
        correction_angle=0



   return correction_angle









#calling function all my obtained degrees are rotated towards anti clockwise direction
   find_correction_angle('rotated.tif')
