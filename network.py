import numpy as np
import random
import copy

def m_sum(m):
    val=0
    for i in range(0, len(m)):
        val+=m[i]
    return val

def m_add(m1, m2):
    if(len(m1)==len(m2)):
        tempArray=[]
        for i in range(0, len(m1)):
            tempArray.append(m1[i]+m2[i])
        return tempArray

def m_sub(m1, m2):
    if(len(m1)==len(m2)):
        tempArray=[]
        for i in range(0, len(m1)):
            tempArray.append(m1[i]-m2[i])
        return tempArray

def m_pow(m1, power):
    tempArray=[]
    for i in range(0, len(m1)):
        tempArray.append(pow(m1[i],power))
    return tempArray

def sigmoid(z):
    return 1/(1+np.exp(-z))

def inverseSigmoid(z):
    return -1*np.log(z/(1-z))

class NeuralNetwork():
    def __init__(self, layers):
        self.layers = layers
        self.wb=[[[15.08564862125264, -2.198893010482858, -10.01957083494719, -17.195390000236184, 14.363304927869907, 9.091221558207344, -28.109238211597837, 18.537519632244322, -5.126288296830021, -10.91489255206032, -40.22151787830566, -56.72805614596976, 23.24865864396427, -26.16804908646627, -7.8835125326129205, 4.554917323741176, -7.4923151771922, -32.62977195290588, 33.10278032047831, -20.726801224772345, -13.449932956235564, -14.8054069706005, -0.7662901508715265, -11.171399523881222, -36.619430129667705, -28.20221774424308, -36.641413702221534, -25.707124383598607, -1.5664291442604612, -10.707376457682804, 2.958020758773167, 17.911062433170603, 7.599549832095988, 28.370154775778627, 15.767559257688639, -3.5209857721814237, -13.066748019028198, 15.409732700467194, 3.5156094135183773, 7.093577309059785, -15.238930383701113, -29.157517146282615, -9.057455605737324, -38.73516525297248, -28.238851529885146, -15.009918065311098, -28.830468667901478, 14.316972490451796, 3.503184144803712, 31.01440508031197, 12.589855569321264, -27.617958717622926, -0.8613452719645291, -0.8584341483541877], [16.689709720371397, 34.523678615712406, -14.383141352449744, -24.119680099651013, -5.082476767342061, 19.95258739091315, -54.0611426272638, -7.763081356344011, -47.06515328438125, -13.89529076292639, 21.479793119640014, 28.949100574556386, 24.619828756935863, 14.425975627856078, 23.560287202584973, -0.5157717586484463, -60.67075654533989, -12.4554868343175, -5.359185834181952, 92.7718197353742, -2.54720832389739, 12.597733986521202, 28.565709281084036, -78.48676121499314, -42.32271659621202, 43.07038117197655, -15.5584251113811, -0.9321026702486837, 16.944917799110804, -2.4586037925957074, 23.038348058478395, 9.957857070651464, 35.07453715641598, 44.87335353975837, 30.315698141555075, -32.53627998254304, 49.619177168545754, 13.981641695254591, 2.251094857189446, -14.681814194326662, 12.851512211102452, -40.6404154306253, 3.4103016243715345, -40.2732665182729, -31.922825420440578, -0.19127120397993203, -9.070426572961004, 18.0676647166215, 1.8074980931190359, -5.8959578685468585, 17.69066723155445, 8.806520583013137, 2.979072171727482, -11.560688383371073], [13.210537277074067, -5.957252942884296, -7.274732750164444, -59.15777360856177, -6.12934156256753, 0.061412775244624296, 56.1806934248825, -37.73383320073515, -6.011517348738156, 7.451057522048121, 18.46283238138572, -34.55925743535065, -7.235565129027146, 29.948361454406363, -10.177092626144328, 41.00851591330697, 0.6996464985494093, -15.975068621250399, 78.17601480168108, 11.65463971224047, 2.2880252380108477, 1.3679504299508283, 14.94830835944942, 15.478791461799982, -15.901002101642218, 14.50717422998854, 13.617467918326142, -4.5230376501693, 22.627648345312082, 56.275768988955335, 13.917087766148288, 47.855311506725414, -19.523901955099326, -9.09270028080736, -4.197743095472802, 6.669177413198267, 9.381928564756713, -0.606325803122977, -27.95799035075962, -23.884487059292912, -26.3837822407675, 10.467986543306946, -9.576705413773512, -27.401612557992465, 25.803063301849182, 21.61286131657787, -23.935616189191578, 3.360069488244476, 12.417797102066663, -14.820891814558198, -24.022042748733057, 13.888420328536178, 26.3431185322359, -20.688152709474835], [-51.71224918228864, 17.57059228618841, 7.467802989560044, -10.658569204727357, -5.181594926885024, -5.007812073122851, -15.357633137639427, 48.483528666762425, -40.708057082568665, -56.54865937998569, 37.978127123051564, 31.837845784081537, 24.980506480631128, 26.406232432173475, 8.564059575348336, -16.490257917534333, -40.991416266525775, -11.473611475673348, -40.521582457716335, 12.927908360966054, 59.23946125933679, -17.064865605758907, -7.018028665349306, -43.4136423752578, -9.603860883379653, -17.30218599202771, 35.47722389092292, 10.490784658708128, -22.625328419708133, 20.343059845804536, -2.3940479046131466, 47.94666077733907, -12.25466929962999, -8.156494128610845, 6.207502110427006, -35.86815122132265, 6.239428358387307, 3.7825143869611977, -21.352904937358915, 26.087807198577195, -10.738020834222086, 21.38405769861227, -12.629392902288973, -7.017200822984226, 34.7739753836156, -19.46459982927865, -17.403755056635394, 5.942882770611336, 41.18647511221289, -19.72503969183955, -21.227944971610995, 4.780111390736892, -12.24592057033393, 9.413556167040152], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []], [], [], [], [], []]
        """for i in range(0, len(self.layers)-1):
            self.wb.append([])
            for j in range(0, self.layers[i+1]):
                self.wb[i].append([])
                for k in range(0, self.layers[i]+1):
                    self.wb[i][j].append(1)"""
        self.best=self.wb

    def calc(self, val):
        for i in range(0, len(val)):
            val[i]=sigmoid(val[i])
        answer=self.func(val)
        for i in range(0, len(answer)):
            answer[i]=inverseSigmoid(answer[i])
        return answer

    def func(self, val):
        neurons = []
        for i in range(0, len(self.layers)):
            neurons.append([])
            for j in range(0, self.layers[i]):
                neurons[i].append(0)

        neurons[0]=val
        for i in range(0, len(self.layers)-1):
            for j in range(0, self.layers[i+1]):
                tempVar=0
                for k in range(0, self.layers[i]):
                    tempVar+=self.wb[i][j][k]*neurons[i][k]
                tempVar+=self.wb[i][j][len(self.wb)-1]
                neurons[i+1][j]=sigmoid(tempVar)
        return neurons[len(neurons)-1]

    def cost(self, val):
        return m_sum(m_pow(m_sub(self.func(val[0]), val[1]), 2))

    def bestVals(self):
        self.best=copy.deepcopy(self.wb)

    def nudge(self, alpha):
        for i in range(0, len(self.wb)):
            for j in range(0, len(self.wb[i])):
                for k in range(0, len(self.wb[i][j])):
                    self.wb[i][j][k]=self.best[i][j][k]+(random.random()-0.5)*alpha