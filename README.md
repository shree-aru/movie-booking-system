# Movie Booking System Database

## 1. Introduction

## 2. Features

## 3. Installation

## 4. Usage

## 5. Technologies Used

## 6. Project Structure

## 7. Contributing

## 8. Contact


### 1.1 Problem Statement
The modern entertainment industry, particularly cinema, relies heavily on efficient and robust booking systems to manage operations, enhance customer experience, and optimize resource allocation. A core component of such systems is a well-structured database capable of handling real-time transactions, maintaining accurate records of available seats, mapping showtimes to specific theaters, and managing customer information. Without a reliable and scalable database, movie booking operations can quickly become chaotic, leading to issues such as overbooking, scheduling conflicts, and poor customer satisfaction. The challenge lies in designing a relational database that can accurately reflect the complex interdependencies between movies, shows, theaters, seats, customers, and their bookings, while ensuring data integrity and transactional consistency.

### 1.2 Project Objective
This project aims to design and implement a relational database for a comprehensive movie booking system. The primary objective is to create a robust backend infrastructure capable of managing all essential entities involved in the movie booking process. This includes defining clear relationships between theaters, movie shows, individual seats, customer profiles, and booking transactions. The database will be built using MySQL, a widely adopted open-source relational database management system, ensuring a solid foundation for future application development and scalability.

### 1.3 Expected Outcome
The expected outcome of this project is a fully functional MySQL database schema, complete with defined tables, appropriate data types, primary and foreign key constraints, and sample data. This database will serve as the foundational backend for a hypothetical movie booking application, demonstrating the ability to:
*   Store and retrieve information about various theaters, including their names, locations, and seating capacities.
*   Manage details of movie shows, such as movie titles, associated theaters, showtimes, and ticket prices.
*   Track the availability and status of individual seats within each theater.
*   Maintain customer records, including personal details and contact information.
*   Record booking transactions, linking customers to specific shows and seats.

The project will also include comprehensive documentation, presented in this README.md file, detailing the database design, installation instructions, usage guidelines, and verification steps. This documentation is crafted to meet professional standards, suitable for academic portfolios and collaborative development environments.


## 2. Features

The Movie Booking System Database is designed to provide a robust and scalable backend for managing all aspects of a cinema booking operation. Its key features include:

### 2.1 Comprehensive Entity Management
The database effectively manages core entities crucial for a movie booking system:
*   **Theatres:** Stores details about each cinema location, including its name, physical address, and total seating capacity.
*   **Shows:** Manages information about individual movie screenings, such as the movie title, the theatre where it's being shown, the specific showtime, and the ticket price.
*   **Seats:** Tracks every seat within each theatre, including its unique identifier, seat number, and current availability status. This allows for real-time seat tracking and prevents overbooking.
*   **Customers:** Maintains a record of customer profiles, including their first name, last name, unique email address, and phone number. This enables personalized booking experiences and communication.
*   **Bookings:** Records each transaction where a customer reserves a seat for a specific show. It links customers, shows, and seats, and logs the booking timestamp.

### 2.2 Relational Integrity
The database schema is designed with strong relational integrity, utilizing primary and foreign keys to establish clear relationships between tables. This ensures data consistency and prevents orphaned records. For instance:
*   A `Show` is always linked to an existing `Theatre`.
*   A `Booking` always references a valid `Customer`, `Show`, and `Seat`.

### 2.3 Real-time Seat Availability
The `Seats` table includes an `is_available` flag, which is updated in real-time upon booking or cancellation. This critical feature ensures that the booking system accurately reflects the current seating status, preventing double-bookings and providing an accurate view of available seats to customers.

### 2.4 Scalability and Performance
Designed with scalability in mind, the database structure is optimized for efficient data retrieval and storage. Proper indexing on frequently queried columns (e.g., `theatre_id`, `show_id`, `customer_id`) can further enhance performance as the volume of data grows.

### 2.5 Data Consistency
Through the use of appropriate data types and constraints (e.g., `NOT NULL`, `UNIQUE`), the database enforces data consistency, ensuring that only valid and meaningful data is stored. This minimizes errors and improves the reliability of the booking system.

### 2.6 MySQL Implementation
The entire database is implemented using MySQL, a robust and widely-used open-source relational database management system. This choice provides a stable, high-performance, and secure environment for the movie booking system's data. The SQL scripts provided are compatible with standard MySQL installations.


## 3. Installation

To set up the Movie Booking System Database on your local machine, follow these steps:

### 3.1 Prerequisites
Ensure you have the following installed on your system:
*   **MySQL Server:** The database backend. You can download it from the official MySQL website or install it via your operating system's package manager.
    *   For Ubuntu/Debian:
        ```bash
        sudo apt-get update
        sudo apt-get install -y mysql-server mysql-client
        ```
