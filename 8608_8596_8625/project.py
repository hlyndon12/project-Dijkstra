import tkinter as tk,random,networkx as nx,time


root = tk.Tk()
root.title("Djkstra")
root.geometry('600x600')
c = tk.Canvas(root, height=500, width=500, bg="black")
c.pack()
lable1 = tk.Label(text = "Press 'd' for Dijkstras path")
lable2 = tk.Label(text = "Press 'c' to clear path")
lable1.pack(side='top')
lable2.pack(side='top')
dk = []
def new():
    b=c.create_rectangle(0,0,500,500,fill= "#ffafbd")
    x = 10
    while (x != 500):
        c.create_line(0,x,500,x)
        c.create_line(x,0,x,500)
        x=x+10
    '''r=c.create_rectangle(0,10,10,0, fill="#753a88")'''
    matrix =[]
    for i in range (0,50):
        matrix.append([])
    for i in range (0,50):
        for j in range (0,50):
            matrix[i].append(j)
            matrix[i][j]=0
    for j in range (0,50):
        for i in range (0,50):
            matrix[j][i]=random.randint(0,1)*random.randint(0,1)*random.randint(0,1)
            if(matrix[j][i]==1):
                r=c.create_rectangle(i*10,j*10,(i*10)+10,(j*10)+10, fill="#00FFFF")
                #print(j+1, i+1)
    matrix[49][49]=0
    matrix[0][0]=0
    g = nx.Graph()
    for i in range (0,50):
        for j in range (0,50):
            if(matrix[i][j]!=1):
                if(j!=49  and matrix[i][j+1]==0 ):
                    g.add_edge((i*50)+j,(i*50)+j+1)
                    
                    #print(i,j,i,j+1)
                if(i!=49 and matrix[i+1][j]==0):
                    g.add_edge((i*50)+j,((i+1)*50)+j)
    global dk
    dk =nx.dijkstra_path(g,0,(50*50)-1)   
        
                #print(i,j,i+1,j)
#print(list(g.edges))
#print(nx.dijkstra_path(g,0,(50*50)-1))

#ast = nx.bidirectional_shortest_path(g,0,(50*50)-1)
'''size = len(sol)
for x in range (0 , len(sol)):
    j = sol[x]//50
    i = sol[x]%50
    #print(i,j)
   # matrix[j][i]=2
    r=c.create_rectangle(i*10,j*10,(i*10)+10,(j*10)+10, fill="black")'''
#print(matrix)
def move(i,j):
    r=c.create_rectangle(i*10,j*10,(i*10)+10,(j*10)+10, fill="black")
    root.update()
def clear(i,j):
    r=c.create_rectangle(i*10,j*10,(i*10)+10,(j*10)+10, fill="#ffafbd")
    root.update()
'''def function(event):
    x = 0
    while(x !=len(sol)):
        b = sol[x]//50
        a = sol[x]%50
        root.after(10,move(a,b))
        x = x+1'''
def function(event):
    global dk
    if(event.char=="d"):
        x = 0
        
        while(x !=len(dk)):
            b = dk[x]//50
            a = dk[x]%50
            root.after(10,move(a,b))
            x = x+1
    '''if(event.char=="a"):
        x = 0
        while(x !=len(ast)):
            b = ast[x]//50
            a = ast[x]%50
            root.after(10,move(a,b))
            x = x+1'''
    '''if(event.char=="s"):
        x = 0
        while(x !=len(ast)):
            b = ast[x]//50
            a = ast[x]%50
            root.after(10,clear(a,b))
            x = x+1'''
    if(event.char=="c"):
        x = 0
        
        while(x !=len(dk)):
            b = dk[x]//50
            a = dk[x]%50
            root.after(10,clear(a,b))
            x = x+1
button = tk.Button(text = "new",command = new)
button.pack(side = "top")
r=c.create_rectangle(0,0,10,10, fill="black")
r=c.create_rectangle(490,490,500,500, fill="black")
root.bind("<Key>",function)
root.mainloop()