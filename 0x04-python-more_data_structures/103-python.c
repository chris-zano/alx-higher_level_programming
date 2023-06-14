#include <Python.h>

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;
	PyObject *list_type = PyObject_Type(p);
	PyObject *allocated_att;
	Py_ssize_t allocated;

	printf("[*] Python list info\n");

	size = PyObject_Length(p);
	printf("[*] Size of the Python List = %zd\n", size);

	if (list_type && PyType_Check(list_type))
	{
		allocated_att = PyObject_GetAttrString(list_type, "allocated");
		allocated = PyLong_AsSsize_t(allocated_att);
		Py_DECREF(list_type);
		Py_XDECREF(allocated_att);

		if (allocated >= 0)
			printf("[*] Allocated = %zd\n", allocated);
		else
			printf("[*] Failed to retrieve the
					'allocated' attribute\n");
	}
	else
		printf("[*] Failed to retrieve the list type\n");

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyObject_Length(p);
	string = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %zd bytes:", (size < 10 ? size + 1 : 10));
	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", (unsigned char)string[i]);
	printf("\n");
}

