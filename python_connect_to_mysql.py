import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='2002',database='retail_store')
my_cursor=conn.cursor()

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
        USE retail_store;
        DELIMITER //
        CREATE TRIGGER update2_cart
        AFTER INSERT ON customer
        FOR EACH ROW
        BEGIN
            INSERT INTO cart (customer_id) VALUES (NEW.customer_id);
        END//
    """
    my_cursor.execute(trigger_sql1)
    

def trigger2():
    trigger_sql2 = """
        USE retail_store;
        DELIMITER //
        CREATE TRIGGER update_membership
        AFTER INSERT ON customer
        FOR EACH ROW
        BEGIN
            INSERT INTO membership (customer_id) VALUES (NEW.customer_id);
        END//
    """
    my_cursor.execute(trigger_sql2)

while True:

    print("***** APNI DUKAAN *****\n")
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
