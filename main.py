# từ thư viện random thêm vào hàm randint
from random import randint

print("Nhap keo bua bao:")

# tạo biến computer có giá trị là random số từ 1 đến 3
computer = randint (1,3)

# nhập dữ liệu từ tôi
player = input()


# Nếu computer bằng 1 thì computer có giá trị keo>
if computer == 1:
    computer = "keo"

# Nếu computer bằng 2 thì computer có giá trị bao
if computer == 2:
    computer = "bua"

if computer == 3:
    computer = "bao"

print("---")
print("you choose: " + player)
print("computer choose: " + computer)
print("---")

# Nếu player bằng keo thì
if player == "keo":
    # Nếu computer bằng keo thì in Hoa
    if computer == "keo":
        print("Hoa")
    # Nếu computer bằng bua thì in Thua
    if computer == "bua":
        print("Thua")
    if computer == "bao":
        print("Thang")

if player == "bua":
    if computer == "keo":
        print("Thang")
    if computer == "bua":
        print("Hoa")
    if computer == "bao":
        print("Thua")

if player == "bao":
    if computer == "keo":
        print("Thua")
    if computer == "bua":
        print("Thang")
    if computer == "bao":
        print("Hoa")

