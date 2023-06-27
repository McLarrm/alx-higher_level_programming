#include <Python.h>
#include <floatobject.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: The PyObject pointer representing the list object
 */
void print_python_list(PyObject *p)
{
	const char *elementType = Py_TYPE(element)->tp_name;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, elementType);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: The PyObject pointer representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	const char *bytesString = PyBytes_AsString(p);

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);

	printf("[.] Bytes object info\n");
	printf("  [.] Size: %zd\n", size);
	printf("  [.] Trying string: %s\n", bytesString);
	printf("  [.] First %zd bytes: ", (size < 10) ? size : 10);

	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)bytesString[i]);
		if (i < size - 1 && i < 9)
			printf(" ");
	}

	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: The PyObject pointer representing the float object
 */
void print_python_float(PyObject *p)
{
	double value = PyFloat_AsDouble(p);

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	printf("[.] Float object info\n");

	printf("  [.] value: %.17g\n", value);
}
