# -*- coding: utf-8 -*-
from math import atan, degrees, tan

class Dim:
    "Клас описує поняття розміру"
    n=0.0 #номінальний розмір
    ei=0.0 #нижнє відхилення
    es=0.0 #верхнє відхилення
    v=0.0 #дійсне значення
    def __init__(self,n,ei,es,doc):
        "конструктор"
        self.v=n
        self.n=n
        self.ei=ei
        self.es=es
        self.__doc__=doc.decode('utf-8')
    def min(self):
        "повертає мінімальний розмір"
        return self.n+self.ei
    def max(self):
        "повертає максимальний розмір"
        return self.n+self.es
    
nkt114={'D':Dim(114.3,0.0,0.0,"зовнішній діаметр труби"),
    'd':Dim(100.3,0.0,0.0,"внутрішній діаметр труби"),
    'Dm':Dim(132.1,0.0,0.0,"зовнішній діаметр муфти"),
    'Lm':Dim(156.0,0.0,0.0,"довжина муфти*"),
    'P':Dim(3.175,0.0,0.0,"крок різьби паралельно осі різьби"),
    'dsr':Dim(112.566,0.0,0.0,"середній діаметр різьби в основній площині"),
    'd1':Dim(111.031,0.0,0.0,"зовнішній діаметр різьби в площині торця труби"),
    'd2':Dim(107.411,0.0,0.0,"внутрішній діаметр різьби в площині торця труби"),
    'L':Dim(65.0,-3.2,3.2,"загальна довжина різьби труби"),
    'l':Dim(52.3,0.0,0.0,"довжина різьби труби до основної площини (з повним профілем)"),
    'l1':Dim(10.0,0.0,0.0,"максимальна довжина збігу різьби труби"),
    'd3':Dim(111.219,0.0,0.0,"внутрішній діаметр різьби в площині торця муфти"),
    'd0':Dim(115.9,0.0,0.8,"діаметр циліндричної виточки муфти"),
    'l0':Dim(9.5,-0.5,1.5,"глибина виточки муфти"),
    'A':Dim(6.5,0.0,0.0,"натяг при згвинчуванні вручну"),
    'fi':Dim(atan(1.0/32),0.0,0.0,"кут нахилу (рад)"),
    'H':Dim(2.75,0.0,0.0,"висота вихідного профілю"),
    'h1':Dim(1.81,-0.1,0.05,"висота профілю різьби"),
    'h':Dim(1.734,0.0,0.0,"робоча висота профілю"),
    'alfa_2':Dim(30.0,-1.0,1.0,"кут нахилу сторони профілю alfa/2"),
    'r':Dim(0.508,0.0,0.045,"радіус заокруглення вершини профілю"),
    'r1':Dim(0.432,-0.045,0.0,"радіус заокруглення впадини профілю")}

nkt33={'D':Dim(33.4,0.0,0.0,"зовнішній діаметр труби"),
    'd':Dim(22.6,0.0,0.0,"внутрішній діаметр труби"),
    'Dm':Dim(42.2,0.0,0.0,"зовнішній діаметр муфти"),
    'Lm':Dim(84.0,0.0,0.0,"довжина муфти*"),
    'P':Dim(2.54,0.0,0.0,"крок різьби паралельно осі різьби"),
    'dsr':Dim(32.065,0.0,0.0,"середній діаметр різьби в основній площині"),
    'd1':Dim(32.382,0.0,0.0,"зовнішній діаметр різьби в площині торця труби"),
    'd2':Dim(29.568,0.0,0.0,"внутрішній діаметр різьби в площині торця труби"),
    'L':Dim(29.0,-2.5,2.5,"загальна довжина різьби труби"),
    'l':Dim(16.3,0.0,0.0,"довжина різьби труби до основної площини (з повним профілем)"),
    'l1':Dim(8.0,0.0,0.0,"максимальна довжина збігу різьби труби"),
    'd3':Dim(31.210,0.0,0.0,"внутрішній діаметр різьби в площині торця муфти"),
    'd0':Dim(35.0,0.0,0.8,"діаметр циліндричної виточки муфти"),
    'l0':Dim(8.0,-0.5,1.5,"глибина виточки муфти"),
    'A':Dim(5.0,0.0,0.0,"натяг при згвинчуванні вручну"),
    'fi':Dim(atan(1.0/32),0.0,0.0,"кут нахилу (рад)"),
    'H':Dim(2.2,0.0,0.0,"висота вихідного профілю"),
    'h1':Dim(1.412,-0.1,0.05,"висота профілю різьби"),
    'h':Dim(1.336,0.0,0.0,"робоча висота профілю"),
    'alfa_2':Dim(30.0,-1.0,1.0,"кут нахилу сторони профілю alfa/2"),
    'r':Dim(0.432,0.0,0.045,"радіус заокруглення вершини профілю"),
    'r1':Dim(0.356,-0.045,0.0,"радіус заокруглення впадини профілю")}
    
