# Data Science Python Project

A collection of Python scripts for data manipulation, database operations, and file generation (Excel, PDF) using student and faculty data.

## Project Files

### Core Database Files

#### `database.py`
- **Purpose**: SQLite database operations with student data
- **Features**:
  - Creates and manages SQLite database (`students.db`)
  - Inserts student records (5 students with id, name, age, marks)
  - Sorts students by age (ascending and descending)
  - Calculates mean marks
  - Converts database data to Pandas DataFrame
- **Usage**: `python database.py`

#### `database2.py`
- **Purpose**: Similar to `database.py`
- **Features**: Same functionality as database.py

#### `faculty.py`
- **Purpose**: Faculty database management with salary calculations
- **Features**:
  - Creates SQLite `faculty.db` database
  - Stores faculty info (name, subject, experience, salary)
  - Calculates faculty salary based on number of students allocated and fee per student
  - Sorts faculty by salary in descending order
- **Usage**: `python faculty.py`

### Data Processing Files

#### `ds.py`
- **Purpose**: Pandas DataFrame operations on student data
- **Features**:
  - Creates DataFrame with 10 student records
  - Calculates mean marks
  - Finds lowest 5 students by marks
  - Sorts students by age
- **Usage**: `python ds.py`

#### `excel.py`
- **Purpose**: Creates Excel file from student data
- **Output**: Generates `students.xlsx`
- **Features**:
  - Creates DataFrame with student info (Name, Age, Marks, Grade)
  - Exports to Excel format without index
- **Usage**: `python excel.py`

#### `pdf.py`
- **Purpose**: Generates PDF file with student information
- **Output**: Generates `students.pdf`
- **Dependencies**: ReportLab library
- **Features**:
  - Creates PDF document
  - Displays student name and marks
- **Usage**: `python pdf.py`
- **Installation**: `pip install reportlab`

### Database Schema Files

#### `database_student.sql`
- **Purpose**: MySQL database schema and initial data
- **Features**:
  - Creates `college_db` database
  - Creates `students` table with fields:
    - `student_id` (Primary Key)
    - `name`
    - `subject`
    - `cgpa`
    - `email_id`
  - Inserts 5 sample student records
- **Usage**: Execute in MySQL/MariaDB: `mysql < database_student.sql`

#### `tempCodeRunnerFile.py`
- **Purpose**: Temporary code testing file (can be ignored)

---

## Installation & Setup

### Prerequisites
- Python 3.x
- pip package manager

### Required Libraries
```bash
pip install pandas
pip install openpyxl  # For Excel support
pip install reportlab  # For PDF generation
```

### For MySQL Database
```bash
# Linux/Mac
mysql < database_student.sql

# Or in MySQL CLI
source database_student.sql
```

---

## Data Used

### Students Table Columns
- **id/student_id**: Unique identifier
- **name**: Student's full name
- **age**: Age of student
- **marks**: Academic marks/score
- **grade**: Letter grade (A++, A+, etc.)
- **cgpa**: Cumulative Grade Point Average
- **email_id**: Student's email address

### Faculty Table Columns
- **name**: Faculty member's name
- **subject**: Subject taught
- **experience**: Years of experience
- **salary**: Calculated based on students allocated and fees
- **students_allocated**: Number of students assigned

---

## Quick Start

```bash
# Run all scripts
python database.py
python ds.py
python excel.py
python pdf.py
python faculty.py

# Check generated files
ls -la *.xlsx *.pdf *.db
```

---

## Sample Output

### database.py Output
```
Original DataFrame:
  id    name  age  marks
0  1   Kunal   20     85
1  2  Monika   21     90
...

Mean of Marks:
80.8
```

### excel.py Output
Creates `students.xlsx` with student data in Excel format

### pdf.py Output
Creates `students.pdf` with student information

---

## Key Concepts Covered

- **SQLite Operations**: Database creation, insertion, querying
- **Pandas DataFrames**: Data manipulation, sorting, filtering
- **File I/O**: Excel export, PDF generation
- **Data Analysis**: Mean calculation, sorting, ranking
- **MySQL Schema**: Table design and data insertion

---

## License

This is a learning project for data science concepts.

---

**Last Updated**: May 2026
