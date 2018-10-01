# resize the image size 1280X720 to 640X360 for report show

import cv2

def resize(src, dst):
	img = cv2.imread(src)
	img_resize = cv2.resize(img, (640, 320))
	print("writing... >>", dst)
	cv2.imwrite(dst, img_resize)

if __name__ == "__main__":
	# resize("../output_images/undistort/test6.jpg", "../output_images/undistort/test6_resize.jpg") 
	# resize("../output_images/threshed/test6.jpg", "../output_images/threshed/test6_resize.jpg") 
	# resize("../output_images/wraped/test6.jpg", "../output_images/wraped/test6_resize.jpg") 
	resize("../output_images/test6.jpg", "../output_images/test6_resize.jpg") 
