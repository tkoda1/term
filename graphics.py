from cmu_112_graphics import *
from cmu_112_graphics import *
import math
import copy
from string import ascii_lowercase

#this is essentially just the graphics layout. 
#if you drag and drop a resistor you can enter a resistance value so thats fun
def appStarted(app):
    app.mode = 'schemMode'
    app.rows = 8
    app.cols = 8
    app.margin = 6 
    app.message = ''
    app.resl = app.loadImage('Image 11-2-21 at 4.13 PM.jpg')
    #from https://www.electronics-notes.com/articles/analogue_circuits/circuits-symbols-diagrams/resistors-fixed-variable.php
    app.vs = app.loadImage('Image 11-2-21 at 4.31 PM.jpg')
    #from https://www.circuitbread.com/tutorials/voltage-and-current-sources-independent-and-dependent-sources
    app.vd = app.loadImage('Image 11-2-21 at 4.36 PM.jpg')
    #https://en.wikipedia.org/wiki/Voltage_divider
    app.resM = app.loadImage('Image 11-2-21 at 4.13 PM copy.jpg')
    
    app.resM = app.scaleImage(app.resM, 1/3)
    app.vs = app.scaleImage(app.vs, 2/3)
    app.res = app.scaleImage(app.resl, 1/3)
    app.gridWidth = app.width - 20*app.margin
    app.im = app.res
    app.vsBool = False
    app.vdBool = False
    app.press = False 
    app.resBool = False
    app.lineBool = False
    app.parB = True
    app.sm = False
    
    
    app.vsList = []
    app.imp = []
    app.curr = []
    app.c = []
    app.currL = []
    app.vdList = []
    app.resList = []   
    app.resDis = [] 
    app.pp = []
    app.cx2 = []
    app.resVals = []
    app.sortedList = [] 
    app.sortRes = []
    app.vdDis = []
    app.voltArc = []
    app.reStructure = []
    app.boardCor = []
    app.voltAcross = []
    app.b = False
    app.x = []
    app.y = 0
    app.Y = 0
    app.names = ["a","b","c","d","e","f","i","j","k","l","m","n","o","p","q"
    ,"r","s","t","u","v","w","dd","1","2","3","4","5","6","7","8","9","10","11"]
    app.g = Graph()
    boardCor(app)
    app.linep = []
    app.resDraw = []
    app.linePoint = []
    app.boardCor2 = []
    app.eqRes = ""
    app.board2 = app.loadImage('IMG_2048.jpg')
    #from https://pixabay.com/vectors/breadboard-arduino-technology-5659036/
    app.board2 = app.scaleImage(app.board2, 6/9)
    app.resI = app.loadImage('IMG_2052.jpg')
    #I drew
    app.resI = app.scaleImage(app.resI, 1/13)
    #IMG_2052 copy.jpg
    app.resR = app.loadImage('IMG_2052 copy.jpg')
    #I drew
    app.resR = app.scaleImage(app.resR, 1/15)
    app.marginH = 264
    app.marginW = 123
    app.colorList2 = []
    app.colorList = []
    app.rows2 = 5
    app.cols2 = 30
    app.ha = []
    app.v = []
    app.how = []
    app.new = []
    app.long =0

    app.count = 0
    app.G =Graph2()
    app.r = Resistor()
    app.resL = []
    boardCor(app)
    
    
    #app.count += 1
    getColor(app)

def schemMode_keyPressed(app, event):
    if(event.key == "p"):
        if(app.im == app.res):
            app.im = app.resM
        else:
            app.im = app.res
        

def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  =  app.width - 40*app.margin
    gridHeight = app.height - 10*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
#from http://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
    return (x0, y0, x1, y1)
def schemMode_mousePressed(app, event):
    # canvas.create_rectangle(875,  554, 775, 606, fill="pink", width=5)
    
    pointInGrid(app, event.x, event.y)
   
    
    if(app.lineBool == True):
        m = closestBoard(app, event.x, event.y)
        app.linep.append(m)
        if(len(app.linep) == 2):
            g = (app.linep)
            app.linePoint.append(g)
            app.linep = []
       
    #875,  54, 775, 106
    if((775 <= event.x <= 875) and (54 <= event.y <= 106)):
        try:
            app.b = True
            app.vsBool = False
            app.vdBool = False
            app.resBool = False
            app.lineBool = False
            app.g.isPar()
            app.g.isSolve()
            app.g.sorting()
            c = app.g.solving()
            app.eqRes = c
           
            f = app.g.makeMatrix()
            
            app.curr = define(app)
            currNodeL(app)
            voltAcross(app)
            isParTot(app)
          
            app.b = False
        except:
            app.showMessage('Try entering a smaller board this program cannot solve this one')
            appStarted(app)
    #875,  654, 775, 706
    if((775 <= event.x <= 875) and (654 <= event.y <= 706)):
        app.b = True
        app.vsBool = False
        app.vdBool = False
        app.resBool = False
        app.lineBool = False
        app.press = False
        app.g.isPar()
        app.g.isSolve()
        app.g.sorting()
        c = app.g.solving()
        app.eqRes = c
        
        f = app.g.makeMatrix()
        
        app.curr = define(app)
        currNodeL(app)
        voltAcross(app)
        isParTot(app)
        
        app.b = False
        app.mode = 'boardMode'
        app.cx2 = copy.deepcopy(app.imp)
        boardMode_getColor(app)
    

       
    #875,  154, 775, 206
    # canvas.create_rectangle(875,  554, 775, 606, fill="pink", width=5)
    if(( 775<= event.x <= 875 ) and (154<event.y<206)):
        app.vsBool = False
        app.vdBool = False
        app.resBool  = False
        app.lineBool = True
    if(( 775<= event.x <= 875 ) and (554<event.y<606)):
        app.resBool = False
        if(app.im == app.res):
            app.im = app.resM
        else:
            app.im = app.res

def longest(app):
    print("ahhaha",app.cx2)
    for i in app.cx2:
        if len(i) > app.long:
            app.long = len(i)

          
