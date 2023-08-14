#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print information about a Python list object.
 * @p: The Python list object.
 *
 * This function prints various information about a Python list object.
 * It displays the size of the list, the number of allocated slots, and
 * the type of each element in the list.
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
