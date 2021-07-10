# Grafico Ajuste de Jonscher T200
import matplotlib.pyplot as plt
import numpy as np

# dados de entradas
lista_de_cores = ['#000000', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6',
                       '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', 'red', '#800000', '#aaffc3', '#808000',
                       '#ffd8b1', '#000075', '#808080', '#ffffff']

data=np.loadtxt('DadosJonscherCrT110.txt')
f1=data[:,0]
Cr1=data[:,1]
AjCr1=data[:,2]

data=np.loadtxt('DadosJonscherCrT120.txt')
f2=data[:,0]
Cr2=data[:,1]
AjCr2=data[:,2]

data=np.loadtxt('DadosJonscherCrT130.txt')
f3=data[:,0]
Cr3=data[:,1]
AjCr3=data[:,2]

data=np.loadtxt('DadosJonscherCrT140.txt')
f4=data[:,0]
Cr4=data[:,1]
AjCr4=data[:,2]

data=np.loadtxt('DadosJonscherCrT150.txt')
f5=data[:,0]
Cr5=data[:,1]
AjCr5=data[:,2]

data=np.loadtxt('DadosJonscherCrT160.txt')
f6=data[:,0]
Cr6=data[:,1]
AjCr6=data[:,2]

data=np.loadtxt('DadosJonscherCrT170.txt', comments="#")
f7=data[:,0]
Cr7=data[:,1]
AjCr7=data[:,2]

data=np.loadtxt('DadosJonscherCrT180.txt', comments="#")
f8=data[:,0]
Cr8=data[:,1]
AjCr8=data[:,2]

data=np.loadtxt('DadosJonscherCrT190.txt')
f9=data[:,0]
Cr9=data[:,1]
AjCr9=data[:,2]

data=np.loadtxt('DadosJonscherCrT200.txt')
f10=data[:,0]
Cr10=data[:,1]
AjCr10=data[:,2]


lista_tempe = [str('%s.0K'%i) for i in range(110, 210, 10)]
print(lista_tempe)
lista_freq = [('f%s'%i) for i in range(1,16)]
print(lista_freq)
lista_Cr = [('Cr%s'%i) for i in range(1,16)]
print(lista_Cr)
lista_AjCr = [('AjCr%s'%i) for i in range(1,16)]
print(lista_AjCr)

######
#Listas
l_f = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
l_cr = [Cr1, Cr2, Cr3, Cr4, Cr5, Cr6, Cr7, Cr8, Cr9, Cr10]
l_t = lista_tempe
l_c = lista_de_cores
l_ajcr = [AjCr1, AjCr2, AjCr3, AjCr4, AjCr5, AjCr6, AjCr7, AjCr8, AjCr9, AjCr10]
l_t.append('\nAjuste')


#tamanho da figura
fig = plt.figure(figsize=(9, 6))
fig.subplots_adjust(right=0.82, left=0.129, bottom=0.174, top=0.964)
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
print(l_f[0])
# dados experimentais
i = 0
while i <= len(l_cr)-1:
    eixo_x = l_f[i]
    eixo_y = l_cr[i]
    plt.plot(eixo_x, eixo_y, label=l_t[i] ,marker='o',linestyle='',color=l_c[i],markersize=6)
    #plt.legend(loc='upper center', bbox_to_anchor=(1.12, 0.95), shadow=True, ncol=1, fontsize=11)
    i = i + 1

i = 0
while i <= len(l_cr)-1:
    eixo_x = l_f[i]
    eixo_y = l_ajcr[i]
    plt.plot(eixo_x, eixo_y, linestyle='-',color='r',markersize=6)
    #plt.legend(['30.0K', '35.0K', '40.0K', '45.0K', '50.0K', '55.0K', '60.0K', '65.0K', '70.0K', '75.0K', '80.0K', '85.0K', '90.0K', '95.0K', '100.0K',
    #            '\nAjuste'],
    #loc='upper center', bbox_to_anchor=(1.12, 0.95), shadow=True, ncol=1, fontsize=11)
    plt.legend(l_t,loc='upper center', title='Temperatura',bbox_to_anchor=(1.12, 0.95), shadow=True, ncol=1, fontsize=11)

    #plt.legend(prop={'family': 'monospace'})
    i = i + 1

plt.xlabel('$f(Hz)$', fontsize=15)
plt.ylabel('$\\sigma^{\'}(\\Omega cm)^{-1}$', fontsize=15)
plt.yscale('log')
plt.xscale('log')
plt.savefig('GrafAjJonscherT200.png')
plt.savefig('GrafAjJonscherT200.pdf')
plt.show()
