__author__ = 'redsphinx'
'''
make panel with live map and where the robot thinks it is


'''


from Tkinter import *
import numpy as np

#controller = MapControl()
FIELDWIDTH = 600  # measured in cm
FIELDHEIGHT = 400  # measured in cm
OFFSET = 25
alpha = 2  # offset of the drawn pixel
beta = 2  # size

'''

*** = OFFSET
        ....................................
        .                             *    .
        .           fieldWidth        *    .
        .     ------o--------o------- * * *.
        .  h |                       |     .
        .  e |                       |     .
        .  i |                       |     .
        .  g |                       |     .
        .  h |                       |     .
        .  t |_______________________|     .
        .    |                       |     .
'''

root = Tk()
#root.wm_title("[ALPHA] - Simultaneous Localization And Mapping")
#root.configure(bg='black')
#frame = Frame(root, bg='black', width=600, height=400)

'''
output is [output[0],output[1]]
output[0] are poses and they are of this format : [x,y,theta]
output[1] are landmark positions of this format : [x,y]                                                                                                                                                                                                                                                                                                                                                                                                  `    `
'''

class MapViewer(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("[ALPHA] - SLAM")
        self.pack(fill=BOTH, expand=1)
        self.updateMapNew([[[30, 30, 30]], [[20, 40, True], [50, 60, True], [300, 45, True], [60, 100, True]]])
        root.geometry("600x400")
        root.mainloop()
        pass




    # old method for updating the map
    def updateMap(self, output):  
        print output
        self.canvas = Canvas(self)
        self.canvas.create_rectangle(0, 0, FIELDWIDTH, FIELDHEIGHT, fill='#006400')
        self.canvas.pack(fill="both", expand=1)
        # create a pixel representing the robot
        self.drawAt(output[0], output[1], 'blue')
        #self.canvas.create_rectangle(output[0], output[1], output[0]+2, output[1]+2, fill='black')
        # create all the landmarks pixels
        for i in xrange(3, len(output), 2):
            self.drawAt(output[i], output[i+1], 'white')
            #self.canvas.create_rectangle(output[i], output[i + 1], output[i]+2, output[i + 1]+2, fill='red')

        #self.canvas.pack(fill="both", expand=1)
        pass
    
    '''
    output is [output[0],output[1]]
    output[0] are poses and they are of this format : [x,y,theta]
    output[1] are landmark positions of this format : [x,y]                                                                                                                                                                                                                                                                                                                                                                                                  `    `
    '''

    def updateMapNew(self, output):
        print output
        self.canvas = Canvas(self)
        self.canvas.create_rectangle(0, 0, FIELDWIDTH, FIELDHEIGHT, fill='#006400')
        self.canvas.pack(fill="both", expand=1)
        # create a pixel representing the robot
        poses = output[0]
        landmarks = output[1]
        for i in range(len(poses)):
            self.drawAt(poses[i][0], poses[i][1], poses[i][2], 'blue', 'robot')
            
        for k in range(len(landmarks)):
            print len(landmarks)
            if (landmarks[k][2] is True):
                self.drawAt(landmarks[k][0], landmarks[k][1], 'yellow')
            if (landmarks[k][2] is False):
                self.drawAt(landmarks[k][0], landmarks[k][1], 'white')
        
        pass
        

    def drawAt(self, x, y, theta, color, mode):
        if mode is 'robot':
             #TODO make triangle representing the robot and the direction it's facing using theta in radians and [-pi, pi]
            pass
        else:
            if (x - alpha > 0) and (x + alpha < FIELDWIDTH):
                if (y - alpha > 0) and (y + alpha < FIELDHEIGHT):
                    self.canvas.create_oval(x-alpha, y-alpha, x+2*alpha, y+2*alpha, fill=color)
                    #self.canvas.create_rectangle(x-2, y-2, x+5, y+5, fill=color)
                    self.canvas.pack(fill="both", expand=1)
                else:
                    print("please enter {0}>y>{1}".format(FIELDHEIGHT-2, 2))
            else:
                print("please enter {0}>x>{1}".format(FIELDWIDTH-2, 2))



        #test
mappie = MapViewer(root)