def pointInGrid(app, x, y):
    
    # return True if (x, y) is inside the grid defined by app.
    if(((app.gridWidth +30 <= x <= app.gridWidth + app.margin + 
    app.vs.width+30) and (400 - app.vs.height <= y <= 400 + app.vs.height)) == True):
        app.vsBool = True
        app.vdBool = False
        app.resBool = False
        app.lineBool = False
    
    if(((781  <= x <= 853) and (269 <= y <= 317)) == True):
       
        app.vsBool = False
        app.vdBool = False
        app.resBool = True
        app.lineBool = False
    
    
def schemMode_mouseDragged(app, event):
    
    #app.x = event.x
    app.y = event.y

def closestBoard(app,x,y):
    smallestDis = 10000
    point = []
    for row in app.boardCor:
        for col in app.boardCor[0]:
            c = (row)
            m = (x,y)
            n = distance(c,m)
            if(n < smallestDis):
                smallestDis = n
                point = c
    return point


def schemMode_mouseReleased(app, event):
    #pointInGrid(app, event.x, event.y)
    m = closestBoard(app, event.x, event.y)
    #app.x = event.x
    app.y = event.y
    if(app.vsBool == True):
        app.vsList.append(m)
        #Have this be the rows and cols?
        app.g.add_vertex(f"voltage{m}",m,0)
        app.names.pop(0)
    elif(app.vdBool == True):
        app.vdList.append(m)
    elif(app.resBool == True):
        name = app.getUserInput('Resistance Value')
 
        if (name == None):
            app.message = 'You canceled!'
        
        else:
            r = (m[0] - 35,m[1],name)
        
            if(app.im == app.res):
                q = (m[0] - 35,m[1],app.im)
                r = (m[0] - 35,m[1],name)
            else:
                q = (m[0]+10,m[1]+45,app.im)
                r = (m[0]-15,m[1]+30,name)
            app.resList.append(r)
        
            app.resDraw.append(q)
            app.g.add_vertex(f'resistor{m}',m,int(name))
            app.names.pop()    
            
            if(len(app.vsList) > 1):
                orderRes(app)
        

            for v in app.g:
                vid = v.get_id()
                p = v.get_position()
                w = v.get_weightL()
                    
                

def orderRes(app):
    if(len(app.vsList) > 0):
        ref = app.vsList[1]
        for i in app.resList:
            
            m = ((i[0] - ref[0]),i[2])
            app.resDis.append(m)
    if(len(app.vsList) > 0):
        ref = app.vsList[1]
        for k in app.vdList:
            o = ((k[0] - ref[0]),'voltageDivider')
            app.vdDis.append(o)
    
def boardCor(app):  
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            r = (x0,y0)
            app.boardCor.append(r)
def restructRes(app):
    app.resList
    app.reStructure 
    return 42
def isParTot(app):
    
    build = app.g.getBuild()
   
 
    app.imp = resBoardL(build)
    app.parB == True
    for i in range(len(build)):
        
        if(len(build[i]) != 1):
            app.parB = False
    if(app.parB == True):
        app.voltArc = [app.voltArc[0]]
      


def resBoardL(L):
    newL = []
    for r in range(len(L)):
        temp = []
        for c in range(len(L[r])):
            temp.append(L[r][c][1])
        newL.append(temp)
    
    return(newL)



