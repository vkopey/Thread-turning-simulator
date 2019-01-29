# -*- coding: utf-8 -*-
"Інструменти для побудови моделі"
import FreeCAD as App # модуль для роботи з програмою
import FreeCADGui as Gui # модуль для роботи з GUI
import Part # workbench-модуль для створення і керування BRep об'єктами
print "OCC", Part.OCC_VERSION
import numpy as np
pi=np.pi

##
def show(name): # показує форму
    doc.addObject("Part::Feature",name).Shape=globals()[name]

def rebuildSketch_(dim, sk):
    """Перебудовує ескіз і повертає грань
    dim - словник з розмірами ескізу sk
    Ключами може бути номер або назва обмеження ескізу"""
    doc=App.activeDocument()
    sketch=doc.__getattribute__(sk) #або doc.<назва ескізу>
    for k,v in dim.iteritems():
        print k,v
        sketch.setDatum(k,v)
    doc.recompute()
    w=sketch.Shape.Wires[0]
    f=Part.Face(w) # грань
    return f
    
def rebuildSketch(dim, sk):
    """Перебудовує ескіз і повертає грань
    dim - словник з розмірами ескізу sk
    Ключами може бути номер або назва обмеження ескізу
    Це версія функції працює коректно зі значними змінами розміру"""
    doc=App.activeDocument()
    sketch=doc.__getattribute__(sk) #або doc.<назва ескізу>
    dv={}
    n=100 # кількість ітерацій
    for k,v in dim.iteritems():
        #print k,v
        dv[k]=np.linspace([x for x in sketch.Constraints if x.Name==k][0].Value, v, 100) # радіани
        #dv[k]=np.linspace(sketch.getDatum(k).Value, v, n) # градуси
    for i in range(n):
        for k,v in dim.iteritems():
            #print i   
            sketch.setDatum(k,dv[k][i])
    doc.recompute()
    doc.saveAs(u"sketch_temp.FCStd")
    w=sketch.Shape.Wires[0]
    f=Part.Face(w) # грань
    return f
        
def revolve(f):
    """Створює тіло шляхом обертання грані f навколо осі Y"""
    return f.revolve(App.Vector(0,0,0), App.Vector(0,1,0)) # тіло

def helix(r,h,p,fi):
    "Гвинтова лінія. r-радіус, h-висота, p-крок, fi-кут конуса (рад.)"
    w=Part.makeLongHelix(p,h,r,np.degrees(fi)) # !!! але не makeHelix
    #FreeCAD-master\src\Mod\Part\App\TopoShape.cpp
    w.rotate(App.Vector(0,0,0),App.Vector(1,0,0),-90)
    return w

def makeThread(f,h,s): # різьба ніпеля/муфти
    s2=h.makePipeShell(f.Wires,True,True) # дозволяє кілька профілів!
    #https://forum.freecadweb.org/viewtopic.php?t=4199
    s=s.cut(s2)
    return s

def makeQuasiThread(f,s,p,tanFi,h):
    """3D квазі-різьба (кільцеві канавки) ніпеля/муфти
    f - грань передньої поверхні, s - тіло заготовки, p - крок, tanFi - тангенс кута нахилу, h - довжина різьби"""
    plane=Part.makePlane(400,400,App.Vector(0,-200,0),App.Vector(0,0,1)) # площина XY
    h_=0
    while h_<h:
        proj=plane.makeParallelProjection(f.OuterWire,App.Vector(0,0,1))
        fp=Part.Face(proj.Wires[0])
        s2=revolve(fp)
        s=s.cut(s2)
        f.translate((tanFi*p,p,0))
        h_+=p
    return s

def angle_(): # виберіть вершину, грань і задню поверхню
    v,face = FreeCADGui.Selection.getSelectionEx()[0].SubObjects # вибрати вершину і грань
    v0=v.Point
    f, = FreeCADGui.Selection.getSelectionEx()[1].SubObjects # вибрати задню поверхню
    uv=face.Surface.parameter(v.Point) # значення параметрів поверхні у точці
    t=face.tangentAt(uv[0],uv[1]) # дотична
    line=Part.makeLine((t[0].x,t[0].y,t[0].z), (t[1].x,t[1].y,t[1].z))
    line.translate((v.X-t[0].x, v.Y-t[0].y, v.Z-t[0].z)) # в положення точки
    Part.show(line)
    print line.Edges
    e=line.Edges[0]
    v1,v2=e.Vertexes # вершини
    v1,v2=v1.Point,v2.Point # вектори
    print v0
    print v1,v2
    
    # p=f.project([e]) # проекція на задню поверхню (увага! сплайн)
    # print p.Edges
    # Part.show(p)
    # v3,v4=p.Vertexes # вершини
    # v3,v4=v3.Point,v4.Point # вектори
    # print v3,v4
    # a=(v0-v2).getAngle(v0-v4) # кут між векторами
    # print np.degrees(a)
    
    v5=App.Vector(v2).projectToPlane(f.Surface.value(0,0), f.Surface.normal(0,0)) # інший спосіб
    print v5
    a=(v0-v2).getAngle(v0-v5) # кут між векторами
    print np.degrees(a)

