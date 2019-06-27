# Thread-turning-simulator
The system, based on FreeCAD, for creating geometric models of threaded joints with various geometric deviations, which arise during the thread turning.

Using FreeCAD API, a Python program has been developed for simulating threads with various geometric deviations that occur during thread turning. The algorithm is based on the approximation of a complex trajectory of tool movement by splines and using the Boolean "cut" operation on the bodies of the workpiece and the tool.

To simulate various machining errors in the program, it is possible to change the values of the geometric parameters of the workpiece and tool and the parameters of the tool path relative to the workpiece. The testing of the suitability of threads with deviations is realized by Boolean operations on the maximum permissible and real bodies. The models of threaded connections constructed with this program can be used to simulate the stress-strain state by the finite element method and justify the values of the thread tolerances.

---

If you use Thread-turning-simulator please cite the following references in your work (books, articles, reports, etc.):

V B Kopei et al 2019 IOP Conf. Ser.: Mater. Sci. Eng. 477 012032 https://doi.org/10.1088/1757-899X/477/1/012032

Kopei V., Onysko O., Panchuk V. (2020) The Application of the Uncorrected Tool with a Negative Rake Angle for Tapered Thread Turning. In: Ivanov V. et al. (eds) Advances in Design, Simulation and Manufacturing II. DSMIE 2019. Lecture Notes in Mechanical Engineering. Springer, Cham. https://doi.org/10.1007/978-3-030-22365-6_15