def schemMode_redrawAll(app, canvas):
    try:
        canvas.create_rectangle(875,  54, 775, 106, fill="pink", width=5)
        canvas.create_rectangle(875,  154, 775, 206, fill="pink", width=5)
        canvas.create_rectangle(875,  654, 775, 706, fill="pink", width=5)
        canvas.create_rectangle(875,  554, 775, 606, fill="pink", width=5)
        canvas.create_text(825,80, text = "Solve")
        
        canvas.create_text(400,23, text = "to start drag and place in a Voltage sorce of 5V and then place resistors to the right")
        canvas.create_text(400,10, text = "to rotate first click rotate button then re-drag resistor")
        canvas.create_text(400,34, text = "ensure no two resistors share the same node")
        canvas.create_text(400,46, text = "'v' to clear")
        canvas.create_text(825,180, text = "Wire")
        canvas.create_text(825,680, text = "Bread Board")
        canvas.create_text(825,580, text = "Rotate resisor")
        canvas.create_text(755, 752, text = app.eqRes)
        if(len(app.linePoint) > 0):
            for l in app.linePoint: 
                canvas.create_line(l[0][0],l[0][1],l[1][0],l[1][1],width = 4)
        
        for row in range(app.rows):
            for col in range(app.cols):
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_oval(x1+5, y1+5, x1-5, y1-5, fill='pink')
        for i in app.vsList:
            canvas.create_image(i[0],i[1], image=ImageTk.PhotoImage(app.vs))
            

        #for k in app.vdList:
            #canvas.create_image(k[0],k[1], image=ImageTk.PhotoImage(app.vd))
        for a in app.resDraw:
            canvas.create_image(a[0]-5,a[1], image = ImageTk.PhotoImage(a[2]))
        
        for j in range(len(app.resList)):    
         
            font = 'Arial 11 bold'
            
            canvas.create_text(app.resList[j][0],  app.resList[j][1] + app.margin*3, text=app.resList[j][2], font=font)
            if(len(app.voltArc) > 0):
                
                
                    r = app.pp
              
                    if((j > len(app.voltArc) - 1) and len(app.voltArc) > 2):
                 
                        c = app.currL[-1]*int(app.resList[-1][2])
                        
                        canvas.create_text(r[j][0][0]- app.margin*4,  r[j][0][1] + app.margin*6  , text=f'v:{round(c,3)}', font=font)
                    elif(len(app.voltArc) < 2):
                        c = app.currL[-1]*int(app.resList[j][2])
                        if(r[j][0][1] == app.Y):
                            canvas.create_text(r[j][0][0]- app.margin*4,  r[j][0][1] + app.margin*6  , text=f'v:{-round(c,3)}', font=font)
                        else:
                            canvas.create_text(r[j][0][0]- app.margin*4,  r[j][0][1] + app.margin*6  , text=f'v:{round(c,3)}', font=font)
                    else:
                        
                        if(r[j][0][1] == app.Y):

                            c = app.currL[-1]*int(app.resList[j][2])
                            canvas.create_text(r[j][0][0]- app.margin*4,  r[j][0][1] + app.margin*6 , text=f'v:{-round(app.voltArc[j],3)}', font=font)
                        else:
                         
                            canvas.create_text(r[j][0][0]- app.margin*4,  r[j][0][1] + app.margin*6 , text=f'v:{round(app.voltArc[j],3)}', font=font)
            
        c = 0        
        low = 0
        if(app.press == True):
          
            for row in range(2,app.rows):
          
                for col in range(1,app.cols):
                   
                    if(col <= (len(app.cx2)+1)):
                       
                   
                        (x0, y0, x1, y1) = getCellBounds(app, row, col+1)
                        (x02, y02, x12, y12) = getCellBounds(app, 3+app.long,2)
                        if((col > 1) and (row <= len(app.cx2[col-2])+1)):
                            
                            if(row ==2):
                                c += (x1-x0)
                                canvas.create_line(x0,y1,x1,y1,width = 4)
                                canvas.create_image(x1-3,y1, image = ImageTk.PhotoImage(app.res),anchor = "e")
                                if(app.long ==1):
                                    (x03, y03, x13, y13) = getCellBounds(app, 4+app.long,2)
                                    canvas.create_line(x1,y1,x1,y03,width = 4)
                            else:
                                
                                canvas.create_line(x1,y0,x1,y02,width = 4)
                                canvas.create_line(x1,y1,x1,y1+(y1-y0),width = 4)
                                canvas.create_image(x1+5,y1+5, image = ImageTk.PhotoImage(app.resM),anchor = "n")
                                
                                #canvas.create_oval(x1+5, y1+5, x1-5, y1-5, fill='blue')
                        elif((row == 3) and (col == 1)):
                            canvas.create_line(x1,y0,x1,y02,width = 4)
                            canvas.create_line(x1,y1,x1,y1+(y1-y0),width = 4)
                            canvas.create_image(x1,y1, image=ImageTk.PhotoImage(app.vs))
            if(app.long < 2):
                (x0, y0, x1, y1) = getCellBounds(app, 4+app.long,2)
                canvas.create_line(x1,y0,x0+c+(x1-x0),y0,width = 4) 
            else: 
                (x0, y0, x1, y1) = getCellBounds(app, 3+app.long,2)
                canvas.create_line(x1,y0,x0+c+(x1-x0),y0,width = 4)                

        #canvas.create_rectangle(app.gridWidth,300 - app.vs.height,app.gridWidth + app.margin + 
        #app.vs.width,300 + app.vs.height)
        canvas.create_image((app.gridWidth + app.margin)+30, 300, image=ImageTk.PhotoImage(app.res))
        canvas.create_image((app.gridWidth + app.margin)+30, 400, image=ImageTk.PhotoImage(app.vs))
        #canvas.create_image((app.gridWidth + app.margin), 400, image=ImageTk.PhotoImage(app.vd))
        #canvas.create_rectangle(app.gridWidth + app.margin-20,200,app.gridWidth + app.margin + 40,120)
    
    except:
        font = 'Arial 20 bold'
        print("Try entering a different board this program cannot solve this one,press 'v' to clear")
        canvas.create_text(app.width//2,app.height//2, text = "Try entering a different board this program cannot solve this one,press 'v' to clear",font = font)
        
        
   
def newL2(app):
    if(app.press == True):
        count2 = 0
        for col in range(2,app.cols):
            count = -1
            for row in range(1,app.rows):
                
                if(col <= (len(app.cx2)+1)):
                    
                    (x0, y0, x1, y1) = getCellBounds(app, row, col+1)
        
                    if((col > 1) and (row <= len(app.cx2[count2]))):
                        print(count,len(app.cx2[count2]),row)
                        if(count == len(app.cx2[count2])-1):
                            print("h")
                            p = (x1-30,y1+230,app.cx2[count2][count])
                            app.resList.append(p)
                            count +=1
                            continue
                        elif(row == 2):
                            m = (x1-30,y1-60,app.cx2[count2][count])
                            app.resList.append(m)
                            count +=1
                            continue
                        
                        else:
                            p = (x1+40,y1+200,app.cx2[count2][count])
                            app.resList.append(p)
                            count +=1
                            continue
            count2+=1
       
                        
def schemMode_keyPressed(app, event):
    distanceList = []
  
    if (event.key == "Left"):  
        if(len(app.vsList) > 1):
            
            for i in app.resDis:
                e = (int(i[0]),int(i[1]))
                
                w = e
              
                distanceList.append(w)
            for i in app.vdDis:
                e = (int(i[0]),'voltageDivider')
               
                w = e
               
                distanceList.append(w)
            
            app.sortedList = more(app,distanceList,app.resList,app.vsList[1],app.vdList)

            #("hhhhhhhhhhhhh",app.sortedList)
        h =[]
        for i in app.sortedList:
            if i not in h:
                if( i[2] != 'voltageDivider'):
                    h.append(int(i[2]))
                    app.sortRes.append(int(i[2]))
                else:
                    h.append(i[2])
                    app.sortRes.append(i[2])
     

    if (event.key == "Right"):  
        
        ep = circuit(app.sortRes)
        
    if(event.key == "s"):
        app.g.isPar()
        app.g.isSolve()
        app.g.sorting()
        c = app.g.solving()
        app.eqRes = c
     
        f = app.g.makeMatrix()
        
    if(event.key == "p"):
        
        if(app.im == app.res):
            app.im = app.resM
        else:
            app.im = app.res
       

    if(event.key == "t"):
        print(app.g)
    if(event.key == "d"):
        #fix this 
        app.curr = define(app)
        currNodeL(app)
        voltAcross(app)
        isParTot(app)
       
    if(event.key == "v"):
        appStarted(app)
    if (event.key == 'h'):
        app.mode = 'boardMode'
        boardMode_getColor(app)
        boardMode_boardCor(app)
def boardMode_getColor(app):
    for r in range(len(app.imp)):
        m = []
        for c in range(len(app.imp[r])):
            m.append(boardMode_resColor(app,app.imp[r][c]))
        h = m
        app.colorList.append(h)
def boardMode_resColor(app,res):
    color = Resistor()
    colors = Resistor.res(color,res)
    return colors
def currNodeL(app):
    app.currL = []
    if(len(app.curr) > 0):
        #fix this 
        for i in range(len(app.curr)-1):
          
            app.currL.append(app.curr[i][0])
            app.currL.append(((app.curr[i][0])-(app.curr[i+1][0])))
        app.currL.append(app.curr[-1][0])
    else:
        app.currL = app.curr


        
def voltAcross(app):
    build = app.g.getBuild()
    build.reverse()
    app.voltArc =[]
    pp = app.g.voltListing(build)
    y = app.g.getTopY(pp)
    app.Y = y
    app.pp = pp
    j =-1
    
    for i in range(len(pp)):
        if((i < (len(app.currL) -1)) and(pp[i][0][1] != y) or (pp[i][0][1] == y)):
            j += 1
        else:
            break
        
        m = (app.currL[j] * pp[i][1])
        app.voltArc.append(m)
    
    #self.bestY


def currAcross(app):
    return app.currL      
 

def distance(p1,p2):
    
    return math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )

