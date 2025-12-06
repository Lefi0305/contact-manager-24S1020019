def search_contact():
    name = input("Nhập tên cần tìm: ")

    found = False
    for contact in phonebook:
        if contact['name'].lower() == name.lower():
            print(f"Đã tìm thấy: {contact['name']} - {contact['phone']}")
            found = True
            break
    
    if not found:
        print("Không tìm thấy liên hệ.")
