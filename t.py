USE [ShoeGalaxy]
GO
DELETE FROM [dbo].[replys] WHERE [username] <> N'Admin';
DELETE FROM [dbo].[comments] WHERE [username] <> N'Admin';
DELETE FROM [dbo].[OrderDetails] 
WHERE [order_id] IN (SELECT [id] FROM [dbo].[Orders] WHERE [username] <> N'Admin');
DELETE FROM [dbo].[Orders] WHERE [username] <> N'Admin';
DELETE FROM [dbo].[ShoppingCarts] WHERE [username] <> N'Admin';
DELETE FROM [dbo].[Addresses] WHERE [account_username] <> N'Admin';
DELETE FROM [dbo].[Authorities] WHERE [username] <> N'Admin';
DELETE FROM [dbo].[Accounts] WHERE [username] <> N'Admin';
GO
EXEC DeleteAccountAndRelatedData N'vietbx23@gmail.com';
EXEC DeleteAccountAndRelatedData N'hieuptps24504@fpt.edu.vn';
EXEC DeleteAccountAndRelatedData N'phamthieu961@gmail.com';
EXEC DeleteAccountAndRelatedData N'nguyenpham242003@gmail.com';
EXEC DeleteAccountAndRelatedData N'vietbxps22788@fpt.edu.vn';
EXEC DeleteAccountAndRelatedData N'XuanViet123';
EXEC DeleteAccountAndRelatedData N'vietbx23@gmail.com';
EXEC DeleteAccountAndRelatedData N'NV01';
EXEC DeleteAccountAndRelatedData N'NV02';
EXEC DeleteAccountAndRelatedData N'asddd';