from example12 import EmployeeFactory


def cloned_main():
    """主函数"""
    cloned_emps = [
        EmployeeFactory.cloned_create('M', '曹操'), 
        EmployeeFactory.cloned_create('P', '荀彧', 120),
        EmployeeFactory.cloned_create('P', '郭嘉', 85), 
        EmployeeFactory.cloned_create('S', '典韦', 123000),
    ]
    for cloned_emp in cloned_emps:
        print('%s: %.2f元' % (cloned_emp.name, cloned_emp.cloned_get_salary()))


if __name__ == '__main__':
    cloned_main()