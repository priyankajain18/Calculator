import simpleguitk as simplegui


#Initialize Global Variables
variable1 = 0;
variable2 = 0;

def input_output():
    print "Input ----->";
    print "Number 1: ", variable1;
    print "Number 2: ", variable2;
    print "Output ----->";

def input1(input1):
    global variable1;
    variable1 = float(input1);

def input2(input2):
    global variable2;
    variable2 = float(input2);

#Division Function
def divide():
    if variable2 != 0:
        input_output();
        print "Result: ", (variable1/variable2);
        return (variable1/variable2);
    else:
        print "Zero Division Error";
        return "Zero Division Error";

#Multiplication Function
def multiply():
    input_output()
    print "Result: ", (variable1 * variable2);
    return (variable1 * variable2);

#Addition Function
def add():
    input_output()
    print "Result: ", (variable1 + variable2);
    return (variable1 + variable2);

#Subtraction Function
def subtract():
    input_output()
    print "Result: ", (variable1 - variable2);
    return (variable1 - variable2);

#Swap Function
def swap():
    input_output()
    variable3, variable4 = variable2, variable1;
    print "Number 1: ", variable3;
    print "Number 2: ", variable4;
    return variable3, variable4;

#Creating Frame
frame = simplegui.create_frame("Calculator", 500, 500);

#Creating Input Fields
frame.add_input("Enter 1st Number", input1, 50);
frame.add_input("Enter 2nd Number", input2, 50);

#Creating Buttons
frame.add_button("Divide", divide, 50);
frame.add_button("Multiply", multiply, 50);
frame.add_button("Add", add, 50);
frame.add_button("Subtract", subtract, 50);
frame.add_button("Swap", swap, 50);

#Initializing Frame
frame.start();