def getMax(p):
    i = 0
    m = 0
    g = 0
    bestIndex = 0
    for i in range(len(p)):
       
        if(p[i][0] > m):
            m = p[i][0]
            g = p[i]
            bestIndex = i 
    return (g,bestIndex)

def sort(a):
    r = copy.deepcopy(a)
    k = []
    s = []
    while len(r) > 0:
        k = getMax(r)
        s.append(k[0])
        r.pop(k[1])
    return s

def makeTheList(a,m):
   
    newL = []
    for l in m:
        newL.append(l)
    return newL

def more(app,a,m,y,vdList):
    
    for i in range(len(vdList)):
        r = (vdList[i][0],vdList[i][1],'voltageDivider')
        vdList[i] = r
    
    L = []
    m = m + vdList
    
    L = makeTheList(a,m)
    
    top = []
    g = []
    bottom = []
    for k in range(len(L)):
        
        if(L[k][0] > y[1]):
            top.append(L[k])
        else:
            bottom.append(L[k])
    top = sort(top)
    
    bottom = sort(bottom)
    
    top = top[::-1]
    g = top + bottom
    return g    
   
def seriesSumRes(seriesList):
    
    sum = 0
    for i in range(len(seriesList)):
        sum += seriesList[i]
    return sum
def sumParRes(parList):
    
    sum = 0
    for i in range(len(parList)):
        sum += (1/(parList[i]))
    sum = (1/sum)
    return sum
# voltage divider begining and end 
def voltageDivider(L):

    #not actually final step before 
    fin = []
    result = 0
    a = 0
    for r in range(len(L)):
        a = 0
        i = -1
        if("voltageDivider" not in L[r]):
            fin.append(seriesSumRes(L[r]))
        else:
            while((i < len(L[r]))):
                if(type(L[r][i]) == int):
                    a = L[r][i]
                i += 1
                parList = []
                #there is a voltage divider adds it 
                if((i < len(L[r])) and (L[r][i] == "voltageDivider")):
                    i +=1 
                    while((i < len(L[r]) and L[r][i] != "voltageDivider")):
                        parList = L[r][i]
                        if(type(parList) != list):
                            fin.append(parList)
                        else: 
                            fin.append(voltageDivider(parList)) 
                        i +=1
            fin[r] += a
  
    result = sumParRes(fin)
    return result 
def circuit(L):
    result = []
    r = 0
    for r in range(len(L)):
        i = 0
        voltL = []
        if((L[r] != "voltageDivider")and type(L[r]) == int):
                    result.append(L[r])
        while(i < len(L)):
            if((r < len(L)) and (L[r] == "voltageDivider")):
                r +=1 
                voltL = L[r]
                if(type(voltL) == list):
                    result.append(voltageDivider(voltL))
            i += 1
    r = seriesSumRes(result)
    return r







class Vertex:
    def __init__(self, node,rowCol,weight):
        self.id = node
        self.weight = weight
        self.rowCol = rowCol
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id
    def __repr__(self):
        return f'{self}'
    def get_weightL(self):
        return self.weight

    def get_position(self):
        return self.rowCol

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]





