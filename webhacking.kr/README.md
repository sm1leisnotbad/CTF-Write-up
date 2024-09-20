# Webhacking.kr hint solution

## challenge-01
This challenge passes when cookie `user_lv` >3 and <=4. Changing value of this cookie into a float number like 3.1 or sth...
![image](https://github.com/user-attachments/assets/4d80485d-485c-483c-a346-2392737bab08)

## challenge-24
We need to find a way to make $ip = "127.0.0.1".
The code has some filters which is `str_replace` but it's not hard to find a string to pass this.
I found `17.277...00...00...1`. Then set the `REMOTE_ADDR` cookie value is that string to pass.
![image](https://github.com/user-attachments/assets/46b4d529-ed6e-41f1-92ae-d465fe5b1ec0)

## challenge-17
Use deobsfucator of js

#challenge-

