from resources import bank_account as ba

ac1 = ba('Ali', 100001, 2300)
ac2 = ba('Ahmed', 100002)

ac1.transfer(300, ac2)
ac2.print_slip()


