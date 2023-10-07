#include <Python.h>
#include <object.h>
#include <listobject.h>
/*
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	
	printf("[*] Size of the Python List = %zd\n", Py_SIZE(list));
	printf("[*] Allocated = %zd\n", list->allocated);
	
	for (Py_ssize_t i = 0; i < Py_SIZE(list); i++)
	{
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem
					(list, i))->tp_name);
	}
}
