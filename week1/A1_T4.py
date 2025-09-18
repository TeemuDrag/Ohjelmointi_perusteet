#Arvon määrittäminen muuttujalle 47Num1
#Arvon määrittäminen muuttujalle 102Num2
#Summaa muuttujat ja , ja laita tulos muuttujaanNum1Num2Sum
#Vähennä ja tallenna tulos muuttujaan.Num1Num2Diff
#Kerro ja ja aseta sitten saatu tuote .SumDiffProduct
#Tulosta summaoperaatio ""{Num1} + {Num2} = {Sum}
#Tulosta alitoiminto ""{Num2} - {Num1} = {Diff}
#Tulosta kertolaskutoiminto ""{Sum} * {Diff} = {Product}
#Tulosta summa-, ali- ja kertolaskutoiminnot yhdessä. Katso "ohjelman ajo" alta.
num1 = 47
num2 = 102
Sum = num1 + num2
Diff = num2 - num1
print(num1,"+",num2,"=", Sum)
print(num2,"-",num1,"=", Diff)
print( Sum,"*",Diff,"=",Sum * Diff)
print("(" ,num1,"+",num2,") * (",num2,"-",num1,") =",(Sum * Diff))
