def convert_raw(raw_data):

    original_data = []

    length_of_raw_data = len(raw_data)

    for i in range(1,length_of_raw_data):

        current_line = raw_data[i].strip().split(",")

        current_item = {
            "Product":current_line[0],
            "Quantity":int(current_line[1]),
            "Price": int(current_line[2]),
            "Date":current_line[3],
            "Total": int(current_line[4])
        }

        original_data.append(current_item)
    
    return original_data

def revenue_per_product(all_products):
    return [{"Product":x['Product'],"Total_revenue": x["Total"]} for x in all_products]

def Highest_revenue_day(all_products):
    Max_revenue = max([x["Total"] for x in all_products])
    return [x["Date"] for x in all_products if x["Total"]==Max_revenue]

def Most_sold_item(all_products):
    return [x["Product"] for x in all_products if x['Quantity']==(max([y["Quantity"] for y in all_products]))]

def Average_order_value(all_products):
    return sum([x["Price"] for x in all_products])/len(all_products)

