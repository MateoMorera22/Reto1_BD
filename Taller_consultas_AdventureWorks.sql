---1

select FirstName,LastName from Person.Person where FirstName = 'Mark' 

----2 

select COUNT(*) as 'Numero Filas Person.Person' 

from [Person].[Person] 

  

--3 

SELECT top(100)* 

from [Production].[Product] 

where ListPrice>0 

  

--4 

select * from [HumanResources].[vEmployee] 

where LastName like '[a-c]%' 

  

--5 

select p.Name, avg(StandardCost) as promedio  

from [Production].[Product] as p 

where [StandardCost]>0 

group by p.Name 

  

--6 

select PersonType, COUNT(*)  

from [Person].[Person]  

group by PersonType  

  
  

--7 

select *  

from [Person].[StateProvince] 

where [CountryRegionCode] ='CA' 


----8 

select Color,COUNT(*) as 'cantidad_color' 

from [Production].[Product] as c 

where (Color='Red' or Color='Black')  

group by Color 


---9 

select avg([Freight]) as 'Promedio_de_venta' 

from [Sales].[SalesOrderHeader] 

where [TerritoryID] = 4 


--10 

select * from  

Sales.vIndividualCustomer  

where (LastName = 'Lopez' or LastName = 'Martin' or LastName = 'Wood' 

or vIndividualCustomer.FirstName Between 'C' and 'L') 

 
--11 

Select FirstName as 'Nombre',LastName as 'Apellido' 

from Sales.vIndividualCustomer 

where LastName = 'Smith' 

 
--12 

select * from  

Sales.vIndividualCustomer  

where (CountryRegionName = 'Australia' or PhoneNumberType = 'Cell'  

or EmailPromotion='0') 

 
--13 

select MAX(Production.Product.ListPrice) as 'Producto mas caro' 

from Production.Product 

 
--14 

select TotalDue, TerritoryID    

from Sales.SalesOrderHeader 

where [TotalDue]>1000 

Order by TerritoryID 

 
--15 

select TotalDue, Sales.SalesTerritory.Name   

from Sales.SalesOrderHeader 

inner join Sales.SalesTerritory 

on sales.SalesOrderHeader.TerritoryID = Sales.SalesOrderHeader.TerritoryID 

where [TotalDue]>100 

 
--16 

select *  

from HumanResources.vEmployeeDepartment 

where (Department = 'Executive' or Department = 'Tool Design' 

or Department = 'Engineering' 

) 

 
--17 

select * 

from HumanResources.vEmployeeDepartment 

where (StartDate Between '2000-07-01' and '2002-06-30' ) 

 
--18 

select *  

from Sales.SalesOrderHeader 

where SalesPersonID is not null 

 
--19 

select COUNT(MiddleName) as 'Numero de registros sin Null' 

from Person.Person 

where MiddleName is not null 

 
--20 

Select SalesPersonID,TotalDue 

from sales.SalesOrderHeader 

where (SalesPersonID is not null and TotalDue>70000) 

 
--21 

Select * 

from sales.vIndividualCustomer  

where FirstName like 'R%' 

 
--22 

Select * 

from sales.vIndividualCustomer  

where LastName like '%R' 

 

 
---23 

select Color,COUNT(*) as 'num_resgistros' 

from Production.Product 

where (Color is not null) 

group by Color 

having COUNT(*)>20 


-- 32  

select ProductID,Color= 

case 

when Color is Not null then Color 

when Color is null then 'sin color' 

end 

from [Production].[Product] 

  