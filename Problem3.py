test_cases = [
    {"phone":"-", "normalized_phone":"-"},
    {"phone":"+6282214119550", "normalized_phone":"6282214119550"},
    {"phone":"+1 (804) 244-3470", "normalized_phone":"18042443470"},
    {"phone":"+62-081377229637", "normalized_phone":"6281377229637"},
    {"phone":"(021) 5736789", "normalized_phone":"62215736789"},
    {"phone":"0", "normalized_phone":"0"},
    {"phone":"+1 917 856 9984", "normalized_phone":"19178569984"}
]

for case in test_cases:
    phone = case["phone"]
    phone = phone.replace(" ", "")
    phone = phone.replace("*", "")
    phone = phone.replace("+", "")
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")
    phone = phone.replace(".", "")
    phone = phone.replace("?", "")
    
    
    if len(phone) > 1:
        phone = phone.replace("-", "")
        
        if (phone[0:2] == "62" and phone[2] == "0"):
            phone = phone[0:2] + phone [3:]
        
        if (phone[0] == "0"):
            phone = "62" + phone[1:]
        
    print(phone)