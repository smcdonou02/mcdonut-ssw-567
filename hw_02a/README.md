# mcdonut-ssw-567
## Assignment Description
The objective of this assignment is for you to (a) develop a set of tests for an existing triangle classification program, (b) use those tests to find and fix defects in that program, and (c) report on your testing results for the Triangle problem

Description of assignment:

Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program.   In this assignment you will start with an existing implementation of the classify triangle program that will be given to you.   You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.  

These are the two files:  Triangle.py and TestTriangle.py
Triangle.py is a starter implementation of the triangle classification program.  
TestTriangle.py  contains a starter set of unittest test cases to test the classifyTriangle() function in the file Triangle.py file.   
In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program.  You will need to update the test program until you feel that your tests adequately test all of the conditions.   Then you should run the complete set of tests against the original triangle program to see how correct the triangle program is.    Capture and then report on those results in a formal test report described below.   For this first part you should not make any changes to the classify triangle program.  You should only change the test program.

Based on the results of your initial tests, you will then update the classify triangle program to fix all defects.  Continue to run the test cases as you fix defects until all of the defects have been fixed.   Run one final execution of the test program and capture and then report on those results in a formal test report described below.   

Note that you should NOT simply replace the logic with your logic from Assignment 1.  Test teams typically don't have the luxury of rewriting code from scratch and instead must fix what's delivered to the test team.   

Triangle.py contains an implementation of the classifyTriangle() function with a few bugs.  

TestTriangle.py contains the initial set of test cases
## Author
Stephanie McDonough

## Summary
- a summary of your results

- reflection -- this is where you actually think about the assignment after it is over -- what did you learn? What worked, what didn't?

## Honor Pledge
I pledge my honor that I have abided by the Stevens Honor System. - SAM

## Detailed Results 

### Test Report 1 

