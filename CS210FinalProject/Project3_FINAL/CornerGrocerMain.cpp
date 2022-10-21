// Main.cpp
// 7 - 1 Project 3: Corner Grocer App
// SNHU CS - 210
// 2022 / 04 / 15
// Craig Rowell

#include <Python.h>
#include <iostream>
#include <iomanip>
#define NOMINMAX
#include <Windows.h>
#undef NOMINMAX
#include <cmath>
#include <string>
#include <fstream>

using namespace std;

/*
Description:
	To call this function, simply pass the function name in Python that you wish to call.
Example:
	callProcedure("printsomething");
Output:
	Python will print on the screen: Hello from python!
Return:
	None
*/
void CallProcedure(string pName)
{
	char* procname = new char[pName.length() + 1];
	strcpy(procname, pName.c_str());

	Py_Initialize();
	PyObject* my_module = PyImport_ImportModule("CornerGrocerPythonCode");
	PyErr_Print();
	PyObject* my_function = PyObject_GetAttrString(my_module, procname);
	PyObject* my_result = PyObject_CallObject(my_function, NULL);
	Py_Finalize();

	delete[] procname;
}

/*
Description:
	To call this function, pass the name of the Python function you wish to call and the string parameter you want to send
Example:
	int x = callIntFunc("PrintMe","Test");
Output:
	Python will print on the screen:
		You sent me: Test
Return:
	100 is returned to the C++
*/
int callIntFunc(string proc, string param)
{
	char* procname = new char[proc.length() + 1];
	strcpy(procname, proc.c_str());

	char* paramval = new char[param.length() + 1];
	strcpy(paramval, param.c_str());


	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	// Initialize the Python Interpreter
	Py_Initialize();
	// Build the name object
	pName = PyUnicode_FromString((char*)"CornerGrocerPythonCode");
	// Load the module object
	pModule = PyImport_Import(pName);
	// pDict is a borrowed reference 
	pDict = PyModule_GetDict(pModule);
	// pFunc is also a borrowed reference
	pFunc = PyDict_GetItemString(pDict, procname);
	if (PyCallable_Check(pFunc))
	{
		pValue = Py_BuildValue("(z)", paramval);
		PyErr_Print();
		presult = PyObject_CallObject(pFunc, pValue);
		PyErr_Print();
	}
	else
	{
		PyErr_Print();
	}
	//printf("Result is %d\n", _PyLong_AsInt(presult));
	Py_DECREF(pValue);
	// Clean up
	Py_DECREF(pModule);
	Py_DECREF(pName);
	// Finish the Python Interpreter
	Py_Finalize();

	// clean 
	delete[] procname;
	delete[] paramval;


	return _PyLong_AsInt(presult);
}

/*
Description:
	To call this function, pass the name of the Python function you wish to call and the string parameter you want to send
Example:
	int x = callIntFunc("doublevalue",5);
Return:
	25 is returned to the C++
*/
int callIntFunc(string proc, int param)
{
	char* procname = new char[proc.length() + 1];
	strcpy(procname, proc.c_str());
	
	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	// Initialize the Python Interpreter
	Py_Initialize();
	// Build the name object
	pName = PyUnicode_FromString((char*)"CornerGrocerPythonCode");
	// Load the module object
	pModule = PyImport_Import(pName);
	// pDict is a borrowed reference 
	pDict = PyModule_GetDict(pModule);
	// pFunc is also a borrowed reference 
	pFunc = PyDict_GetItemString(pDict, procname);
	if (PyCallable_Check(pFunc))
	{
		pValue = Py_BuildValue("(i)", param);
		PyErr_Print();
		presult = PyObject_CallObject(pFunc, pValue);
		PyErr_Print();
	}
	else
	{
		PyErr_Print();
	}
	//printf("Result is %d\n", _PyLong_AsInt(presult));
	Py_DECREF(pValue);
	// Clean up
	Py_DECREF(pModule);
	Py_DECREF(pName);
	// Finish the Python Interpreter
	Py_Finalize();

	// clean 
	delete[] procname;

	return _PyLong_AsInt(presult);
}


/*
This function produces a menu to prompt user input between 1 and 4.
User input then executes the corresponding Python function.
		~1 outputs a list of items and the number of times they appear in the list
		~2 searches for the number of an individual item
		~3 will print a histogram of each item
		~4 quits the program
*/
void MainMenu() {

	// initializes local variables
	int loopMainMenu = 0;									// tracks the number of menu loops
	int matches = 0;										// tracks the number of times the searched item was found
	int quantityPurchased = 0;								// contains an item quantity from frequency.dat
	string searchForItem;									// collects user input for an item to search
	string itemPurchased;									// contains an item name from frequency.dat
	ifstream fileInput;										// opens ifstream for file

	while (loopMainMenu != 4) {

		// prompts user to choose an action
		cout << "[1] Calculate the number of times each item appears\n";
		cout << "[2] Calculate the frequency of a specific item\n";
		cout << "[3] Create a histogram based on the number of appearances of each item\n";
		cout << "[4] Exit\n";

		cin >> loopMainMenu;

		// input validation
		while (cin.fail()) {
			cin.clear();
			cin.ignore(numeric_limits<streamsize>::max(), '\n');
			cout << "Please input a valid selection: ";
			cin >> loopMainMenu;
		}


		// switch statement that executes the proper command for user input
		switch (loopMainMenu) {


		// produces a list of all items and how many were purchased that day
		case 1:
			system("CLS");									// clears the screen
			CallProcedure("CountAllItems");					// calls the Python function "CountAllItems"
			cout << endl;							// newline
			break;

			
		// produces a number representing how many times a specific item were purhased that day		
		case 2:
			// clears the screen and collects user input
			system("CLS");
			cout << "What item would you like to search for?\n";
			cin >> searchForItem;

			// calls the Python function with the search term, then return an integer word count value
			matches = callIntFunc("CountInstances", searchForItem);

			if (matches > 0) {
				// prints returned item count.
				cout << endl << searchForItem << " : " << matches << endl << endl;
				//system("pause");									// pause to display results
			}
			else {
				cout << "\nNo " << searchForItem << " was purchased today.\n\n";
			}
			break;

			
		// produces a text-based histogram listing all items purchased that day along with a representation 
		// of the number of times each item was purchased
		case 3:
			system("CLS");											// clears the screen
			CallProcedure("RecordData");							// calls the Python function "RecordData"

			fileInput.open("frequency.dat");						// opens the frequency.dat file

			fileInput >> itemPurchased;								// collects the first item on the list
			fileInput >> quantityPurchased;							// collects the first quantity on the list

			// prints a histogram for each line in the file
			while (!fileInput.fail()) {

				// prints the item and formats for the histogram
				cout << setw(14) << left << itemPurchased << setw(6);

				// prints a number of asterisks equal to quantityPurchased
				for (int i = 0; i < quantityPurchased; i++) {

					// prints asterisks
					cout << right << "*";
				}
				// endline then set the next item's name and quantity.
				cout << endl;
				fileInput >> itemPurchased;
				fileInput >> quantityPurchased;
			}

			// closes frequency.dat
			fileInput.close();
			break;

			
		// exits the program
		case 4:
			continue;

			// input validation
		default:
			cout << "Please input a valid selection.\n";
			break;
		}
	}
}

// main calls the MainMenu method to collect user input.
int main()
{
	// calls main menu method
	MainMenu();
	return 0;
}