*   **Python 3.x:** Required to run the verification script and potentially interact with the database programmatically.
*   **pip:** Python's package installer.

### 3.2 Install MySQL Python Connector
To allow Python scripts to interact with your MySQL database, you need to install the `mysql-connector-python` library:

```bash
pip install mysql-connector-python
```

### 3.3 Configure MySQL (Optional but Recommended for Local Development)
By default, MySQL root user might require a password or specific authentication methods. For local development and ease of use, you might want to configure the root user for passwordless login or set a simple password. **Note: This is not recommended for production environments.**

To allow passwordless login for the `root` user from `localhost` (common in development environments):

```bash
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY ''; FLUSH PRIVILEGES;"
```

If you encounter `Access denied` errors, ensure your MySQL server is running and you have the necessary permissions. You might need to start the MySQL service:

```bash
sudo service mysql start
```

### 3.4 Clone the Repository (if applicable)
If you are getting this project from a version control system like GitHub, clone the repository:

```bash
git clone https://github.com/shree-aru/movie-booking-system.git
cd movie-booking-database
```

If you have downloaded the project as an archive, simply extract it and navigate into the project directory.


## 4. Usage

Once the prerequisites are met and the project files are in place, you can set up and interact with the movie booking database.

### 4.1 Creating the Database and Tables
Navigate to the project directory in your terminal. The `schema.sql` file contains the SQL commands to create the `movie_booking_db` database and all necessary tables (Theatres, Shows, Seats, Customers, Bookings).

Execute the schema script using the MySQL client:

```bash
sudo mysql < schema.sql
```

This command will create the database and define the table structures within your MySQL server.

### 4.2 Populating with Sample Data
The `data.sql` file contains SQL `INSERT` statements to populate the newly created tables with sample data. This data is useful for testing and demonstrating the database functionality.

Execute the data script using the MySQL client:

```bash
sudo mysql < data.sql
```

This will insert sample theatres, shows, seats, customers, and booking records into your database.

### 4.3 Verifying Database Structure and Data
To confirm that the database and tables have been created correctly and populated with data, you can use the `verify_db.py` Python script. This script connects to the MySQL database, describes the table structures, and queries data from each table to display its contents.

Run the verification script from your terminal:

```bash
python verify_db.py
```

The output in your terminal will show:
*   The schema (columns and their types) for each table.
*   The data currently stored in the `Theatres`, `Shows`, `Customers`, and `Bookings` tables.
*   A list of seats that have been marked as booked (`is_available = FALSE`).

This verification step ensures that your database is set up as expected and ready for integration with an application.


## 5. Technologies Used

This project utilizes the following technologies and tools:

*   **MySQL:** The chosen Relational Database Management System (RDBMS) for storing and managing all booking-related data. MySQL is a popular open-source database known for its reliability, performance, and ease of use.
*   **SQL (Structured Query Language):** Used for defining the database schema (DDL - Data Definition Language) and populating/manipulating data (DML - Data Manipulation Language).
*   **Python 3.x:** Employed for scripting database interactions, particularly for verification and programmatic data access. Python's simplicity and extensive library ecosystem make it ideal for such tasks.
*   **`mysql-connector-python`:** The official MySQL driver for Python, enabling Python applications to connect to and interact with MySQL databases. This library facilitates executing SQL queries and fetching results within Python scripts.

These technologies collectively provide a robust and efficient foundation for the movie booking system's backend database.


## 6. Project Structure

The project directory is organized as follows:

```
movie_booking_database/
├── schema.sql
├── data.sql
├── verify_db.py
└── README.md
└── todo.md
```

*   `schema.sql`: Contains the SQL commands for creating the `movie_booking_db` database and all its tables (Theatres, Shows, Seats, Customers, Bookings).
*   `data.sql`: Contains SQL `INSERT` statements to populate the database with sample data for testing and demonstration purposes.
*   `verify_db.py`: A Python script used to connect to the MySQL database, verify the table structures, and display the inserted sample data.
*   `README.md`: This comprehensive document providing an overview of the project, its features, installation, usage, and technical details.
*   `todo.md`: A markdown file used for tracking the project's development progress and outstanding tasks.


## 7. Contributing

Contributions to this project are welcome! If you have suggestions for improvements, new features, or bug fixes, please consider:

1.  **Forking the repository.**
2.  **Creating a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name` or `bugfix/your-bug-name`.
3.  **Making your changes** and ensuring they adhere to the existing code style.
4.  **Writing clear, concise commit messages.**
5.  **Pushing your branch** to your forked repository.
6.  **Opening a Pull Request** to the `main` branch of this repository, describing your changes in detail.

Your contributions will help enhance this database solution for movie booking systems!


## 8. Contact

For any inquiries or further information regarding this project, please feel free to reach out.

---

