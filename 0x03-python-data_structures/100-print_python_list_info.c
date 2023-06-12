#include <Python.h>

/*
 * print_python_list_info - Prints basic info about Python lists
 * @p: pyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, j;
	PyObject *my_obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (j = 0; j < size; j++)
	{
		printf("Element %d: ", j);

		my_obj = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(my_obj)->tp_name);
	}
}
