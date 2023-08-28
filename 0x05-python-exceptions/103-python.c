#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints info about python list
 * @p: A python List object
 * Return: void 
 */
void print_python_list(PyObject *p)
{
    fflush(stdout);
    
    if (!p){
        printf("  [ERROR] Invalid List Object\n");
        return;
    }
    else
    {
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %d", )
    }
}