D=nkt114 #nkt33 вибрати типорозмір
class Dims(object): pass
d=Dims() # атрибутами є об'єкти класу Dim, що зручніше ніж словник D
for key,value in D.iteritems():
    setattr(d,key,value)
    
# дійсні розміри ескіза:
"""
d.D.v=d.D.n/2
d.d.v=d.d.max()/2
d.Dm.v=d.Dm.min()/2
d.Lm.v=d.Lm.n/2
d.P.v=d.P.n
d.dsr.v=d.dsr.n/2
d.d1.v=d.d1.n/2
d.d2.v=d.d2.n/2
d.L.v=d.L.min()
d.l.v=d.l.n
d.l1.v=d.l1.n
d.d3.v=d.d3.n/2
d.d0.v=d.d0.min()/2
d.l0.v=d.l0.max()
d.A.v=d.A.n
d.fi.v=d.fi.n
d.H.v=d.H.n
d.h1.v=d.h1.max()
d.h.v=d.h.n
d.alfa_2.v=d.alfa_2.n
d.r.v=d.r.max()
d.r1.v=d.r1.min()
"""
d.D.v=d.D.n/2
d.d.v=d.d.n/2
d.Dm.v=d.Dm.n/2
d.Lm.v=d.Lm.n/2
d.P.v=d.P.n
d.dsr.v=d.dsr.n/2
d.d1.v=d.d1.n/2
d.d2.v=d.d2.n/2
d.L.v=d.L.n
d.l.v=d.l.n
d.l1.v=d.l1.n
d.d3.v=d.d3.n/2
d.d0.v=d.d0.n/2
d.l0.v=d.l0.n
d.A.v=d.A.n
d.fi.v=d.fi.n
d.H.v=d.H.n
d.h1.v=d.h1.n
d.h.v=d.h.n
d.alfa_2.v=d.alfa_2.n
d.r.v=d.r.max()
d.r1.v=d.r1.min() #0.3 - для FEA без радіусів при вершині

# приклад використання:
#print d.D.v
#print d.D.n
#print d.D.min()
#print d.D.__doc__

##
# Або доступ до дійсного значення без атрибута v:
class F(float, Dim): pass
d=Dims() # атрибутами є дійсні розміри ескіза
for key,value in D.iteritems():
    setattr(d,key,F(value.v))
    getattr(d,key).v=value.v
    getattr(d,key).n=value.n
    getattr(d,key).ei=value.ei
    getattr(d,key).es=value.es
    getattr(d,key).__doc__=value.__doc__

# приклад використання:
#print d.D
#print d.D.n
#print d.D.min()
#print d.D.__doc__

# допоміжні параметри:
# Увага! не враховано відхилення h1
d.tanFi=tan(d.fi) # тангенс кута нахилу (зміна радіуса конуса на одиницю довжини)
d._l=d.L-d.A # відстань від 0 до верхнього торця муфти
d._l2=d.Lm-d._l # відстань від 0 до нижнього торця муфти
d._r=d.dsr-d.tanFi*(d.l+d._l2) # радіус середнього діаметра в нижьому торці муфти
x1,y1 = -d.H/2, 0 # вектор переміщення в 0,0 сер діам різця ніпеля
x2,y2 = -d.H/2+d.tanFi*d.P/2, d.P/2 # -//- муфти
d._v1 = x1+d._r, y1-d._l2, 0  # поч положення різця ніпеля
d._v2 = x2+d._r, y2-d._l2, 0 # поч положення різця муфти