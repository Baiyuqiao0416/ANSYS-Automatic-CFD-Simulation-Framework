# ANSYS-Automatic-CFD-Simulation-Framework
## This is a demo of the CFD simulation co-operation of the python and the ANSYS Workbench.

List of external packages:  
PyWbUnit  (https://github.com/ansys-dev/PyWbUnit)  
psutil   

The work flow is: 
1.	SCDM change the parameters of the single geometry. The script is generated automatically by the space claim. Because the language of the script is Iron python, we can define several variables, organize and normalize the geometric parameters, and finally modify the parameters in the main program to complete the automatic iteration of the geometry.
2.	Meshing also use the automatically generated script. One thing to note is that the function of automatically generating scripts is only available in ANSYS2021R2. So we need to record the meshing script with the automatically generated geometry. The script of the higher vision still work on lower versions (2019R2) .
3.	After meshing, use the following codes to update the mesh to the fluent.

4.	The fluent script is recorded as journal, but the language of it is scheme.

##output residuals

5.	We can read the residuals.dat to determine if it converges. If not converged, execute the ‘add_iteration.scm’ to add iterations.
6.	After calculation save the project and create a new one.


