import stafflib as lib
lib.newEmployee(Fn="Daniel",Ln="Huang",Age="17",Since="1998",Salary="10",Role="none",Days=1)
lib.newEmployee(Fn="A",Ln="a",Age="12",Since="1234",Salary="11111",Role="A",Days=2)
lib.newEmployee(Fn="B",Ln="b",Age="34",Since="2345",Salary="22222",Role="B",Days=3)
lib.newEmployee(Fn="C",Ln="c",Age="56",Since="3456",Salary="33333",Role="C",Days=4)
lib.newEmployee(Fn="someone",Ln="else",Age="100",Since="1916",Salary="1000000",Role="something",Days=5)

lib.showEmployee()
lib.showEmployee()

lib.deleteEmployees(3)
lib.showEmployee()