def angle__():
    v,e1 = FreeCADGui.Selection.getSelectionEx()[0].SubObjects # вибрати вершину і гвинтову кромку
    e2,f = FreeCADGui.Selection.getSelectionEx()[1].SubObjects # вибрати різальну кромку і задню поверхню
    v1,v2=e2.Vertexes
    v3=v1 if not v.Point.isEqual(v1.Point, 1e-3) else v2  # v3 не v
    vec=e1.tangentAt(e1.parameterAt(v)) # дотична в точці
    vec=vec+v.Point # перемістити в положення
    Part.show(Part.Point(vec).toShape())
    pl=Part.Plane(v.Point,v3.Point,vec) # площина різання
    uv=pl.parameter(v.Point)
    vec2=pl.normal(uv[0],uv[1]) # нормаль до площини різання (0,0 або uv[0],uv[1])
    #vec2=vec2+v.Point # перемістити в положення
    #Part.show(Part.Point(vec2).toShape())
    
    # кут між площинами - це кут між їх нормалями !!!
    uv=f.Surface.parameter(v.Point)
    vec3=f.Surface.normal(uv[0],uv[1]) # нормаль до задньої поверхні (0,0 або uv[0],uv[1])
    a=vec2.getAngle(vec3) # кінематичний задній кут
    print np.degrees(a)

def angle(f0,f1,v0,e0):
    """f0 - передня поверхня, f1 - задня поверхня, v0 - вершина на різальній кромці, e0 - гвинтова кромка"""
    plane0=f0.Surface
    curve0=e0.Curve
    res=plane0.intersect(curve0) # або common, distToShape
    print "к-ть точок перетину: ", len(res[0])
    #p1=res[0][0] # точка Part.Point перетину
    # але може бути кілька точок перетину, тому використовуйте: elt.Placement.Base isEqual distanceToPoint
    for resi in res[0]:
        if v0.Point.isEqual(resi.toShape().Point, d.P): # близька до v0
            p1=resi
    Part.show(p1.toShape())
    vec1=App.Vector(p1.X, p1.Y, p1.Z)
    vec=curve0.tangent(curve0.parameter(vec1))[0] # дотична в точці
    vec=vec+vec1 # перемістити в положення
    plane=Part.Plane(vec1, v0.Point, vec) # площина різання
    Part.show(Part.makeLine(vec1,vec))
    Part.show(Part.makeLine(vec1,(vec-vec1).negative()+vec1))
    uv=plane.parameter(vec1)
    vec2=plane.normal(uv[0],uv[1]) # нормаль до площини різання
    uv=f1.Surface.parameter(vec1)
    vec3=f1.Surface.normal(uv[0],uv[1]) # нормаль до задньої поверхні
    a=vec2.getAngle(vec3) # кінематичний задній кут
    
    vec2=vec2+vec1 # перемістити в положення
    plane=Part.Plane(vec1, v0.Point, vec2) # основна площина
    Part.show(Part.makeLine(vec1,vec2))
    Part.show(Part.makeLine(vec1,(vec2-vec1).negative()+vec1))
    uv=plane.parameter(vec1)
    vec4=plane.normal(uv[0],uv[1]) # нормаль до основної площини
    uv=f0.Surface.parameter(vec1)
    vec5=f0.Surface.normal(uv[0],uv[1]) # нормаль до передньої поверхні
    g=vec4.getAngle(vec5) # кінематичний передній кут
    return np.degrees(a), np.degrees(g)

def section(s1,s2):
    """поздовжній перетин для FEA моделі"""
    f=Part.makePlane(400,400,App.Vector(0,-200,0),App.Vector(0,0,1)) # площина XY
    f1=s1.common(f).Faces[0] # поздовжній перетин
    f2=s2.common(f).Faces[0]
    return f1,f2
