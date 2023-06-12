#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - a C function that
 * prints some basic info about Python lists.
 *
 * @p: pointer to a python object (list)
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	PyObject *item;
	PyTypeObject *type;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = item->ob_type;
		printf("Element %zd: %s\n", i, type->tp_name);
	}
}
