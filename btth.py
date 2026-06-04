
blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]

def find_bag_index(inventory, bag_id):

    clean_id = bag_id.strip().upper()
    for i in range(len(inventory)):
        if inventory[i].startswith(clean_id + "-"):
            return i
    return -1


def display_inventory(inventory):

    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    print(f"{'Mã Túi':<7} | {'Người Hiến':<16} | {'Nhóm Máu':<8} | {'Thể Tích':<8} | Ngày Hết Hạn")

    
    total_volume = 0
    for bag in inventory:
        parts = bag.split("-")
        bag_id = parts[0]
        donor = parts[1]
        blood_type = parts[2]
        volume = int(parts[3])
        expiry = parts[4]
        
        total_volume += volume
        print(f"{bag_id:<7} | {donor:<16} | {blood_type:<8} | {volume:<4} ml  | {expiry}")
        

    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


def add_blood_bag(inventory):

    bag_id = input("Nhập mã túi máu mới: ").strip()
    if len(bag_id) == 0:
        print("Lỗi: Mã túi máu không được để trống!")
        return
    
    if find_bag_index(inventory, bag_id) != -1:
        print(f"Lỗi: Mã túi máu {bag_id.upper()} đã tồn tại! Vui lòng nhập mã khác.")
        return

    donor = input("Nhập tên người hiến: ").strip()
    if len(donor) == 0:
        print("Lỗi: Tên người hiến không được để trống!")
        return

    blood_type = input("Nhập nhóm máu: ").strip()
    volume_str = input("Nhập thể tích (ml): ").strip()

    if not volume_str.isdigit() or int(volume_str) <= 0:
        print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return
        
    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()
    if len(expiry) == 0:
        print("Lỗi: Ngày hết hạn không được để trống!")
        return

    final_id = bag_id.upper()
    final_donor = donor.title()
    final_blood_type = blood_type.upper()
    final_volume = volume_str 
    final_expiry = expiry

    new_bag_record = "-".join([final_id, final_donor, final_blood_type, final_volume, final_expiry])
    inventory.append(new_bag_record)
    print(f"Thành công: Đã nhập túi máu {final_id} vào kho!")


def update_expiry(inventory):

    bag_id = input("Nhập mã túi máu cần cập nhật: ").strip()
    
    if len(bag_id) == 0:
        print("Lỗi: Mã túi máu không được để trống!")
        return
        
    index = find_bag_index(inventory, bag_id)
    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {bag_id.upper()} trong kho!")
        return
        
    new_expiry = input("Nhập ngày hết hạn mới: ").strip()
    if len(new_expiry) == 0:
        print("Lỗi: Ngày hết hạn mới không được để trống!")
        return

    parts = inventory[index].split("-")
    parts[4] = new_expiry
    
    inventory[index] = "-".join(parts)
    print(f"Thành công: Đã cập nhật ngày hết hạn cho túi máu {parts[0]}!")


def remove_blood_bag(inventory):
    bag_id = input("Nhập mã túi máu cần xuất/hủy: ").strip()
    
    if len(bag_id) == 0:
        print("Lỗi: Mã túi máu không được để trống!")
        return
        
    index = find_bag_index(inventory, bag_id)
    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {bag_id.upper()} trong kho!")
        return

    actual_id = inventory[index].split("-")[0]
    inventory.pop(index)
    print(f"Thành công: Đã xuất túi máu {actual_id} khỏi kho!")


while True:
        print("=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        match choice:
            case "1":
                display_inventory(blood_inventory)
            case "2":
                add_blood_bag(blood_inventory)
            case "3":
                update_expiry(blood_inventory)
            case "4":
                remove_blood_bag(blood_inventory)
            case "5":
                print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
                break
            case _:
                print("\nLựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
