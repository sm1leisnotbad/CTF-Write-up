# God of gamblers - Vua cờ bịp

Trong bài này, cái khó ở chỗ đoán được giá trị random tạo bởi hàm srand(time(0)) và rand() 

##Bypass rand và srand
```
Enter your bet (or enter 0 to quit): 20
Enter 1 for small or 2 for big: 2
Sorry, you lose $20.
The result is 6 (dice 1: 1, dice 2: 4, dice 3: 1).
Your balance is now $0.
```

Để win được trò chơi thì ta cần đoán tổng 3 xúc sắc nhỏ(3-9) hay lớn(10-18). Từ source code, ta thấy các số được tạo bởi hàm rand().
```C
dice1 = rand() % 6 + 1;
dice2 = rand() % 6 + 1;
dice3 = rand() % 6 + 1;
points = dice1 + dice2 + dice3;
```
Và seed là time(0).
![image](https://github.com/sm1leisnotbad/CTF-Write-up/assets/90888568/2d7bd27a-4002-432e-b424-450f2118280a)

Ta chỉ cần code lại phần này là được


##Bypass buffer overflow

Phần này, chall yêu cầu ta phải đoán số random từ /dev/urandom. Việc này gần như là không thể.
![image](https://github.com/sm1leisnotbad/CTF-Write-up/assets/90888568/045c0c3e-bd71-48f0-a3f9-15b5c06966b8)

Khi để ý code phần code ở dưới, hàm này sử dụng scanf("%s",v1) và so sánh v1 với số random. 
Vì scanf("%s") không giới hạn độ dài của chuỗi nhập vào nên bằng việc nhập vào v1 ta có thể ghi đè vào bến ptr. Ta chỉ cần nhập 16 byte giống nhau là có được flag
![image](https://github.com/sm1leisnotbad/CTF-Write-up/assets/90888568/95424fbb-dc40-4677-8217-d93c731692fd)


