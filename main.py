import pandas as pd
import conf as c
import random as rnd




def U(E_t,S_t):
    """
        Tabe mohasebe Matloobiat
        :param E_t: hazine afrad
        :param S_t: hazine masrafi bakhsh dolati
        :return: Emtiaze Matloobiat
    """
    return ((1/(1-c.vu))*((E_t**(1-c.upsilon))*(S_t**(c.upsilon))))**(1-c.vu)

def L (E_t,S_t,landa , mu , Year, G , R_f,R_s,R_p ,t_j,v_j):
    """
        Tabe mohasebe Lagranzh
        :param E_t: hazine afrad
        :param S_t: hazine masrafi bakhsh dolati
        :param landa: Zaribe Aval Lagranzh
        :param mu: Zaribe Dovom Lagranzh
        :param Year: Salha
        :param G: Pardakhthaye jaari
        :param R_f: Maaliate mostaghim
        :param R_s: Daramad Penhan
        :param R_p: Daramad + Daramad Penhan
        :param t_j: nerkhe maliaat bar vaaredat
        :param v_j: nerkhe maliaat bar arzesh afzoodeh
        :return: Emtiaze Lagranzh
    """
    lagranzh = 0 ; Zigma_1 = 0 ; Zigma_2 = 0 ; Zigma_3 = 0 ; U1 =0
    for i in range(len(Year)):
        Zigma_1 += t_j*(E_t[i] - R_p[i])
        Zigma_2 += v_j*(E_t[i] - R_s[i])+ R_f[i]
        Zigma_3 += R_p[i] - E_t[i]  - landa*G[i]
        U1 += U(E_t[i], S_t[i])
    lagranzh +=U1 +  (landa - mu) * (Zigma_1 + Zigma_2 )
    lagranzh += mu * Zigma_3
    return lagranzh

def read_file(path = 'mr.asad data.xlsx'):
    """
    Tabe Khandane File
    :param path: Masire File Excel
    :return: year list : List Salhha
             Et list   : List hazine afrad
             St list   : List hazine masrafi bakhsh dolati
             G list    : List Pardakhthaye jaari
             Rf list   : List Maaliate mostaghim
             R list    : List Daramad
             Rs list   : List Daramad Penhan
             Rp list   : List Daramad + Daramad Penhan
             
    """
    year =[]; Et=[];St=[];G=[];Rf=[];R=[];Rs=[];Rp=[]
    dfs1 = pd.read_excel(path, sheet_name='Sheet1')
    for index, row in dfs1.iterrows():
        year.append(int(row['year']))
        Et.append(row['Et'])
        St.append(row['St'])
        G.append(row['G'])
        Rf.append(row['Rf'])
        R.append(row['R'])
        Rs.append(row['Rs'])
        Rp.append(row['Rp'])
    return year,Et,St,G,Rf,R,Rs,Rp

if __name__ == "__main__":
    result = -1
    year,Et,St,G,Rf,R,Rs,Rp = read_file()
    for i in range(c.iteration):
        r1 = rnd.uniform(c.LowerBand1, c.UpperBand1)
        r2 = rnd.uniform(c.LowerBand2, c.UpperBand2)
        landa = rnd.uniform(0,1)
        mu = rnd.uniform(0,landa)
        Lag = L(E_t=Et,S_t=St,landa=landa,mu=mu,Year=year,G=G,R_f=Rf,R_s=Rs,R_p=Rp,t_j=r1,v_j=r2)
        if result < Lag :
            result = Lag
            print(result, '\t\t landa=',landa,'\t mu=',mu,'\t t_j=',r1,'\t  v_j=',r2)


