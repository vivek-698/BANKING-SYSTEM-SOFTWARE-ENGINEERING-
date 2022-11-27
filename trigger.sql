delimiter @@

create trigger upd_bal
AFTER insert
on transactions
for each row
begin
	if new.TransactionType = "Deposit" THEN
		UPDATE banksystem.cust SET Balance = Balance + new.Amount where cust.ID = new.CustID;
    END if;
    if new.TransactionType = "Withdraw" THEN
		UPDATE banksystem.cust SET Balance = Balance - new.Amount where cust.ID = new.CustID;
    END if;
end
@@

delimiter ;	