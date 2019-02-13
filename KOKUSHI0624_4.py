import numpy as np
import pandas as pd
import sqlite3
import datetime
import glob
import matplotlib.pyplot as plt
from PIL import Image
import datetime
import os
import sqlite3
import numpy as np
import pandas as pd
import datetime
from ipywidgets import interactive
from IPython.display import display,HTML,clear_output
from time import sleep


#%matplotlib inline

class QQ(object):
    
    def __init__(self):
        
        self.Field = ''
        self.number = int()
        self.cc = 'koku_code.db'
        self.ccf = 'PT'
    
    def invest(self):
        self.Field = input("どの分野の問題をしますか？\n")
        con = sqlite3.connect("koku_code.db")
        c = con.cursor()

        c.execute(f"select count(*) from code_0624 where field='{symbol}'")
        (number_of_rows,)=c.fetchone()
            
        if number_of_rows>0:
            self.number = int(input(f"何問しますか？\n該当問題は全部で\n{number_of_rows}問あります。\n"))
   
            select_sql = f"select * from PT where field='{self.Field}'"
            vv3 = []
            for row in c.execute(select_sql):
                vv3.append(row)
        
        
            np.random.shuffle(vv3)
        
            vv1 = vv3[:self.number]
        
            vv1 = pd.DataFrame(vv1)
            vv1.columns = ["no","categ","number","Figsname","qq","s1","s2","s3","s4","s5","a","field"]
            return vv1
        
        else:
            print("該当する分野はありませんでした。")
        
        con.close()
    

    
    
    
class IDcheck(object):
    
    def __init__(self):
        self.ID = ''
        self.G = ''
        self.KI = ''
        self.NU = ''

    def Searchdata(self,D1,D2,D3,D4):#D1:種類、D2:問題番号、D3:分野、D4:解答結果、D5:時間
        if self.G=='P':
            g='pt'
        elif self.G=='J':
            g='j'
        elif self.G=='A':
            g='a'
        else:
            g='x'
            
        f1 = f"{g}{self.KI.zfill(2)}"+".db"
        f2 = f"{self.NU}"
        tcon = sqlite3.connect(f1)
        #std = f"create table {ID} (NN varchar(10),num integer,updated varchar(30),ans integer)"
        cur = tcon.cursor()
        time = datetime.datetime.now()
        tt = f"{time.year}/{time.month}/{time.day}_{time.hour}:{time.minute}:{time.second}"
        cur.execute(f"insert into {f2}(NN, num,FF ,updated,ans) values ('{D1}',{D2},'{D3}','{tt}',{D4})")
        tcon.commit()
        tcon.close()
        
    
    def SS(self):
        k=0
        while True:
    
            ID = input("Enter your student ID (example; 111P000) :")
            b = [str(i) for i in range(10)]+['J','A','P']

            c=0
            for i in ID:
                c+=b.count(i)
    
            if c==7:
                self.ID = ID
                self.G =  ID[3]
                self.KI = ID[1]
                self.NU = ID[-4:]
                print("success")
                break
                
    
            elif k>=3:
                print("Please visit a creater.")
                break
    
            else:
                print("Please Enter once.")
    
            k+=1
        
    
    def Allanswer(self):
        if self.G=='P':
            g='pt'
        elif self.G=='J':
            g='j'
        elif self.G=='A':
            g='a'
        else:
            g='x'
            
        f1 = f"{g}{self.KI.zfill(2)}"+".db"
        f2 = f"{self.NU}"
        tcon = sqlite3.connect(f1)
        #std = f"create table {ID} (NN varchar(10),num integer,updated varchar(30),ans integer)"
        cur = tcon.cursor()  
        for i in cur.execute(f"select * from {self.NU}"):
            print(i)
            
        tcon.close()
        
        


