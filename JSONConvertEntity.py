json = {"fuzzy:host_ip": {"type": "string"}, "fuzzy:host_name": {"type": "string"},
        "os_type": {"type": "string"}, "host_group": {"type": "string"},
        "host_tag": {"type": "string"},
        "fuzzy:name": {"type": "string", "description": "Web服务器名称"},
        "name": {"type": "string", "description": "按照名称分组时带上"},
        "fuzzy:service_version": {"type": "string", "description": "版本"},
        "service_version": {"type": "string", "description": "按照版本分组时带上"},
        "fuzzy:dir_path": {"type": "string", "description": "安装路径"},
        "fuzzy:user": {"type": "string", "description": "启动用户"},
        "fuzzy:bin_path": {"type": "string", "description": "二进制文件路径"},
        "fuzzy:conf_path": {"type": "string", "description": "配置文件路径"},
        "umid": {"type": "string", "description": "按照主机分组时带上"}}
# json = input("输入map")
for name in json:
    source = name
    n = name.find(":")
    code = "private "
    status = 0
    if n != -1:
        status = 1
        name = name.replace(":", name[n+1].upper())
        list_str = list(name)
        list_str.pop(n+1)
        list_str = "".join(list_str)
        name = str(list_str)
    m = name.find("_")
    if m != -1:
        status = 1
        name = name.replace("_", name[m + 1].upper())
        list_str = list(name)
        list_str.pop(m+1)
        list_str = "".join(list_str)
        name = str(list_str)
    text = json[source]
    # print(" /**")
    # print("  *")
    # print(" */")
    if status == 1:
        print("@JsonAlias(\""+source+"\")")
    if text["type"] == "string":
        code += "String " + name + ";"
    else:
        print("add :"+text["type"])
    print(code)
    print()