class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.positions = []
        self.s = set()
        self.build = []
        self.solve = False
        self.isParBool = False
        self.best = 0
        self.a = 0
        self.b = 0
    def getA(self):
       
        return self.a
    def getB(self):
        
        return self.b
    
    def __repr__(self):
        return f'{self.vert_dict,self.build}'
    
       
    
    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, rowCol,weight):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node,rowCol,weight)
        self.positions.append(rowCol)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
    
    def get_vertices(self):
        return self.vert_dict.keys()

    #rename something like x list
    def sorting(self):
        self.build = []
        q = []
        for key in self.vert_dict:
            self.s.add(self.vert_dict[key].get_position()[0])
        q = list(self.s)
        q = sorted(q)
        for i in range(len(self.s)):
            if(len(self.build) != len(q)):
                self.build.append([])
        
        for i in range(len(q)):
            
            for key in self.vert_dict:
                
                if(self.vert_dict[key].get_position()[0] == q[i]):
                    m = (self.vert_dict[key].get_position(),self.vert_dict[key].get_weightL())
                    self.build[i].append(m)
        self.build.reverse()
        
        

    def isPar(self):
        self.isParBool = True
    def isSolve(self):
        self.solve = True
    def solving(self):
        if(self.solve == True):
            if(self.isParBool == True):
                total = 0
                total += self.firstSum(self.build[0])
                for i in range(1,len(self.build)-1):
                   
                    
                    if((total>0) and (self.summing(self.build[i]) > 0)):
                        c = (1/self.summing(self.build[i]) + (1/total))
                        total = (1/c)
                      
                        total += self.addTopY(self.build[i])
                        
                total += self.build[-1][0][1]
             
                return total
    def getTopY(self,L):
        self.bestY()
        best = 9999
        for i in L:
            if(i[0][1] < best):
                best = i[0][1]
        return best
    def voltListing(self,L):
        y = self.getTopY(L)
        nL = []
        for i in range(len(L)):
            for r in range(len(L[i])):
                nL.append(L[i][r])
  
        return nL

    def addTopY(self,L):
        best = 9999
        self.bestY()
        bestl = self.getTopY(L)
        bestY = 0
        for i in L:
            
            if(i[0][1] < best):
                best = i[0][1]
               
                bestY = i[1]
       
        if(bestl != self.best):
            bestY = 0
        return bestY
    def bestY(self):
        best = 9999
        
        for i in range(len(self.build)):
            for j in range(len(self.build[i])):
                if(self.build[i][j][0][1] < best): 
                    
                    best = self.build[i][j][0][1]
        
        self.best = best
    def firstSum(self,L):
        sum = 0
        for i in L:
            sum += i[1]
        return sum
    def summing(self,L):
        self.bestY()
        best = self.getTopY(L)
       
       
        sum = 0
        for i in L:
            if(best == self.best):
                if i[0][1] != best:
                    sum += i[1]
            else:
                sum += i[1]
      
        return sum 
    def adding(self,L,o):
        
        sum = 0
        for i in range(len(L)):
            sum += L[i][1]
        sum += o
        
        return sum

    def makeMatrix(self):
        tDog = self.build
       
        tDog.reverse()
        
        
        tDog.reverse()

        tDog.pop()
        
       
        
        a = []
        for i in range(len(tDog)):
            a.append([])
        print("howdy",tDog,a)
        for r in range(len(tDog)): 
            print(a[r])
            print((tDog[r]))
            if(r >0):
                a[r].append(a[r-1][-1])
            if(r + 1 < len(tDog)):
                
                a[r].append(self.adding(tDog[r],tDog[r+1][-1][1]))
                a[r].append(-(tDog[r+1][-1][1]))
                
            else:
                a[r].append(self.adding(tDog[r],0))
        for r in a:
            r = r.reverse()   
        b = [[5]]
        for i in range(len(a) - 1):
            b.append([0])
        for k in a:
            if len(k) < len(a):
                k.insert(1,0)
        self.a = a 
        self.b = b

        print("hahhaa",self.a,self.b,a.reverse())
    def getBuild(self):
        return self.build
                




#All the code for setting up the graph comes from this sorce
#https://python-course.eu/applications-python/graphs-python.php
            
def print_matrix(Title, M):
    
    for row in M:
        print([x+0 for x in row])
        
def print_matrices(Action, Title1, M1, Title2, M2):
    
    print(Title1, '\t'*int(len(M1)/2)+"\t"*len(M1), Title2)
    for i in range(len(M1)):
        row1 = ['{0:+7.3f}'.format(x) for x in M1[i]]
        print('{0:+7.3f}'.format(x) for x in M1[i])
        row2 = ['{0:+7.3f}'.format(x) for x in M2[i]]
        print(row1,'\t', row2)
        
       
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')
        sys.exit()

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C
def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])
def define(app):
    m = 0
    k = app.g.getA()
    negIndex = -1 
    zeroInd = -1
    bestLen = 0
    for j in range(len(k)):
        if(len(k[j]) > bestLen):
            bestLen = len(k[j])
    for t in k:
        while(len(t) != bestLen):
            t.append(0)


    for r in range(len(k)):
        for c in range(len(k[r])):
            print(r,k,negIndex,zeroInd)
            if(k[r][c] < 0):
                negIndex = c
            if(k[r][c]== 0):
                zeroInd = c
            if(((negIndex) >= 0) and (zeroInd >= 0)):
                swap(k[r], negIndex, zeroInd)
                negIndex = -1 
                zeroInd = -1
            
    B = app.g.getB()
    print("howdy",k,B)
   
    A = k
    #A = [[5.,3.,1.],[3.,9.,4.],[1.,3.,5.]]
    #B = [[9.0],[16.0],[9.0]]


    AM = copy_matrix(A)
    n = len(A)
    BM = copy_matrix(B)

    print_matrices('Starting Matrices are:', 'AM Matrix', AM, 
               'IM Matrix', BM)
    print()

    indices = list(range(n)) # allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
        BM[fd][0] *= fdScaler
        
        # Section to print out current actions:
        string1  = '\nUsing the matrices above, '
        string1 += 'Scale row-{} of AM and BM by '
        string2  = 'diagonal element {} of AM, '
        string2 += 'which is 1/{:+.3f}.\n'
        stringsum = string1 + string2
        val1 = fd+1; val2 = fd+1
        Action = stringsum.format(val1,val2,round(1./fdScaler,3))
        #print_matrices(Action, 'AM Matrix', AM, 'BM Matrix', BM)
        print()
        
        # SECOND: operate on all rows except fd row.
        for i in indices[0:fd] + indices[fd+1:]: # *** skip fd row.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): # cr - crScaler*fdRow.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            BM[i][0] = BM[i][0] - crScaler * BM[fd][0]
            
            # Section to print out current actions:
            string1  = 'Using matrices above, subtract {:+.3f} *'
            string1 += 'row-{} of AM from row-{} of AM, and '
            string2 = 'subtract {:+.3f} * row-{} of BM '
            string2 += 'from row-{} of BM\n'
            val1 = i+1; val2 = fd+1
            stringsum = string1 + string2
        
            Action = stringsum.format(crScaler, val2, val1, 
                                    crScaler, val2, val1)
            print_matrices(Action, 'AM Matrix', AM, 
                                'BM Matrix', BM)
           
            m = BM
        m = BM
    return m

