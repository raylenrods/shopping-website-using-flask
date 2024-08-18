use FlaskProject;


desc Products;
desc users;
 
select * from products,cart where products.id=cart.product_id;

CREATE TABLE Users (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(30) NOT NULL,
    dob date NOT NULL,
    gender VARCHAR (30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    passwd Varchar (50) NOT NULL,
    mobile VARCHAR(20) NOT NULL
);