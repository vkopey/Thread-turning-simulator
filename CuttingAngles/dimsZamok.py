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

#z66    
zn80={'D':Dim(80,-0.5,0.5,"зовнішній діаметр труби ніпеля"),
    'D1':Dim(76.5,-0.5,0.5,"зовнішній діаметр упорного торця"),
    'd3':Dim(25.0,-0.6,0.6,"внутрішній діаметр ніпеля"),
    'd4':Dim(36.0,-0.6,0.6,"внутрішній діаметр муфти"),
    'L2':Dim(240.0,0.0,0.0,"довжина муфти*"),
    'dsr':Dim(60.080,0.0,0.0,"середній діаметр різьби в основній площині"),
    'd5':Dim(66.674,0.0,0.0,"діаметр більшої основи конуса ніпеля*"),
    'd6':Dim(47.674,0.0,0.0,"діаметр меншої основи конуса ніпеля*"),
    'l3':Dim(76.0,-2.0,0,"довжина конуса ніпеля"),
    'd7':Dim(68.3,-0.6,0.6,"діаметр конічної виточки в площині торця муфти"),
    'd8':Dim(61.422,0.0,0.0,"внутрішній діаметр різьби в площині торця муфти*"),
    'l4':Dim(82.0,0.0,0.0,"відстань від торця до кінця різьби з повним профілем муфти (не менше)"),
    'P':Dim(5.080,0.0,0.0,"крок різьби паралельно осі різьби"),
    'fi':Dim(atan(0.25/2),0.0,0.0,"кут нахилу (рад.)"),
    'H':Dim(4.376,0.0,0.0,"висота гострокутного профілю"),
    'h1':Dim(2.993,0.0,0.0,"висота профілю різьби"),
    'h':Dim(2.626,0.0,0.0,"робоча висота профілю"),
    'l':Dim(0.875,0.0,0.0,"висота зрізу вершин"),
    'f':Dim(0.508,0.0,0.0,"відтин впадини"),
    'a':Dim(1.016,0.0,0.0,"площадка*"),
    'r':Dim(0.508,0.0,0.0,"радіус заокруглень впадин*"),
    'r_':Dim(0.38,0.0,0.0,"радіус спряжень (не більше)"),
    'lsr':Dim(15.875,0.0,0.0,"відстань від торця муфти/ніпеля до основної площини")}

#z152
zn197={'D':Dim(197.0,-0.5,0.5,"зовнішній діаметр труби ніпеля"),
    'D1':Dim(186.0,-0.5,0.5,"зовнішній діаметр упорного торця"),
    'd3':Dim(89.0,-0.6,0.6,"внутрішній діаметр ніпеля"),
    'd4':Dim(122.0,-0.6,0.6,"внутрішній діаметр муфти"),
    'L2':Dim(365.0,0.0,0.0,"довжина муфти*"),
    'dsr':Dim(146.248,0.0,0.0,"середній діаметр різьби в основній площині"),
    'd5':Dim(152.186,0.0,0.0,"діаметр більшої основи конуса ніпеля*"),
    'd6':Dim(131.019,0.0,0.0,"діаметр меншої основи конуса ніпеля*"),
    'l3':Dim(127.0,-2.0,0,"довжина конуса ніпеля"),
    'd7':Dim(154.0,-0.6,0.6,"діаметр конічної виточки в площині торця муфти"),
    'd8':Dim(145.6,0.0,0.0,"внутрішній діаметр різьби в площині торця муфти*"),
    'l4':Dim(133.0,0.0,0.0,"відстань від торця до кінця різьби з повним профілем муфти (не менше)"),
    'P':Dim(6.35,0.0,0.0,"крок різьби паралельно осі різьби"),
    'fi':Dim(atan(1.0/12),0.0,0.0,"кут нахилу (рад.)"),
    'H':Dim(5.487,0.0,0.0,"висота гострокутного профілю"),
    'h1':Dim(3.735,0.0,0.0,"висота профілю різьби"),
    'h':Dim(3.293,0.0,0.0,"робоча висота профілю"),
    'l':Dim(1.097,0.0,0.0,"висота зрізу вершин"),
    'f':Dim(0.635,0.0,0.0,"відтин впадини"),
    'a':Dim(1.270,0.0,0.0,"площадка*"),
    'r':Dim(0.635,0.0,0.0,"радіус заокруглень впадин*"),
    'r_':Dim(0.38,0.0,0.0,"радіус спряжень (не більше)"),
    'lsr':Dim(15.875,0.0,0.0,"відстань від торця муфти/ніпеля до основної площини")}

D=zn80 #zn197 вибрати типорозмір
class Dims(object): pass
d=Dims() # атрибутами є об'єкти класу Dim, що зручніше ніж словник D
for key,value in D.iteritems():
    setattr(d,key,value)

# дійсні розміри ескіза:
d.D.v=d.D.min()/2
d.D1.v=d.D1.min()/2
d.d3.v=d.d3.max()/2
d.d4.v=d.d4.max()/2
d.L2.v=d.L2.n/2
d.dsr.v=d.dsr.n/2
d.d5.v=d.d5.n/2
d.d6.v=d.d6.n/2
d.l3.v=d.l3.min()
d.d7.v=d.d7.max()/2
d.d8.v=d.d8.max()/2
d.l4.v=d.l4.n
d.P.v=d.P.n
d.fi.v=d.fi.n
d.H.v=d.H.n
d.h1.v=d.h1.n
d.h.v=d.h.n
d.l.v=d.l.n
d.f.v=d.f.n
d.a.v=d.a.n
d.r.v=d.r.n
d.r_.v=d.r_.n

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
d.tanFi=tan(d.fi) # тангенс кута нахилу (зміна радіуса конуса на одиницю довжини)
d._r=F(d.dsr-d.tanFi*(d.l4-d.lsr))
d._r.__doc__=u"середній діаметр в площині l4 (менший радіус конуса муфти)"
x1,y1 = -d.H/2, 0 # вектор переміщення в 0,0 середнього діам різця ніпеля
x2,y2 = -d.H/2+d.tanFi*d.P/2, d.P/2 # -//- муфти
d._v1 = x1+d._r, y1+d.l3-d.l4, 0  # поч положення різця ніпеля
d._v2 = x2+d._r, y2+d.l3-d.l4, 0 # поч положення різця муфти