#from https://integratedmlai.com/system-of-equations-solution/

    #def solving(self):
    
class Resistor2(object):
    def __init__(self,resistance):
        self.resistance = resistance
        
    def __repr__(self):
        return f'{self.resistance}'  





##########################################
# BreadBoard Mode
##########################################



#596
#x,(144,250,356,462,568,673) y,(347)
#(228,369) 84


   
    

def boardMode_drawImageWithSizeBelowIt(app, canvas, image, cx, cy):
    canvas.create_image(cx, cy, image=ImageTk.PhotoImage(image))
    
def boardMode_mousePressed(app, event):
    
    return 42

  
    
   

def boardMode_getCellBounds(app, row, col):
    # aka 'modelToView'
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = 636
    gridHeight = 101
    x0 =  gridWidth * col / app.cols2
    x1 = gridWidth * (col+1) / app.cols2
    y0 =  gridHeight * row / app.rows2
    y1 =  gridHeight * (row+1) / app.rows2
    return (x0, y0, x1, y1)

def boardMode_getColor(app):
    for r in range(len(app.imp)):
        m = []
        for c in range(len(app.imp[r])):
            m.append(boardMode_resColor(app,app.imp[r][c]))
        h = m
        print(h)
        app.colorList.append(h)
    #print(app.colorList)

jDog = [144,250,356,462,568,673]
ground = [156,175,197,218,240,282,303,324,345,366,409,430,
451,473,494,537,557,579,599,620,662,684,705]

def boardMode_redrawAll(app, canvas):
    canvas.create_rectangle(875,  54, 775, 106, fill="pink", width=5)
    canvas.create_rectangle(675,  54, 575, 106, fill="pink", width=5)
    
    
    
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.board2))
    canvas.create_line(154, 200, 142 , 284, fill='red', width=3)
    canvas.create_line(747, 223, 748 , 595, fill='black', width=3)

    #drawImageWithSizeBelowIt(app, canvas, app.resR, app.width//4, app.height//4)

    #drawImageWithSizeBelowIt(app, canvas, app.image2, 500, 300)
    #canvas.create_image(450,400, image=ImageTk.PhotoImage(app.board))
   
    #for row in range(app.rows):
        #for col in range(app.cols):
            #(x0, y0, x1, y1) = getCellBounds(app, row, col)
            #canvas.create_oval(app.marginW + x1+2,app.marginH +y1+2,app.marginW + x1-2, app.marginH +y1-2, fill='red')
            #canvas.create_oval(app.marginW + x1+2,147+app.marginH +y1+2,app.marginW + x1-2,147+app.marginH +y1-2, fill='red')
    #canvas.create_oval(app.marginW + 3,app.marginH +3,app.marginW -3, app.marginH -3, fill='blue')
    add = 1
    for i in range(len(app.imp)):
        jDog = [144,250,356,462,568,673]
        ground = [156,175,197,218,240,282,303,324,345,366,409,430,
        451,473,494,537,557,579,599,620,662,684,705]
        if(len(app.resL) > 0):
            for p in range(len(app.resL)):
                #print(app.resL)

                canvas.create_image(app.resL[p][0],app.resL[p][1], image=ImageTk.PhotoImage(app.resI),anchor="w")
                canvas.create_line(app.resL[p][0] +27 , app.resL[p][1]-8, app.resL[p][0]+27, app.resL[p][1] +10, fill=app.colorList2[p][-1][0], width=3)
                canvas.create_line(app.resL[p][0] +34, app.resL[p][1]-6, app.resL[p][0] +34, app.resL[p][1]+7, fill=app.colorList2[p][-1][1], width=3)
                canvas.create_line(app.resL[p][0] +39, app.resL[p][1]-6, app.resL[p][0] +39, app.resL[p][1]+7, fill=app.colorList2[p][-1][2], width=3)
        for row in range(app.rows2-1):
            for col in range(app.cols2-1):
                (x0, y0, x1, y1) = boardMode_getCellBounds(app, row, col)
        
                
        canvas.create_image(jDog[i],357, image=ImageTk.PhotoImage(app.resI),anchor="sw")
        canvas.create_line(jDog[i] + 27, 356, jDog[i] + 27, 338, fill=app.colorList[i][0][0], width=3)
        canvas.create_line(jDog[i] + 34, 354, jDog[i] + 34, 341, fill=app.colorList[i][0][1], width=3)
        canvas.create_line(jDog[i] + 39, 354, jDog[i] + 39, 341, fill=app.colorList[i][0][2], width=3)
        if(i < len(app.imp) - 1):
            canvas.create_line(jDog[i] + 84, 323, jDog[i] + 108, 323, fill='green', width=3)
        if(len(app.imp[i]) > 1):
            canvas.create_image(jDog[i] + 84,369, image=ImageTk.PhotoImage(app.resR),anchor="n")
            canvas.create_line(jDog[i] + 76, 391, jDog[i] + 92,391, fill=app.colorList[i][1][0], width=3)
            canvas.create_line(jDog[i] + 78, 399, jDog[i] + 89, 399, fill=app.colorList[i][1][1], width=3)
            canvas.create_line(jDog[i] + 78, 405, jDog[i] + 89, 405, fill=app.colorList[i][1][2], width=3)
            #canvas.create_line(jDog[i]+ 84,513,boardMode_closestGround(jDog[i]+ 77),595,width = 3)

        if(len(app.imp[i]) > 2):
            add = jDog[i] + 84
            y = 463
            p = []
    
            for l in range(2,len(app.imp[i])):
                canvas.create_image(add,y, image=ImageTk.PhotoImage(app.resI),anchor="sw")
                canvas.create_line(add + 27, y -1, add + 27, y - 18, fill=app.colorList[i][l][0], width=3)
                canvas.create_line(add + 34, y -3, add + 34, y- 16, fill=app.colorList[i][l][1], width=3)
                canvas.create_line(add + 39, y -3, add + 39, y -16, fill=app.colorList[i][l][2], width=3)
                add += 86
                y += 19
                p.append(add)
            if(len(p)>0):
                print(p)
                canvas.create_line(p[-1] -2,513,boardMode_closestGround(p[-1]),595,width = 3)
