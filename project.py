import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def calc_trees(c,r,t):
    """c is the amound of co2 in the atmosphere, r is the rate at which co2 is increasing, t is time. This returns the amount of trees needed."""
    return (c*(r+1)**t)/(t*20)

def test_suite():
    test(calc_trees(1000000,0.05,5) == 12762.815625000005)
    test(calc_trees(50000,0.25,3) == 1627.6041666666667)
    test(calc_trees(250000,0.07,8) == 2684.6659059873764)

test_suite()

co2 = float(input("How many pounds of carbon dioxide are in the atmosphere?"))
rate = float(input("What is the rate at which the amount of carbon dioxide increases in the atmosphere per year?"))
time = float(input("By how many years do you want the amound of carbon dioxide in the atmosphere to be balanced out?"))

print("The amount of trees you need for there to be a safe amount of carbon dioxide in the air in", time, "years is", calc_trees(co2,rate,time))