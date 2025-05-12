# key - value

# 41 => kocaeli 
# 34 => istanbul

# dictionary bilmiyor olsaydık
# sehirler = ["kocaeli","istanbul"]
# plakalar = [41,34]
# print(plakalar[sehirler.index("istanbul")])

#print(plakalar["kocaeli"]) => 41 değerine götürmesi için dictionary kullanırız.

plakalar = {"kocaeli" : 41, "istanbul" : 34 }
print(plakalar["kocaeli"])
print(plakalar["istanbul"])

plakalar["ankara"] = 6 # ankara ve plakasını plakalara ekledik.
print(plakalar)

plakalar["kocaeli"] = "new value" # var olan eşleşmeyi değiştirdik.
print(plakalar)

users = { 
"sadikturan": {
    "age":36,
    "roles":["user"],
    "email":"sadik@gmail.com",
    "address":"kocaeli",
    "phone":"5432356322"
    },
"kemaldaysal": {
    "age":19,
    "roles":["admin","user"],
    "email":"kemal@hotmail.com",
    "address":"edirne",
    "phone":"5323523523"
    }
}

print(users["kemaldaysal"]["age"])
print(users["kemaldaysal"]["email"])
print(users["kemaldaysal"]["address"])
print(users["kemaldaysal"]["phone"])
print(users["sadikturan"]["roles"])
print(users["kemaldaysal"]["roles"])

