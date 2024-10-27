USE universidade;

-- Tabela Dimensão: Dim_Professor
CREATE TABLE Dim_Professor (
    ID_Professor INT PRIMARY KEY,
    Nome VARCHAR(50),
    Sobrenome VARCHAR(50),
    Titulacao VARCHAR(20),
    Especialidade VARCHAR(50)
);

-- Tabela Dimensão: Dim_Curso
CREATE TABLE Dim_Curso (
    ID_Curso INT PRIMARY KEY,
    Nome_Curso VARCHAR(100),
    Categoria VARCHAR(20),
    Modalidade VARCHAR(20)
);

-- Tabela Dimensão: Dim_Departamento
CREATE TABLE Dim_Departamento (
    ID_Departamento INT PRIMARY KEY,
    Nome_Departamento VARCHAR(100),
    Faculdade VARCHAR(100)
);

-- Tabela Dimensão: Dim_Data
CREATE TABLE Dim_Data (
    ID_Data INT PRIMARY KEY,
    Data DATE,
    Ano INT,
    Mes INT,
    Dia INT,
    Semestre INT,
    Trimestre INT,      
    Semana INT               
);

-- Tabela Fato: Fato_Professor
CREATE TABLE Fato_Professor (
    ID_Fato_Professor INT PRIMARY KEY,
    ID_Professor INT,
    ID_Curso INT,
    ID_Departamento INT,
    ID_Data INT,
    Carga_Horaria FLOAT,
    Num_Alunos_Inscritos INT,
    Avaliacoes_Media FLOAT,
    FOREIGN KEY (ID_Professor)
        REFERENCES Dim_Professor (ID_Professor),
    FOREIGN KEY (ID_Curso)
        REFERENCES Dim_Curso (ID_Curso),
    FOREIGN KEY (ID_Departamento)
        REFERENCES Dim_Departamento (ID_Departamento),
    FOREIGN KEY (ID_Data)
        REFERENCES Dim_Data (ID_Data)
);