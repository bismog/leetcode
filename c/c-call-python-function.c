#include <Python.h>

int main()
{
 PyObject *TankModule = NULL;
 PyObject *TankDict = NULL;
 PyObject *TankClassObj = NULL;
 PyObject *ForwardFuncObj = NULL;
 PyObject *TankObject = NULL;
 Py_Initialize();
//import module
 TankModule = PyImport_ImportModule("tank");
 TankClassObj = PyDict_GetItemString(TankDict, "Tank");
 TankObject = PyObject_Call(TankClassObj, NULL, NULL);
 PyObject_CallMethod(TankObject, "forward", NULL);
 Py_Finalize();
 return 0;
}
