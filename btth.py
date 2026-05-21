# bước 1: nhập số lượng nhân viên và bắt lỗi input
# bước 2: xử lý thông tin theo từng nhân viên
    # nhánh: lặp qua từng nhân viên -> nhập tên -> nhập số ngày làm
    # nhánh: kiểm tra ngày làm hợp lệ (< 0 hoặc > 22) -> Báo lỗi & continue
    # nhánh: kiểm tra ngày làm == 0 -> In thông báo nghỉ toàn bộ
    # nhánh: in biểu đồ dấu * bằng nested loop
    # nhánh: đánh giá mức độ làm việc

employee_quantity = input("Nhập số lượng nhân viên: ")
while True:
    try:
        employee_quantity = int(employee_quantity)
        if employee_quantity <= 0:
            raise Exception()
        break
    except:
        employee_quantity = input("Không hợp lệ, nhập lại: ")

for employee in range(1, employee_quantity + 1):
    print()
    employee_name = input("Nhập tên nhân viên: ")
    work_days = input("Nhập số ngày làm: ")
    
    while True:
        try:
            work_days = int(work_days)
            break
        except:
            work_days = input("Không hợp lệ, nhập lại: ")

    if work_days < 0 or work_days > 22:
        print("Dữ liệu không hợp lệ")
        continue

    if work_days == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
        continue

    print(f"{employee_name}: ", end="")
    for star in range(1, work_days + 1):
        print("*", end="")
    print() 

    if work_days >= 18:
        work_status = "Làm việc chăm chỉ"
    elif work_days < 10:
        work_status = "Làm việc ít"
    else:
        work_status = "Làm việc bình thường"
        
    print(work_status)