import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='2002',database='retail_store')
my_cursor=conn.cursor()

def admincheck(s,p):
    try:
        string="select password from admin where admin_id = %s" %('\''+s+'\'')
        my_cursor.execute(string)
        for i in my_cursor:
            if(i[0]==p):
                return True
        return False
    except Exception as e:
        return False

def customercheck(s,p):
    try:
        string="select password from customer where first_name = %s" %('\''+s+'\'')
        my_cursor.execute(string)
        for i in my_cursor:
            if(i[0]==p):
                return True
        return False
    except Exception as e:
        return False
    
    
def getBrandwiseQuantity() : 
    s = "SELECT coalesce(brand,'All Brands') as Brands, SUM(quantity) as Quantity FROM retail_store.product GROUP BY brand with ROLLUP;"
    my_cursor.execute(s)
    f=my_cursor.fetchall()
    for i in f:
        print(i)
        print("\n")
        
def getCustomerAddressCost() : 
    s="SELECT coalesce(customer_id,'All Customers') as Customers, coalesce(address,'All addresses') as Address, SUM(total_cost) FROM retail_store.orders GROUP BY customer_id,address with ROLLUP;"
    my_cursor.execute(s)
    f=my_cursor.fetchall()
    for i in f:
        print(i)
        print("\n")
                            
def AverageRatingLocalityWise() : 
    s = "SELECT coalesce(Locality,'All Localities') as Locality, AVG(customer_rating) FROM retail_store.distributor GROUP BY (locality) with ROLLUP;"                                          
    my_cursor.execute(s)
    f=my_cursor.fetchall()
    for i in f:
        print(i)
        print("\n")
        
def DistributorWiseTotalCommission() : 
    s = "SELECT coalesce(distributor_id,'All distributors') as DistributorID, coalesce(customer_rating,'All Ratings') as Ratings, coalesce(locality,'All Localities') as Locality, SUM(commission) as TotalCommision from retail_store.distributor GROUP BY distributor_id,customer_rating,locality with ROLLUP;"
    my_cursor.execute(s)
    f=my_cursor.fetchall()
    for i in f:
        print(i)
        print("\n")
        
def embedsql1():
    s="SELECT * FROM retail_store.product where product_rating>=3.7"
    my_cursor.execute(s)
    f=my_cursor.fetchall()
    for i in f:
        print(i)
        print("\n")

    
def embedsql2():
    s="SELECT first_name,Count(first_name) FROM retail_store.customer group by first_name having count(first_name)>1"
    my_cursor.execute(s)
    f=my_cursor.fetchall()
    for i in f:
        print(i)
        print("\n")

def trigger1():
    trigger_sql1 = """
        Insert into customer values(260,'Hade','quinn','ersgvfve','ffs@gmail.com','78494939','8 walmat street');
        USE retail_store;
        drop trigger update1_cart;
        DELIMITER //
        CREATE TRIGGER update1_cart
        AFTER INSERT ON customer
        FOR EACH ROW
        BEGIN
        INSERT INTO CART(quantity,total_cost,bill_details,cart_id) VALUES(0,'0','NULL',new.customer_id);
        END//
        select * from cart
    """
    my_cursor.execute(trigger_sql1)
    

def trigger2():
    trigger_sql2 = """
        Insert into customer values(299,'Hade','quinn','ersgvfve','ffs@gmail.com','78494939','8 walmat street');
        USE retail_store;
        drop trigger update_membership;
        DELIMITER //
        CREATE TRIGGER update_membership
        AFTER INSERT ON customer
        FOR EACH ROW
        BEGIN
        INSERT INTO membership(types,renewal_date,member_id) VALUES ('default','2023-01-01',new.customer_id);
        END//
        select * from membership;
    """
    my_cursor.execute(trigger_sql2)

while True:

    print("***** APNI DUKAAN *****\n")
    print("**LOGIN**\n1) ADMIN\n2) CUSTOMER")
    ch=int(input("Enter as: "))
    if(ch==1):
        print("Enter the admin details")
        name=input("Name: ")
        pas=input("Password: ")
        if(admincheck(name,pas)):
            print("\nWelcome",name)
        else:
            print("Authentication Failed")
            break
    elif(ch==2):
        print("Enter the customer details")
        id=input("User_id: ")
        pas=input("Password: ")
        if(customercheck(id,pas)):
            print("\nWelcome User")
        else:
            print("Authentication Failed")
            break

    print("SELECT THE TYPE OF QUERY TO PERFORM\n1)EMBEDDED QUERY\n2)TRIGGER QUERY\n3)OLAP QUERY\n")
    val = int(input("Enter your selection: "))
    if(val==1):
        print("1) DISPLAYING INFO OF PRODUCTS HAVING RATING GREATER THAN 3.7\n2) DISPLAYING NAME AND COUNT OF CUSTOMERS HAVING SAME FIRST NAME\n")
        print("CHOOSE THE EMBEDDED QUERY\n")
        val1=int(input("Enter 1/2: "))
        if(val1==1):
            embedsql1()
        elif(val1==2):
            embedsql2()
    
    elif(val==2):
        print("1) CREATING A TRIGGER FOR UPDATING CART VALUE \n2) CREATING A TRIGGER FOR UPDATING MEMBERSHIP\n")
        print("CHOOSE THE TRIGGER\n")
        val1=int(input("Enter 1/2: "))
        if(val1==1):
            trigger1()
        elif(val1==2):
            trigger2()
    elif(val==3):
        print("OLAP QUERIES")
        
    else:
        break




conn.close()
