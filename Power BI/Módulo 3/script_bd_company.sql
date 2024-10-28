CREATE TABLE employee (
    fname VARCHAR(50),
    minit CHAR(1),
    lname VARCHAR(50),
    ssn INT PRIMARY KEY,
    bdate DATE,
    address VARCHAR(100),
    sex CHAR(1),
    salary DECIMAL(10, 2),
    superssn INT,
    dno INT
);
CREATE TABLE dependent (
    essn INT,
    dependent_name VARCHAR(50),
    sex CHAR(1),
    bdate DATE,
    relationship VARCHAR(50),
    FOREIGN KEY (essn) REFERENCES employee(ssn)
);
CREATE TABLE departament (
    dname VARCHAR(50),
    dnumber INT PRIMARY KEY,
    mgrssn INT,
    mgrstartdate DATE,
    mgrbirthdate DATE,
    FOREIGN KEY (mgrssn) REFERENCES employee(ssn)
);
CREATE TABLE dept_locations (
    dnumber INT,
    dlocation VARCHAR(50),
    FOREIGN KEY (dnumber) REFERENCES departament(dnumber)
);
CREATE TABLE project (
    pname VARCHAR(50),
    pnumber INT PRIMARY KEY,
    plocation VARCHAR(50),
    dnum INT,
    FOREIGN KEY (dnum) REFERENCES departament(dnumber)
);
CREATE TABLE works_on (
    essn INT,
    pno INT,
    hours DECIMAL(5, 1),
    FOREIGN KEY (essn) REFERENCES employee(ssn),
    FOREIGN KEY (pno) REFERENCES project(pnumber)
);
