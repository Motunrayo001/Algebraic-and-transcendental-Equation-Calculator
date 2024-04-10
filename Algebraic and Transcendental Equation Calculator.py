from tkinter import*

root = Tk()
Var1 = DoubleVar()
Var2 = DoubleVar()
Var3 = DoubleVar()
Var4 = DoubleVar() 
Var5 = DoubleVar()

def equation():
    Entry7 = Entry(root, textvariable = Var5 )
    Entry7.grid(row = 1, column = 1)
    
def f(x):
    return x**3 - x - 1

def bisection(x0,x1,e):
    if f(x0) * f(x1) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try Again with different guess values.')
        labelans4 = Label(root, text = 'Given guess values do not bracket the root.')
        labelans4.grid()
        labelans5 = Label(root, text = 'Try Again with different guess values.')
        labelans5.grid()
    else:
        step = 1
        print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
        condition = True
        while condition:
            x2 = (x0 + x1)/2
            print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
            labelcalc = Label(root, text ='Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
            labelcalc.grid()

            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2
                step = step + 1
            condition = abs(f(x2)) > e

        print('\nRequired Root is : %0.8f' % x2)
        labelans = Label(root, text = '\nRequired Root is : '+ str(x2))
        labelans.grid()
        
def processBisection():
    bisection(Var1.get(), Var2.get(), Var3.get())

def bisection1():
    Label3 = Label(root, text = "Enter your approximation root 1")
    Label3.grid(row = 5, column = 0)
    
    Entry2 = Entry(root, textvariable = Var1 )
    Entry2.grid(row = 5, column = 1)

    Label3 = Label(root, text = "Enter your approximation root 2")
    Label3.grid(row = 6, column = 0)

    Entry3 = Entry(root, textvariable = Var2)
    Entry3.grid(row = 6, column = 1)

    Label3 = Label(root, text = "Error")
    Label3.grid(row = 7, column = 0)

    Entry4 = Entry(root, textvariable = Var3)
    Entry4.grid(row = 7, column = 1)

    Button3 = Button(None, text = "ENTER", fg = "Blue", command = processBisection )
    Button3.grid(row = 8, column = 3)


def newraphOk():
    #NEWTON RAPHSON METHOD
    # Defining Function
    def f(x):
        return x**3 - x - 1

    # Defining derivative of function
def g(x):
        return 3*(x**2) - 1

    # Implementing Newton Raphson Method

def newtonRaphson(x0,e,N):
        print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
        step = 1
        flag = 1
        condition = True
        while condition:
            if g(x0) == 0.0:
                print('Divide by zero error!')
                break

            x1 = x0 - f(x0)/g(x0)
            print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
            labelans7 = Label(root, text = 'Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
            labelans7.grid()
            x0 = x1
            step = step + 1
            
            if step > N:
                flag = 0
                break
            
            condition = abs(f(x1)) > e
        
        if flag==1:
            print('\nRequired root is: %0.8f' % x1)
            labelans1 = Label(root, text = '\nRequired Root is : '+ str(x1))
            labelans1.grid()
        else:
            print('\nNot Convergent.')
            labelans3 = Label(root, text = '\nNOT CONVERGENT.' )
            labelans3.grid()
        


def processNewtonRaphson():
    newtonRaphson(Var1.get(), Var2.get(), Var3.get())

def newtonraphson1():
    Label2 = Label(root, text = "Enter your approximation root")
    Label2.grid(row = 5, column = 0)

    Entry2 = Entry(root, textvariable = Var1 )
    Entry2.grid(row = 5, column = 1)

    Label3 = Label(root, text = "Error")
    Label3.grid(row = 6, column = 0)

    Entry3 = Entry(root, textvariable = Var2 )
    Entry3.grid(row = 6, column = 1)

    Label4 = Label(root, text = "Maximum Step")
    Label4.grid(row = 7, column = 0)

    Entry4 = Entry(root, textvariable = Var3 )
    Entry4.grid(row = 7, column = 1)

    Button3 = Button(None, text = "ENTER", fg = "Blue", command = processNewtonRaphson)
    Button3.grid(row = 8, column = 3)

def secantOk():
        # Defining Function
    def f(x):
        return x**3 - x - 1

    # Implementing Secant Method

def secant(x0,x1,e,N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
            
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        labelans8 = Label(root, text = 'Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        labelans8.grid()
        x0 = x1
        x1 = x2
        step = step + 1
            
        if step > N:
            print('Not Convergent!')
            labelans6 = Label(root, text = 'NOT CONVERGENT!')
            labelans6.grid()
            break
            
        condition = abs(f(x2)) > e
    print('\n Required root is: %0.8f' % x2)
    labelans2 = Label(root, text = '\nRequired Root is : '+ str(x2))
    labelans2.grid()
        


def processSecant():
    secant(Var1.get(), Var2.get(), Var3.get(), Var4.get())

def secant1():
    Label2 = Label(root, text = "Enter your approximation root 1")
    Label2.grid(row = 5, column = 0)

    Entry2 = Entry(root, textvariable = Var1 )
    Entry2.grid(row = 5, column = 1)

    Label3 = Label(root, text = "Enter your approximation root 2")
    Label3.grid(row = 6, column = 0)

    Entry3 = Entry(root, textvariable = Var2 )
    Entry3.grid(row = 6, column = 1)

    Label4 = Label(root, text = "ERROR")
    Label4.grid(row = 7, column = 0)

    Entry4 = Entry(root, textvariable = Var3 )
    Entry4.grid(row = 7, column = 1)

    Label5 = Label(root, text = "MAXIMUM STEP")
    Label5.grid(row = 8, column = 0)

    Entry5 = Entry(root, textvariable = Var4 )
    Entry5.grid(row = 8, column = 1)

    Button3 = Button(None, text = "ENTER", fg = "Blue", command = processSecant )
    Button3.grid(row = 8, column = 3)
    
def main():
    Label1 = Label(root, text = "ALGEBRAIC AND TRANSCENDENTAL EQUATIONS" )
    Label1.grid(row = 0, column = 1)

    Button5 = Button(None,text = "ENTER YOUR EQUATION" , fg = "Blue", command = equation)
    Button5.grid(row = 1, column = 0)

    Button1 = Button(None, text = "BISECTION METHOD", fg = "Blue" ,command = bisection1)
    Button1.grid(row = 3, column = 0)

    Button2 = Button(None, text = "NEWTON RAPHSON METHOD", fg = "Blue", command = newtonraphson1)
    Button2.grid(row = 3, column = 1)

    Button3 = Button(None, text = "SECANT METHOD", fg = "Blue", command = secant1)
    Button3.grid(row = 3, column = 3)

main()
