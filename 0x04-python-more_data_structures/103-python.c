#include <Python.h>

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the Python list object.
 * Return: void
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %zd bytes:", (size < 10 ? size + 1 : 10));
	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", (unsigned char)string[i]);
	printf("\n");
}
