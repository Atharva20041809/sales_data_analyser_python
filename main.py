from utils import convert_raw, revenue_per_product, Highest_revenue_day, Most_sold_item, Average_order_value

with open('./sales.csv') as file:

    contents = file.readlines()

    original_data = convert_raw(contents)

    print(revenue_per_product(original_data))
    print(Highest_revenue_day(original_data))
    print(Most_sold_item(original_data))
    print(Average_order_value(original_data))

