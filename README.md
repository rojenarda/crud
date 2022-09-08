# AWS CRUD PROJECT

Perform operations on two different AWS DynamoDB tables.

## Table 1

 - Table Name: device_serial_table
 - Primary Key: "device_serial"
 - Primary Key Type: string

| Operation | Path |
|--|--|
| Create Item | /device/create |
| Read Item | /device/read |
| Update Item | /device/update |
| Delete Item | /device/delete |
| Get All Items | /device/get_all |

## Table 2

 - Table Name: user_id_table
 - Primary Key: "identity_id
 - Primary Key Type: string

| Operation | Path |
|--|--|
| Create Item | /user/create |
| Read Item | /user/read |
| Update Item | /user/update |
| Delete Item | /user/delete |
| Get All Items | /user/get_all |