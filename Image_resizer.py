
import cv2

source=input("Enter the image source directory or file name (ex. pixel.jpeg): ")
destination=input("Enter the destination file name and its type (ex. resized_pixel.jpeg): ")

image = cv2.imread(source,cv2.IMREAD_UNCHANGED) # cv2.IMREAD_UNCHANGED will be useful if jpg
if image.shape[0]==image.shape[1]:
    print(f"The height x width x channel is: {image.shape}") # channel is for color ex. RGB represented in number
    scale_percentage=int(input("Enter the percentage to which you want to reduce/increase: "))
    new_height, new_width = (int(image.shape[0]*scale_percentage/100),int(image.shape[1]*scale_percentage/100))

    resized = cv2.resize(image, (new_height, new_width))

    cv2.imshow(destination.split()[0], resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(destination, resized)
else: # if dimensions are not same ex. 800 x 600
    print(image.shape)
    heigth_scale_percentage,width_scale_percentage=input("Enter the percentage to which you want to reduce the 'height' and 'width' separated by ',': ").split(',')
    new_height, new_width = (int(image.shape[0]*int(heigth_scale_percentage)/100),int(image.shape[1]*int(width_scale_percentage)/100))

    resized = cv2.resize(image, (new_height, new_width))

    cv2.imshow(destination.split()[0], resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(destination, resized)