def making_ll(data):
    ll=''
    ll+=str(data) + "-->"
    return ll


def insert_data_at_start(data, ll):
    ll = str(data) + "-->" + ll
    return ll

ll1 = making_ll(12)
ll1 = insert_data_at_start(9, ll1)
ll1 = insert_data_at_start(6, ll1)
ll1 = insert_data_at_start(3, ll1)


print(ll1)
