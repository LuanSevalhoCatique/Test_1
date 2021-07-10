# Programa para determinar a energia de ativação 30/06/2021.
# Autor: Luã da Costa Catique
# Ufam PPGFIS
import numpy as np
import matplotlib.pyplot as plt
import math
data = np.loadtxt(r'C:\Users\catiq\Dropbox\Doutorado042020\MiGrafAl07C\McBaMT300K\TabAjCrT300K\TabAjCrT300K.txt', comments="#", dtype='str')
x_T = data[:,1]
y_dc = data[:,2]
lista_temperatura = [float(x) for x in x_T]
x_T = lista_temperatura
lista_sigma_dc = [float(x) for x in y_dc]
print('Lista da condutividade dc')
print(lista_sigma_dc)

listT =[]
for i in x_T:
    T1 = 1000.0/(i)
    listT.append(T1)
lista_y = []
for j in range(len(x_T)):
    valor_y = math.log(lista_sigma_dc[j]*lista_temperatura[j])
    lista_y.append(valor_y)
print('Lista 1/T')
print(listT)
print('Lista da  log condutividade dc*T')
print(lista_y)

Kb =  float(8.6173324e-5)
def cond1(T, uo, Ea):
    u = math.log(uo)-(Ea/Kb)*(1/T)
    return u

from scipy.optimize import curve_fit

parametros_iniciales=[1e-5, 0.5]
popt, pcov = curve_fit(cond1, lista_temperatura, lista_y, p0=parametros_iniciales)
parametro1 = popt[0]
parametro2 = popt[1]
#------------------------------------------------------------
print('Parâmetro sigma_o: %s +/- %s' % (popt[0], pcov[0,0]**0.5))
print('Parâmetro Energia de ativação:%s +/- %s' % (popt[1], pcov[1,1]**0.5))

funcaoY = []

for j in range(len(x_T)):
    f_u = math.log(parametro1)-(parametro2/Kb)*(1/lista_temperatura[j])
    funcaoY.append(f_u)
print('Lista de ajuste da condutividade dc')
print(funcaoY)

R = (np.corrcoef(funcaoY, lista_y)[0,1]) # aqui
print('Desvio quadrático: %s'% R)

# SALVAR DADOS DO AJUSTE DE CURVA

# salvar parâmetros de ajuste
dados = open( r'C:\Users\catiq\Dropbox\Doutorado042020\MiGrafAl07C\McBaMT300K\TabAjCrT300K\TabEaCrT300K.txt', 'w')
dados.write('Energia de ativação para a temperatura no intervalo de 60-100K\n\n')
dados.write('Sigma_o =  {} +/- {}\n'.format(popt[0], pcov[0,0]**0.5))
dados.write('E_a = {} +/- {}\n'.format(popt[1], pcov[1,1]**0.5))
dados.write('Correlação = {}\n'.format(R))
dados.close()
# salvar dados de ajuste
dados1 = open(r'C:\Users\catiq\Dropbox\Doutorado042020\MiGrafAl07C\McBaMT300K\TabAjCrT300KDadosEaCrT300K.txt', 'w')
dados1.write('#Energia de ativação para a temperatura no intervalo de 60-100K\n\n')
dados1.write('#Sigma_o =  {} +/- {}\n'.format(popt[0], pcov[0,0]**0.5))
dados1.write('#E_a = {} +/- {}\n'.format(popt[1], pcov[1,1]**0.5))
dados1.write('#Correlação = {}\n'.format(R))
dados1.write('#{}      {}     {}\n'.format(r'ln(cr*T)', r'1/T', r'Aj_ln(cr*T)'))
for i in range(len(x_T)):
    dados1.write('{}      {}     {}\n'.format(lista_y[i], listT[i], funcaoY[i]))
dados1.close()

fig = plt.figure(figsize=(9, 6))
fig.subplots_adjust(right=0.955, left=0.129, bottom=0.174, top=0.95)
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(listT, lista_y, 'bo', label='Dados experimentais')
plt.plot(listT, funcaoY, 'r--', label='Ajuste de Curva')
plt.text(3.65, -1.5, r'$E_{a} = (0.445 \pm 0.035)eV$', fontsize=15)
plt.legend(loc='best')
plt.xlabel('$1000/T(K)$', fontsize=15)
plt.ylabel('$\\ln(\\sigma_{dc}T)(\\Omega cm)^{-1}$', fontsize=15)
#plt.yscale('log')
#plt.xscale('log')
plt.title('Energia de ativação')
plt.savefig(r'C:\Users\catiq\Dropbox\Doutorado042020\MiGrafAl07C\McBaMT300K\TabAjCrT300K\EaAjCrT300K.png')
plt.savefig(r'C:\Users\catiq\Dropbox\Doutorado042020\MiGrafAl07C\McBaMT300K\TabAjCrT300K\EabAjCrT300K.pdf')
plt.show()
