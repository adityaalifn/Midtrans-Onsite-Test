transactions = [
    {"id":1, "email":"e1", "phone":"p1", "card":"c1"},
    {"id":2, "email":"e2", "phone":"p2", "card":"c2"},
    {"id":3, "email":"e1", "phone":"p3", "card":"c3"},
    {"id":4, "email":"e4", "phone":"p4", "card":"c4"}    
]

costumers = []

def getCostumerIndex(transaction):
    for costumer in costumers:
        if transaction["email"] in costumer["emails"] or transaction["phone"] in costumer["phones"] or transaction["card"] in costumer["cards"]:
            # print(costumer)
            return costumers.index(costumer)

def parseTransaction(transaction):
    costumer_index = getCostumerIndex(transaction)
    if costumer_index == None:
        costumers.append({"transactions":[transaction["id"]], "emails":[transaction["email"]], "phones":[transaction["phone"]], "cards":[transaction["card"]]})
    else:
        costumers[costumer_index]["transactions"].append(transaction["id"])
        costumers[costumer_index]["emails"].append(transaction["email"])
        costumers[costumer_index]["phones"].append(transaction["phone"])
        costumers[costumer_index]["cards"].append(transaction["card"])

def showCostumerSummary():
    for idx, costumer in enumerate(costumers):
        print("costumer", idx+1)
        print(" transactions: " + str(costumer["transactions"]))
        print(" emails: " + str(costumer["emails"]))
        print(" phones: " + str(costumer["phones"]))
        print(" cards: " + str(costumer["cards"]))
        

if __name__ == '__main__':
    # parse existing transaction
    for transaction in transactions:
        parseTransaction(transaction)
    
    # incoming transaction
    while True:
        showCostumerSummary()
        try:
            transaction = { k : v for k, v in input().split() } 

        except:
            print("Wrong transaction input format\n")
