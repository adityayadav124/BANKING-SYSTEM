import mysql.connector
mybd=mysql.connector.connect(host='127.0.0.1',
                             port='3306',
                             user='root',
                             password='1234',
                             database='BMS')
def Openacc():
    name=input('Enter the customer name:')
    accno=input('Enter the acc/no:')
    dob=input('Enter the dob:')
    add=input('Enter the address:')
    cont_no=int(input('Enter the contact No:'))
    Open_bal=int(input('Enter the balance:'))
    data1=(name,accno,dob,add,cont_no,Open_bal)
    data2=(name,accno,Open_bal)
    sql1=('insert into bms values(%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    x=mybd.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mybd.commit()
    print("Data entered Sucessfully")
    main()
def Depoacc():
    amount=input('Enter the amount you want to deposit:')
    ac=input('Enter the account no:')
    a='select bal from amount where Accno=%s'
    data=(ac,)
    x=mybd.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+int(amount)
    sql=('update amount set bal=%s where Accno=%s')
    sql1 =('update bms set openbal=%s where accno=%s')
    d=(t,ac)
    d2=(t,ac)
    x=mybd.cursor()
    x.execute(sql,d)
    x.execute(sql1,d2)
    mybd.commit()
    main()
def WithdrawAmount():
    amount = input ('Enter the amount you want to withdraw:')
    ac = input ('Enter the account no:')
    a = 'select bal from amount where Accno=%s'
    data = (ac,)
    x = mybd.cursor ()
    x.execute (a, data)
    result = x.fetchone()
    if result[0]<int(amount):
        print("Not enough balance")
        main()
    else:
        t = result [0]-int (amount)
        sql = ('update amount set bal=%s where Accno=%s')
        sql1 = ('update bms set openbal=%s where accno=%s')
        d = (t, ac)
        d2 = (t, ac)
        x = mybd.cursor ()
        x.execute (sql, d)
        x.execute (sql1, d2)
        mybd.commit ()
        print("Current balance:",t)
        main ()

def main():
    print('''
    1.open new account
    2.Deposit amount
    3.Withdraw amount
    4.Balance enquiry
    5.Display customer details
    6.close an account 
    ''')
    choice=input("Enter the task you want to perform")
    if choice=='1':
        Openacc()
    elif choice=='2':
        Depoacc()
    elif choice=='3':
        WithdrawAmount()
    """elif choice=='4':
        displaybalance()
    elif choice=='5':
        Displaycustomer()
    elif choice=='6':
        Closeaccount()
    else:
        print("Wrong input")
        main()"""

main()