| Test ID  |  Input  | Expected Results | Actual Result | Pass or Fail |
| -------- | ------- | ---------------- | ------------- | ------------ |
| testRight1 | classifyTriangle(3,4,5) | 'Right' | 'InvalidInput' | Fail |
| testRight2 | classifyTriangle(5,3,4) | 'Right' | 'InvalidInput' | Fail |
| testEquilateral | classifyTriangle(1,1,1) | 'Equilateral' | 'InvalidInput' | Fail |
| testScalene | classifyTriangle(5,7,9) | 'Scalene' | 'InvalidInput' | Fail |
| testIsoceles | classifyTriangle(5,5,10) | 'Isoceles' | 'InvalidInput' | Fail |
| testInvalid200A | classifyTriangle(201,4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalid200B | classifyTriangle(3,201,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalid200C | classifyTriangle(3,4,201) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegA | classifyTriangle(-3,4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegB | classifyTriangle(3,-4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegC | classifyTriangle(3,4,-5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntA | classifyTriangle("3",4,5) | 'InvalidInput' | TypeError: '>' not supported between instances of 'str' and 'int' | Fail |
| testInvalidNotIntB | classifyTriangle(3,"4",5) | 'InvalidInput' | TypeError: '>' not supported between instances of 'str' and 'int' | Fail |
| testInvalidNotIntC | classifyTriangle(3,4,"5") | 'InvalidInput' | TypeError: '>' not supported between instances of 'str' and 'int' | Fail |

### Test Report 2
| Test ID  |  Input  | Expected Results | Actual Result | Pass or Fail |
| -------- | ------- | ---------------- | ------------- | ------------ |
| testRight1 | classifyTriangle(3,4,5) | 'Right' | 'Right' | Pass |
| testRight2 | classifyTriangle(5,3,4) | 'Right' | 'Right' | Pass |
| testEquilateral | classifyTriangle(1,1,1) | 'Equilateral' | 'Equilateral' | Pass |
| testScalene | classifyTriangle(5,7,9) | 'Scalene' | 'NotATriangle' | Fail |
| testIsoceles | classifyTriangle(5,5,10) | 'Isoceles' | 'NotATriangle' | Fail |
| testInvalid200A | classifyTriangle(201,4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalid200B | classifyTriangle(3,201,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalid200C | classifyTriangle(3,4,201) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegA | classifyTriangle(-3,4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegB | classifyTriangle(3,-4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegC | classifyTriangle(3,4,-5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntA | classifyTriangle("3",4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntB | classifyTriangle(3,"4",5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntC | classifyTriangle(3,4,"5") | 'InvalidInput' | 'InvalidInput' | Pass |

### Test Report 3
| Test ID  |  Input  | Expected Results | Actual Result | Pass or Fail |
| -------- | ------- | ---------------- | ------------- | ------------ |
| testRight1 | classifyTriangle(3,4,5) | 'Right' | 'Right' | Pass |
| testRight2 | classifyTriangle(5,3,4) | 'Right' | 'Right' | Pass |
| testEquilateral | classifyTriangle(1,1,1) | 'Equilateral' | 'Equilateral' | Pass |
| testScalene | classifyTriangle(5,7,9) | 'Scalene' | 'NotATriangle' | Fail |
| testIsoceles | classifyTriangle(5,5,10) | 'Isoceles' | 'NotATriangle' | Fail |
| testInvalid200A | classifyTriangle(201,4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalid200B | classifyTriangle(3,201,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalid200C | classifyTriangle(3,4,201) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegA | classifyTriangle(-3,4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegB | classifyTriangle(3,-4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegC | classifyTriangle(3,4,-5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntA | classifyTriangle("3",4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntB | classifyTriangle(3,"4",5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntC | classifyTriangle(3,4,"5") | 'InvalidInput' | 'InvalidInput' | Pass |

### Test Report 4
| Test ID  |  Input  | Expected Results | Actual Result | Pass or Fail |
| -------- | ------- | ---------------- | ------------- | ------------ |
| testRight1 | classifyTriangle(3,4,5) | 'Right' | 'Right' | Pass |
| testRight2 | classifyTriangle(5,3,4) | 'Right' | 'Right' | Pass |
| testEquilateral | classifyTriangle(1,1,1) | 'Equilateral' | 'Equilateral' | Pass |
| testScalene | classifyTriangle(5,7,9) | 'Scalene' | 'Scalene' | Pass |
| testIsoceles | classifyTriangle(5,5,10) | 'Isoceles' | 'Isoceles' | Pass |
| testInvalid200A | classifyTriangle(201,4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalid200B | classifyTriangle(3,201,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalid200C | classifyTriangle(3,4,201) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegA | classifyTriangle(-3,4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegB | classifyTriangle(3,-4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNegC | classifyTriangle(3,4,-5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntA | classifyTriangle("3",4,5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntB | classifyTriangle(3,"4",5) | 'InvalidInput' | 'InvalidInput' | Pass |
| testInvalidNotIntC | classifyTriangle(3,4,"5") | 'InvalidInput' | 'InvalidInput' | Pass |
| testNotValid1 | classifyTriangle(5,5,10) | 'NotATriangle' | 'NotATriangle' | Pass |
| testNotValid2 | classifyTriangle(5,2,12) | 'NotATriangle' | 'NotATriangle' | Pass |
| testNoInput1 | classifyTriangle(None,None,None) | TypeError("Three inputs required") |  TypeError("Three inputs required") | Pass |
| testNoInput2 | classifyTriangle() | TypeError("Three inputs required") |  TypeError("Three inputs required") | Pass |

### Test Case Summary Matrix + Strategy
|                | Test Run 1 | Test Run 2 | Test Run 3 | Test Run 4 |
| --- | --- | ---- | --- | --- |
| Tests Planned  | 12 | 14 | 14 | 18 |
| Tests Executed | 12 | 14 | 14 | 18 |
| Tests Passed   | 6 | 6 | 12 | 18 |
| Defects Found  | 3 | 5 | 0 | 0 |
| Defects Fixed  | 0 | 0 | 5 | 0 |