def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'
#from https://www.cs.cmu.edu/~112/notes/notes-graphics.html#customColors
def boardMode_closestGround(x): 
    smallDis = 99999
    bestG = 0
    for i in range(len(ground)): 
        if(abs(ground[i] - x) < smallDis):
            bestG = ground[i]  
            smallDis = abs(ground[i] - x)   
    return bestG   
def ohms(totalResistors):
    return 42

class Resistor(object):
    def __init__(self):
        r = 0
   
    
    def bandColors(tempResistance,digits):
        print(tempResistance,digits)
        colors = ["black","brown","red","orange","yellow","green","blue",rgbString(223,7,247)
        ,"grey","white","gold","silver"]
        bandOne = colors[(tempResistance%10)]
        bandTwo = colors[(tempResistance//10)]
        bandThree = colors[digits]
        return (bandTwo,bandOne,bandThree)
    
    
   
    def res(self,resistance):
        word = ""
        totalResistors = []
        resList = []
        while word != None:
            s = resistance
            
            right = s
            word = "hi"
            resistance = int(right)
            
            tempResistance = copy.copy(resistance)
            digits = 0
            resList.append(int(right))
            while tempResistance > 99:
                digits += 1
                print(digits)
                tempResistance //=10
            bands = Resistor.bandColors(tempResistance,digits)
            
           
            #newResistor = resistor.resi(bands[0], bands[1], bands[2], resistance,word)
           
            return bands
               





def boardMode_mouseReleased(app, event):
    if(app.sm == True):
        name = app.getUserInput('Resistance')
        if (name == None):
            app.message = 'You canceled!'
        else:
            app.showMessage('You entered: ' + name)
            app.ha.extend([int(name)])
            app.v.append(app.ha)
            #print(app.x)
            m = boardMode_closestCell(app,event.x,event.y)
            #print("sup",m)
            #print(app.resL)
            app.resL.append(m)
            getColor(app)
def boardMode_closestCell(app,x,y):
    smallestDis = 10000
    point = []
    boardMode_boardCor(app)
    #print(app.boardCor2)
    for row in app.boardCor2:
        for col in app.boardCor2[0]:
            c = (row)
            m = (x,y)
            n = distance(c,m)
            #print(n)
            if(n < smallestDis):
                smallestDis = n
                point = c
    #print(point)
    return point
def distance(p1,p2):
    #print(p1,p2)
    return math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )

def boardMode_mousePressed(app, event):
    name = app.getUserInput('What is your name?')
    if (name == None):
        app.message = 'You canceled!'
    else:
        app.showMessage('You entered: ' + name)
        app.message = f'Hi, {name}!'
    
def drawImageWithSizeBelowIt(app, canvas, image, cx, cy):
    canvas.create_image(cx, cy, image=ImageTk.PhotoImage(image))
    
def boardMode_boardCor(app):
    for row in range(app.rows2-1):
        for col in range(app.cols2-1):
            (x0, y0, x1, y1) = boardMode_getCellBounds(app, row, col)
    
            p =(app.marginW +x1,app.marginH +y1)
            app.c.append(p)
            q = (app.marginW + x1+2,147+app.marginH+y1)
            app.boardCor2.append(q)
def boardMode_mousePressed(app, event):
    
   
    #print(app.x)
    #print(event.x,event.y)
    #print("Vertices of Graph")
    #print(app.G.get_vertices())
    return 42
  
def boardMode_keyPressed(app, event):
    if(event.key == "q"):
        #print("hi")
        app.ledBool = True 
        app.g.getVertex
    if(event.key == "r"):
        #print("hi")
        app.sm = True
    
   

def boardMode_getCellBounds(app, row, col):
    # aka 'modelToView'
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = 636
    gridHeight = 101
    x0 =  gridWidth * col / app.cols2
    x1 = gridWidth * (col+1) / app.cols2
    y0 =  gridHeight * row / app.rows2
    y1 =  gridHeight * (row+1) / app.rows2
    
   
    return (x0, y0, x1, y1)
def resColor(app,res):
    colors = app.r.res(res)
    return colors
def getColor(app):
    #app.colorList = []
    for r in range(len(app.x)):
        m = []
        #print("hiiii",app.x)
        for c in range(len(app.x[r])):

            m.append(resColor(app,app.x[r][c]))
        h = m
        app.colorList.append(h)
        #print(h)
    for i in range(len(app.v)):

        print("heyyy",app.v)
        m = []
        for q in range(len(app.v[i])):
            m.append(resColor(app,app.v[i][-1]))
        r = m
        app.colorList2.append(r)
        #print(app.colorList2)
    #print("sup",app.colorList)
  


def boardMode_endList(app):
    L = []
    m = []
    #print(app.x)
    for i in range(len(app.imp)):
        L = []
        print(app.imp,len(app.imp[i]))
        L.append(jDog[i])
        if(len(app.imp[i]) > 1):
            L.append(jDog[i] + 84)
        if(len(app.imp[i]) >= 2):
            add = jDog[i] + 84
            print(add)
            if(len(app.imp[i]) == 2):
                print("hi")
                add-=85
                print(add)
                L.append(add)
            else:   
                #print("hi")
                for l in range(2,len(app.imp[i])):
                    L.append(add)
                    add += 86
        m.append(L)
    print("sup",m)
    app.how = m
    getColor(app)
   
def boardMode_keyPressed(app, event):
    print(app.how,app.resL)
    
    if(event.key == "p"):
        boardMode_endList(app)
        print(app.how,app.resL)
        app.cx2 = copy.deepcopy(app.imp)
        for i in range(len(app.resL)):
            
            for j in range(len(app.how)):
                #print("ha",app.resL[i][0])
                print("hay",app.how,app.resL[i][0])
                if(app.how[j][-1] + 80< app.resL[i][0] < app.how[j][-1] +90):
                    print(app.ha)
                    app.how[j].append(app.resL[i][0])
                    app.cx2[j].append(app.ha[i])
                    break
        print(app.cx2)
    if(event.key == "b"):
        boardMode_endList(app)
        print(app.how,app.resL)
        app.cx2 = copy.deepcopy(app.imp)
        for i in range(len(app.resL)):
            
            for j in range(len(app.how)):
                #print("ha",app.resL[i][0])
                print("hay",app.how,app.resL[i][0])
                if(app.how[j][-1] + 80< app.resL[i][0] < app.how[j][-1] +90):
                    print(app.ha)
                    app.how[j].append(app.resL[i][0])
                    app.cx2[j].append(app.ha[i])
                    break
        print(app.cx2)
        app.mode = 'schemMode'
        app.resList = []
        app.press = True
        app.resDraw = []
        app.vsList = []
        app.voltArc = []
        app.resList = []
        app.linePoint = []
        
        newL2(app)
        app.new = copy.deepcopy(app.cx2)
        #haha
        #= app.cx2
        longest(app)
        
        app.eqRes = ""
        print("sup2",app.eqRes)
    if(event.key == "r"):
        #print("hi")
        app.sm = True

def closestGround(x): 
    smallDis = 99999
    bestG = 0
    for i in range(len(ground)): 
        if(abs(ground[i] - x) < smallDis):
            bestG = ground[i]  
            smallDis = abs(ground[i] - x)   
    return bestG   
def ohms(totalResistors):
    return 42

class Resistor(object):
    def __init__(self):
        r = 0
   
    
    def bandColors(tempResistance,digits):
        #print(tempResistance,digits)
        colors = ["black","brown","red","orange","yellow","green","blue",rgbString(223,7,247)
        ,"grey","white","gold","silver"]
        bandOne = colors[(tempResistance%10)]
        bandTwo = colors[(tempResistance//10)]
        bandThree = colors[digits]
        return (bandTwo,bandOne,bandThree)
    
    
   
    def res(self,resistance):
        word = ""
        totalResistors = []
        resList = []
        while word != None:
            s = resistance
            
            right = s
            word = "hi"
            resistance = int(right)
            
            tempResistance = copy.copy(resistance)
            digits = 0
            resList.append(int(right))
            while tempResistance > 99:
                digits += 1
                #print(digits)
                tempResistance //=10
            bands = Resistor.bandColors(tempResistance,digits)
            
           
            #newResistor = resistor.resi(bands[0], bands[1], bands[2], resistance,word)
           
            return bands
               
# Python3 program to count number
# of trees in a forest.

# A utility function to add an
# edge in an undirected graph.
def addEdge(adj, u, v):
	adj[u].append(v)
	adj[v].append(u)

# A utility function to do DFS of graph
# recursively from a given vertex u.
def DFSUtil(u, adj, visited):
	visited[u] = True
	for i in range(len(adj[u])):
		if (visited[adj[u][i]] == False):
			DFSUtil(adj[u][i], adj, visited)

# Returns count of tree is the
# forest given as adjacency list.
def countTrees(adj, V):
	visited = [False] * V
	res = 0
	for u in range(V):
		if (visited[u] == False):
			DFSUtil(u, adj, visited)
			res += 1
	return res

# Driver code
if __name__ == '__main__':

	V = 5
	adj = [[] for i in range(V)]
	addEdge(adj, 0, 1)
	addEdge(adj, 0, 2)
	addEdge(adj, 3, 4)
	#print(countTrees(adj, V))

#from https://www.geeksforgeeks.org/count-number-trees-forest/
#this code isnt in use


# This code is contributed by PranchalK
class Graph2:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.positions = []
        self.s = set()
        self.build = []
        self.solve = False
        self.isParBool = False
        self.best = 0
        self.a = 0
        self.b = 0
    def getA(self):
       
        return self.a
    def getB(self):
        
        return self.b
    
    def __repr__(self):
        return f'{self.vert_dict,self.build}'
    
       
    
    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, rowCol,weight):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node,rowCol,weight)
        self.positions.append(rowCol)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
    
    def get_vertices(self):
        return self.vert_dict.keys()

    #rename something like x list
    def sorting(self):
        self.build = []
        q = []
        for key in self.vert_dict:
            self.s.add(self.vert_dict[key].get_position()[0])
        q = list(self.s)
        q = sorted(q)
        for i in range(len(self.s)):
            if(len(self.build) != len(q)):
                self.build.append([])
        
        for i in range(len(q)):
            #print(q[i])
            for key in self.vert_dict:
                #print(self.vert_dict[key])
                if(self.vert_dict[key].get_position()[0] == q[i]):
                    m = (self.vert_dict[key].get_position(),self.vert_dict[key].get_weightL())
                    self.build[i].append(m)
        self.build.reverse()
        print(self.build)
        #print("what up my guy",q,self.build)

class Vertex:
    def __init__(self, node,rowCol,weight):
        self.id = node
        self.weight = weight
        self.rowCol = rowCol
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id
    def __repr__(self):
        return f'{self}'
    def get_weightL(self):
        return self.weight

    def get_position(self):
        return self.rowCol

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


    def isPar(self):
        self.isParBool = True
    def isSolve(self):
        self.solve = True
    def solving(self):
        if(self.solve == True):
            if(self.isParBool == True):
                total = 0
                total += self.firstSum(self.build[0])
                for i in range(1,len(self.build)-1):
                    #print(self.build)
                    print("hey",total,self.summing(self.build[i]),self.addTopY(self.build[i]))
                    if((total>0) and (self.summing(self.build[i]) > 0)):
                        c = (1/self.summing(self.build[i]) + (1/total))
                        total = (1/c)
                        print(total)
                        total += self.addTopY(self.build[i])
                        print(total)
                total += self.build[-1][0][1]
             
                return total


#okay so the next thing we are going to want to do is going to be make matrix
#we are going to add in 0c
runApp(width=900, height=800)
