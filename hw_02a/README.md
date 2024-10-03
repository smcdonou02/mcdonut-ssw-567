# mcdonut-ssw-567
## Test Report

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

## Test Case Summary Matrix + Strategy
|                | Test Run 1 | Test Run 2 | | |
| --- | --- | ---- | --- | --- |
| Tests Planned  | 14 | | | |
| Tests Executed | 14 | | | |
| Tests Passed   | 6 | | | |
| Defects Found  | 4 | | | |
| Defects Fixed  | 4 | | | |

