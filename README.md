Here are several examples for the triangle drawing functionality in Python.

TriangleDraw.py file shows results by the requirements in task, such as:

    1. Function name “triangle_type” used to give result **def triangle_type(a, b, c):**
        • Try to test the function thoroughly using pytest - Done
        • Code and test only the functionality of triangle type. Drawing of the triangle is not yet expected. - Done
    2. Triangle Draw is a scientific software that has input fields ('A:', 'B:', 'C:').
        In addition, it is given that there is text written below the triangle that states:
        • If the triangle is ‘Equilateral’.(An equilateral triangle has three equal sides)
        • Or the triangle is ‘Isosceles’. (An isosceles triangle has two equal sides)
        • Or the triangle is ‘Scalene’. (A scalene triangle has three different sides)
        • Or state that such a triangle is ‘Not possible’.
---------------------------------------------------------------------------------------------------------------------------------------
Steps to run and check results:
1. TriangleDraw.py contains several scenarios inside, prepared to  be run with pytest library,
   
      First 3 cases test Positive cases to trigger different types of triangles.
            ('"' + triangle_type(3,4,5) + '"' , 'Triangle is Scalene'),
            ('"' + triangle_type(3,5,5) + '"' , 'Triangle is Isosceles.'),
            ('"' + triangle_type(3,3,3) + '"' , 'Triangle is Equilateral.'),
      Next list of cases checks non - numeric values and negative. Last test must check boundary - level tests of the field, but MAX is not presented in requirements so I put random big values.
            ('"' + triangle_type(5464564,456445645,456456456) + '"' , 'Triangle is Scalene'),
      Floating values, as we discussed on call also included:
            ('"' + triangle_type(0.5,0.5,0.5) + '"' , 'Triangle is Equilateral.')

3. ManualTest.py is for manual checking of results. Manually put 3 values to check result
   
5. FakerTest.py is for test automation. It used the external library "Faker" to generate a list of random numbers to be used for triangle calculation.
            for _ in range(15):
              a = fake.random_int(min=0, max=15)
              b = fake.random_int(min=0, max=15)
              c = fake.random_int(min=0, max=15)
              print("a = " + str(a) + " b = " + str(b) + " c = " + str(c) + "  " + triangle_type(a,b,c))

 6. ParameterizingPytest.py present example of parametrized call, not used, it wasn't for me.
