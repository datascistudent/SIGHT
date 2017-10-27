import cv2
import numpy as np
import pytesseract
from PIL import Image
from PIL import ImageTk
import Tkinter
import sys
import os.path


class SIGHT:


    def __init__(self, image, knowledge_base):
        self.image = image
        self.knowledge_file = knowledge_base
        self.d = {}
        with open(self.knowledge_file) as f:
            for line in f:
                (key, val) = line.split('|')
                self.d[(key)] = val

    def ExtractTextFromImage(self):
        src_path = os.path.dirname(self.image)

        # Read image with opencv
        img = cv2.imread(self.image)

        # Convert to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply dilation and erosion to remove some noise
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        # Write image after removed noise
        cv2.imwrite(src_path + "/tmp/img_sans_noise.png", img)

        # Write the image after apply opencv to do some ...
        cv2.imwrite(src_path + "/tmp/img_w_improvization.png", img)

        # Recognize text with tesseract for python
        result = pytesseract.image_to_string(Image.open(src_path + "/tmp/img_w_improvization.png"))

        #print result
        return result

    def LookUp(self, quest):
        kb_dictionary = self.d
        ans = kb_dictionary.get(quest)
        return ans


    def popup(self, message):
        root = Tkinter.Tk()
        root.geometry('600x600')

        image = Image.open('/Users/gkannappan/PycharmProjects/SIGHT/BackGround.png')
        image = image.resize((400, 400))
        imageFinal = ImageTk.PhotoImage(image)
        #bg_img = '/Users/gkannappan/PycharmProjects/SIGHT/BackGround.png'
        theLabel = Tkinter.Label(root, image=imageFinal, text=message, compound=Tkinter.CENTER)
        theLabel.pack()
        theLabel.place(x = 100, y = 50)
        root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) == 0:
        sys.exit(-1)
    else:
        img = sys.argv[1]
        kb = sys.argv[2]

    s = SIGHT(image=img, knowledge_base=kb)
    res = s.ExtractTextFromImage()
    answer = s.LookUp(res)
    s.popup(answer)