class kokushi(IDcheck,QQ):
    
    def __init__(self,directname):
        
        self.directname = directname
        self.anssetdata = []
        self.figlist =[]
        self.newans_random_number=[]
        self.newselect =[]
        self.newans=''
        self.figfilename=''
        self.result = int()
        
    def question(self,a,i=0):
        return display(HTML(f"<font size=4>[Q {i}]\n{a}\n"))
         
    
    def ansnumber(self,a,i):
        return display(HTML(f"&emsp;&emsp;<font size=4>{i}. {a}"))
        
    
    
    def ansset(self,ans):
        ans = str(ans)
        if len(ans)!=1:
            a = [ans[i] for i in range(len(ans))]
        else:
            a = [str(ans)]
        
        self.anssetdata= a
    
    
    def figexit(self,figname):
        
        figlist = glob.glob(os.path.join(os.path.expanduser('~'),self.directname,figname)+"*")
        figlist.sort()
        self.figlist = figlist
        print("figss")
    
    def new_ans_set(self,ans,selectlist):
        # to create the random list 
        self.newans_random_number=[i for i in range(5)]
        np.random.shuffle(self.newans_random_number)

        #the new list of answers 
        for i in self.newans_random_number:
            self.newselect.append(selectlist[i])
        
        #the answer to show  
        #v1 = [str(i+1) for i in self.newans_random_number]
        #for i in self.ansset():
        #    self.newans.append(v1.index(i)+1)
        ######
        v=self.newans_random_number
        aa = []
        v1 = [str(i+1) for i in v]
        self.ansset(int(ans))
        for i in self.anssetdata:
            aa.append(str(v1.index(i)+1))
        ######
        
        aa.sort()
        self.newans=''.join([str(i) for i in aa])
        
        if pd.notna(self.figfilename):
            self.figexit(self.figfilename)
            if len(self.figlist)==5 :            
                self.figlist=[self.figlist[i] for i in self.newans_random_number]
                ##
            if len(self.figlist)==6 : 
                fff = self.figlist[:-1]
                fff = [fff[i] for i in self.newans_random_number]
                self.figlist=fff+[self.figlist[-1]]
        ##

    def fig_show6(self,ll):
        figcount = len(ll)
        nc,nr,sizef=2,3,(15,25)

        z255 = np.array([[[255,255,255,255]]],dtype=np.uint8) 
        fig,ax = plt.subplots(nrows=nr,ncols=nc,figsize=sizef)
        for i in range(nc*nr):
            ax[i//nc,i%nc].imshow(z255)
            ax[i//nc,i%nc].tick_params(labelbottom="off",bottom="off") # x軸の削除
            ax[i//nc,i%nc].tick_params(labelleft="off",left="off") # y軸の削除
            ax[i//nc,i%nc].set_xticklabels([])
            ax[i//nc,i%nc].spines["bottom"].set_color("white")
            ax[i//nc,i%nc].spines["top"].set_color("white")
            ax[i//nc,i%nc].spines["right"].set_color("white")
            ax[i//nc,i%nc].spines["left"].set_color("white")

        k=0
        for i in ll:
            im = Image.open(i)
            im_list = np.asarray(im)
                
            #貼り付け
            ax[k//nc,k%nc].imshow(im_list)
            if figcount>=5 and  k<5:
                #ax[i//2,i%2].text(0, 0,f"{k}_{self.newselect[k-1]}",size=14)
                ax[k//nc,k%nc].text(0, 0,f"{k+1}",size=20)#. {self.newselect[k]}",size=14)
                    
            ax[k//nc,k%nc].tick_params(labelbottom="off",bottom="off") # x軸の削除
            ax[k//nc,k%nc].tick_params(labelleft="off",left="off") # y軸の削除
            ax[k//nc,k%nc].set_xticklabels([])
            ax[k//nc,k%nc].spines["bottom"].set_color("white")
            ax[k//nc,k%nc].spines["top"].set_color("white")
            ax[k//nc,k%nc].spines["right"].set_color("white")
            ax[k//nc,k%nc].spines["left"].set_color("white")
            k+=1
            
        plt.show()        
 


    
    def fig_show0(self,ll):
            # In the case of one picture 
        fig,ax=plt.subplots(figsize=(10,10))
        #print("##TEST##")
        #print(self.figlist)
        im = Image.open(ll[0])
        im_list = np.asarray(im)
            #貼り付け
        ax.imshow(im_list)
            
        ax.tick_params(labelbottom="off",bottom="off") # x軸の削除
        ax.tick_params(labelleft="off",left="off") # y軸の削除
        ax.set_xticklabels([])
        ax.spines["bottom"].set_color("white")
        ax.spines["top"].set_color("white")
        ax.spines["right"].set_color("white")
        ax.spines["left"].set_color("white")
                   
        plt.show()
        
        
    def fig_show1(self,ll):
            # In the case of one picture 
        figl=len(ll)
        nc,nr,sizef=1,figcount,(13,6*figcount)
        fig,ax=plt.subplots(ncols=nc,nrows=nr,figsize=sizef)
        #print("##TEST##")
        #print(self.figlist)
        k=0
        for i in ll:
            im = Image.open(i)
            im_list = np.asarray(im)
                
            #貼り付け
            ax[k].imshow(im_list)
                    
            ax[k].tick_params(labelbottom="off",bottom="off") # x軸の削除
            ax[k].tick_params(labelleft="off",left="off") # y軸の削除
            ax[k].set_xticklabels([])
            ax[k].spines["bottom"].set_color("white")
            ax[k].spines["top"].set_color("white")
            ax[k].spines["right"].set_color("white")
            ax[k].spines["left"].set_color("white")
            k+=1
            
        plt.show()    
        

        
        
    def SHOW(self,ans,selectlist,figfilename,qq,kind,kindnumber,field,keyword,m):
        self.figfilename=figfilename
        self.new_ans_set(ans,selectlist)
        if pd.isna(figfilename):
            self.question(qq,m)#############
            for k in enumerate(self.newselect):
                self.ansnumber(k[1],k[0]+1)##############
            
            print('##\n')
            sleep(1)
            self.ANSWER(kind,kindnumber,field,keyword)
            
        
        else:
            if len(self.figlist)>=5:
                print(self.question(qq))
                self.fig_show6(self.figlist)
                for k in enumerate(self.newselect):
                    self.ansnumber(k[1],k[0]+1)
            
                print('##\n')
                sleep(1)
                self.ANSWER(kind,kindnumber,field,keyword)
        
            elif len(self.figlist)==1:
                print(self.question(qq))
                self.fig_show0(self.figlist)
                for k in enumerate(self.newselect):
                    self.ansnumber(k[1],k[0]+1)
            
                print('##\n')
                sleep(1)
                self.ANSWER(kind,kindnumber,field,keyword)
            
            elif len(self.figlist)>1 and len(self.figlist)<5:
                print(self.question(qq))
                self.fig_show1(self.figlist)
                for k in enumerate(self.newselect):
                    self.ansnumber(k[1],k[0]+1)
            
                print('##\n')
                sleep(1)
                self.ANSWER(kind,kindnumber,field,keyword)
        
    

    
    def ANSWER(self,d1,d2,d3,kw):#D1:種類、D2:問題番号、D3:分野、D4:解答結果、D5:時間
       
        display(HTML(f"<font size=5>Enter your answer: </font><br>"))
        aa0 = input("")
        #aa0 = input("<font size=5>Enter your answer: ")

        if not aa0==0:
            self.result=int(str(aa0)==self.newans)
            if str(aa0)==self.newans:
                display(HTML(f"<font size=5 color='blue'>success</font><br>"))#print("success")
                print("############\n")
            
            else:
                g = self.newans
                display(HTML(f"<font size=5 color='#ff1100'>mistaking:{self.newans}</font><br>"))#print("success")
                #print(f"mistaking:{self.newans}\n")
        
        
        #result=int(str(aa0)==self.newans)
        #self.Searchdata(d1,d2,d3,result)
        print(f"############\n\nkey word {kw}\n\n############\n")
        print("\n\n")
        
    
    def Start(self):
        rrr= 0
        self.SS()
        SelectQ = self.invest()
        for i in range(self.number):
            qr1 = SelectQ.iloc[i,:]
            self.SHOW(qr1[10],qr1[5:10],qr1[3],qr1[4],qr1[1],qr1[2],qr1[-1])
            self.figlist=[]
            self.newselect =[]
            self.Searchdata(qr1[1],qr1[2],qr1[-1],self.result)
            
            rrr += self.result
            
        
        print(f"全{self.number}問終了しました。")
        print(f"""今回の結果は{self.number}問中{rrr}問正解です。
        \n\n正答率は　{int(rrr/self.number)}　％でした。""")
        print("""\n######################
                \n######################
                \n
                全ての結果
                \n""")
        
        self.Allanswer()
        
        print("""\n\n###########
                \n###########
                \n""")

        

        
        
        
        
        
        
def readdat(学科,期生,番号,symbol,何問しますか):
    
    
    GGG = 学科
   
    if GGG=='理学療法学科':
        g='pt'
        G = 'P'
        DD = 'PT'
    elif GGG=='柔道整復学科':
        g='j'
        G = 'J'
        DD='JD'
    elif GGG=='鍼灸学科':
        g='a'
        G = 'A'
        DD = 'AC'
        
    
    ###########
    con = sqlite3.connect("koku_code.db")
    c = con.cursor()

    c.execute(f"select count(*) from {DD} where 項目='{symbol}'")
    (number_of_rows,)=c.fetchone()
    print(f'該当分野の問題数は、{number_of_rows} 問です。')
    if 何問しますか>number_of_rows:
        print(f"警告::{number_of_rows}問より減らしてください。")
        
 
   
    select_sql = f"select * from PT where 項目='{symbol}'"
    vv3 = []
    for row in c.execute(select_sql):
        vv3.append(row)
        
        
    np.random.shuffle(vv3)
        
    vv1 = vv3[:何問しますか]
    

            
    KI=期生[:-2].zfill(2)
    KK = 番号
        
    
    f1 = f"{g}{KI.zfill(2)}"+".db"
    f2 = f"{G}{KK}"
    
    return vv1,f1,f2,number_of_rows


######################
######################
######################




###################
###################


def Letgo(dat,w0,w1,directory):#'Documents/Test/12011_1_PM'
    avc = input("ready")
    mmm=1
    for i in dat:
        
        r = kokushi(directory)
        r.SHOW(i[10],i[5:10],i[3],i[4],i[1],i[0],i[11],i[12],mmm)#ans,selectlist,figfilename,qq,kind,kindnumber,field
    
        f1 = f"{w0}"
        f2 = f"{w1}"
        tcon = sqlite3.connect(f1)
        #std = f"create table {ID} (NN varchar(10),num integer,updated varchar(30),ans integer)"
        cur = tcon.cursor()

        time = datetime.datetime.now()
        tt = f"{time.year}/{time.month}/{time.day}_{time.hour}:{time.minute}:{time.second}"
        cur.execute(f"insert into {f2}(NN, num,FF ,updated,ans) values ('{i[1]}',{i[0]},'{i[11]}','{tt}',{r.result})")
        tcon.commit()
        tcon.close()
        mmm=mmm+1
    
    print("終わり")
    tcon = sqlite3.connect(w0)
    #std = f"create table {ID} (NN varchar(10),num integer,updated varchar(30),ans integer)"
    cur = tcon.cursor()
    print(f2)
    for i in cur.execute(f"select * from {w1}"):
        print(i)
        
###################
###################
###################




