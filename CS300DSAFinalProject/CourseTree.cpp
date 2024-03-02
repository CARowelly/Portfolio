//============================================================================
// Name        : CourseTree.cpp
// Author      : Craig Rowell
// Version     : 1.0
// Copyright   : Copyright © 2017 SNHU COCE
// Description : Project 2 in C++ - Course Binary Search Tree, read, search, sort, print, and modify csv data
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <time.h>
#include <Windows.h>
#include <vector>
#include <conio.h> // for getch

using namespace std;

//============================================================================
// Global definitions visible to all methods and classes
//============================================================================

const int SLEEP_TIME = 2000; // default time for sleep

// define a structure to hold course information
struct Course {
    string courseId;
    string courseName;
    vector<string> prereqs;
};

// Internal structure for tree node
struct Node {
    Course course;
    Node* right;
    Node* left;

    // default constructor
    Node() {
        left = nullptr;
        right = nullptr;
    }

    // initialize with a course
    Node(Course aCourse) :
            Node() {
        this->course = aCourse;
    }
};

//============================================================================
// Course Tree class definition
//============================================================================

/**
 * Define a class containing data members and methods to
 * implement a binary search tree
 */
class CourseTree {

private:
    Node* root;

    void addNode(Node* node, Course course);
    void inOrder(Node* node);
    int size = 0;

public:
    CourseTree();
    virtual ~CourseTree();
    void InOrder();
    void Insert(Course course);
    Course Search(string courseId);
    int Size();
 };

/**
 * Default constructor
 */
CourseTree::CourseTree() {
    // set root to nullptr
    root = nullptr;
}

/**
 * Destructor
 */
CourseTree::~CourseTree() {
    // recurse from root deleting every node
}

/**
 * Traverse the tree in order
 */
void CourseTree::InOrder() {
    // call inOrder function and pass root
    this->inOrder(root);
}

/**
 * Insert a course
 */
void CourseTree::Insert(Course course) {
    // insert course into the tree
    if (root == nullptr) {
        // root is equal to new node course
        root = new Node(course);
    }
    else {
        // add Node root and course
        this->addNode(root, course);
    }
}

/**
* Search for a course
*/
Course CourseTree::Search(string courseId) {
    Node* current = root;

    while (current != nullptr) {
        // if match found, return current course
        if (current->course.courseId == courseId) {
            return current->course;
        }
        // if course is smaller than current node then traverse left
        if (courseId.compare(current->course.courseId) < 0) {
            current = current->left;
        }
        // else larger so traverse right
        else {
            current = current->right;
        }
    }
    Course course;
    return course;
}

/**
* Add a course to some node (recursive)
*
* @param node Current node in tree
* @param Course course to be added
*/
void CourseTree::addNode(Node* node, Course course) {
    // if node is larger then add to left
    if (node->course.courseId.compare(course.courseId) > 0) {
        // if no left node
        if (node->left == nullptr) {
            // this node becomes left
            node->left = new Node(course);
        }
        // else recurse down the left node
        else {
            this->addNode(node->left, course);
        }
    }
    // else
    else {
        // if no right node
        if (node->right == nullptr) {
            // this node becomes right
            node->right = new Node(course);
        }
        //else
        else {
            // recurse down the left node
            this->addNode(node->right, course);
        }
    }
}

void CourseTree::inOrder(Node* node) {
    // if node not equal to nullptr
    if (node != nullptr) {
        //visit all nodes to left
        inOrder(node->left);
        // display data
        cout << node->course.courseId << ", " << node->course.courseName << endl;
        // visit all nodes to right
        inOrder(node->right);
    }
}

/**
 * Display the course information to the console (std::out)
 *
 * Display list of prereqs if any exists
 *
 * @param course struct containing course info
*/
void displayCourse(Course course) {
    cout << course.courseId << ", " << course.courseName << endl;
    cout << "Prerequisites: ";

    if (course.prereqs.empty()) {
        //if the list is empty then there are no prereqs
        cout << "none" << endl;
    }
    else {
        for (unsigned int i = 0; i < course.prereqs.size(); i++) {

            cout << course.prereqs.at(i);

            if (course.prereqs.size() > 1 && i < course.prereqs.size() - 1) {
                //add a comma after each element
                cout << ", ";
            }
        }
    }

    cout << endl;
}

/*
from www.codegrepper.com/code-examples/cpp/c%2B%2B+split+string+by+delimiter
*/
vector<string> Split(string lineFeed) {

    char delim = ',';

    lineFeed += delim; //includes a delimiter at the end so last word is also read
    vector<string> lineTokens;
    string temp = "";
    for (unsigned int i = 0; i < lineFeed.length(); i++)
    {
        if (lineFeed[i] == delim)
        {
            lineTokens.push_back(temp); //store words in token vector
            temp = "";
            i++;
        }
        temp += lineFeed[i];
    }
    return lineTokens;
}

