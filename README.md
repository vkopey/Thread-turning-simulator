# Thread-turning-simulator
The system, based on FreeCAD, for creating geometric models of threaded joints with various geometric deviations, which arise during the thread turning.

Using FreeCAD API, a Python program has been developed for simulating threads with various geometric deviations that occur during thread turning. The algorithm is based on the approximation of a complex trajectory of tool movement by splines and using the Boolean "cut" operation on the bodies of the workpiece and the tool.

To simulate various machining errors in the program, it is possible to change the values of the geometric parameters of the workpiece and tool and the parameters of the tool path relative to the workpiece. The testing of the suitability of threads with deviations is realized by Boolean operations on the maximum permissible and real bodies. The models of threaded connections constructed with this program can be used to simulate the stress-strain state by the finite element method and justify the values of the thread tolerances.

---

If you use Thread-turning-simulator please cite the following reference in your work (books, articles, reports, etc.):

Kopei V, Onysko O, Panchuk V 2018 Computerized System Based on FreeCAD for Geometric Simulation of Thread Turning of Oil and Gas Pipes, 6th International Conference of Applied Science (May 9-11, 2018, Banja Luka, Bosnia and Herzegovina): Book of Abstracts (Banja Luka: University of Banja Luka) 108
