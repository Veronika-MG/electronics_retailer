def get_node_level(obj):
    if obj.is_root():
        return "Завод"
    if obj.is_leaf():
        return "ИП"
    return "Розничная сеть"