/*
function to load courses
*/
void loadCourses(string csvPath, CourseTree* courseList) {
    // Create a data structure and add to the collection of courses 

    ifstream inFS; //insteam to read file
    string line; //line feed 
    vector<string> stringTokens;

    inFS.open(csvPath); //open the read file

    if (!inFS.is_open()) {//small error handler
        cout << "Could not open file. Please verify file name. " << endl;
        return;
    }

    while (!inFS.eof()) {

        Course course;//create a new struct for each "line"

        getline(inFS, line);
        stringTokens = Split(line); //split the line into tokens via the delimiter

        if (stringTokens.size() < 2) { //if there aren't 2 tokens the line is misformatted

            cout << "No course Id or Name. Skipping line." << endl;
        }

        else {

            course.courseId = stringTokens.at(0);
            course.courseName = stringTokens.at(1);

            for (unsigned int i = 2; i < stringTokens.size(); i++) {

                course.prereqs.push_back(stringTokens.at(i));
            }

            // push this course to the end
            courseList->Insert(course);
        }
    }

    inFS.close(); //close the file
}

int CourseTree::Size() {
    return size;
}

/*
Force the case of passed string to uppercase
Pass the string by reference and change the case of any alpha to upper
*/
void convertCase(string& toConvert) {

    for (unsigned int i = 0; i < toConvert.length(); i++) {

        if (isalpha(toConvert[i])) {

            toConvert[i] = toupper(toConvert[i]);
        }
    }
}

int main(int argc, char* argv[]) {

    // process command line arguments
    string csvPath, courseKey;

    switch (argc) {
    case 2:
        csvPath = argv[1];
        break;
    case 3:
        csvPath = argv[1];
        courseKey = argv[2];
        break;
    default:
        csvPath = "ABCU_Advising_Program_Input.csv";
    }

    // Define a timer variable
    clock_t ticks;

    // Define a table to hold all the courses
    CourseTree* courseList = new CourseTree();
    Course course;

    bool goodInput;
    int choice = 0;
    while (choice != 9) {
        cout << "Menu:" << endl;
        cout << "  1. Load Courses" << endl;
        cout << "  2. Print Course List" << endl;
        cout << "  3. Print Course" << endl;
        cout << "  9. Exit" << endl;
        cout << "Enter choice: ";

        courseKey = ""; //clear the string        
        string anyKey = " "; //clear the string
        choice = 0; //clear the choice

        try {
            choice = _getch()-'0';

            if ((choice > 0 && choice < 5) || (choice == 9)) {// limit the user menu inputs to good values
                goodInput = true;
            }
            else {// throw error for catch
                goodInput = false;
                throw 1;
            }

            switch (choice) {
            case 1:
                // request filename
                cout << "\nEnter file name: ";
                cin >> csvPath;

                // Initialize a timer variale before loading courses
                ticks = clock();
                
                // Complete the method call to load the courses
                loadCourses(csvPath, courseList);

                // Calculate elapsed time and display result
                ticks = clock() - ticks; // current clock ticks minus starting clock ticks
                cout << "time: " << ticks * 1.0 / CLOCKS_PER_SEC << " seconds" << endl;
                Sleep(SLEEP_TIME);
                break;

            case 2:
                courseList->InOrder();

                cout << "\nPress any key to continue..." << endl;
                _getch();

                break;

            case 3:
                cout << "\nEnter Course ID to find course: " << endl;
                cin >> courseKey;

                ticks = clock();

                convertCase(courseKey); //convert the case of user input

                course = courseList->Search(courseKey);

                ticks = clock() - ticks; // current clock ticks minus starting clock ticks

                if (!course.courseId.empty()) {
                    displayCourse(course);
                }
                else {
                    cout << "\nCourse ID " << courseKey << " not found." << endl;
                }

                cout << "time: " << ticks * 1.0 / CLOCKS_PER_SEC << " seconds" << endl;
                cout << "\nPress any key to continue..." << endl;
                _getch();

                break;

            case 9:
                exit(0);
                break;

            default:

                throw 2;
            }
        }

        catch (int error) {

            std::cout << error << "\nInvalid input, press any key to continue..." << endl;
            _getch();

        }

        // clear the cin operator of extra input or any errors generated by bad input
        cin.clear();
        cin.ignore();

        // clear console
        system("cls");
    }

    cout << "Good bye." << endl;

    Sleep(SLEEP_TIME);

    return 0;
}
