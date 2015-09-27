import simpleguitk as simplegui


variable1 = 0;
variable2 = 0;

def input():
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

def divide():
    input();
    print "Result: ", (variable1/variable2);
    return (variable1/variable2);

def multiply():
    input();
    print "Result: ", (variable1 * variable2);
    return (variable1 * variable2);

def add():
    input();
    print "Result: ", (variable1 + variable2);
    return (variable1 + variable2);

def subtract():
    input();
    print "Result: ", (variable1 - variable2);
    return (variable1 - variable2);

def swap():
    input();
    variable3, variable4 = variable2, variable1;
    print "Number 1: ", variable3;
    print "Number 2: ", variable4;
    return variable3, variable4;

frame = simplegui.create_frame("Calculator", 500, 500);

frame.add_input("Enter 1st Number", input1, 50);
frame.add_input("Enter 2nd Number", input2, 50);

frame.add_button("Divide", divide, 50);
frame.add_button("Multiply", multiply, 50);
frame.add_button("Add", add, 50);
frame.add_button("Subtract", subtract, 50);
frame.add_button("Swap", swap, 50);

frame.start();