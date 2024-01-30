#define PY_SSIZE_T_CLEAN
#include <Python.h>

#if PY_VERSION_HEX < 0x03040000
#define PyUnicode_GET_LENGTH PyUnicode_GET_SIZE
#endif

/**
 * print_python_string - Function that prints
 *  information about Python strings
 * @p: PyObject representing a Python string
 *
 * Description: This function prints information about
 *  Python string objects,
 * including type, length, and value.
 */

void print_python_string(PyObject *p)
{
    if (!Py_IS_TYPE(p, &PyUnicode_Type)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    fflush(stdout);

    /* Print header for string object information */
    printf("[.] string object info\n");

    /* Extract the length of the string */
    Py_ssize_t str_length = PyUnicode_GET_LENGTH(p);

    /* Check if the string is a compact ASCII or compact Unicode object */
    if (PyUnicode_IS_READY(p) && PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    /* Print the length of the string */
    printf("  length: %ld\n", (long)str_length);

    /* Print the value of the string */
    const char *utf8_str = PyUnicode_AsUTF8(p);
    if (utf8_str) {
        printf("  value: %s\n", utf8_str);
    } else {
        printf("  value: <not available>\n");
    }
}
