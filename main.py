

def process_data(list_of_dict_of_cars):
    most_revenue = ('model', 0)
    most_sales = ('model' , 0)
    sales_by_year = {}
    most_poplar_year = (0, 0) #(year, total_sales)
    for car in list_of_dict_of_cars:

        # Find car with the most revenue (price * total sales)
        revenue = car['price'] * car['total_sales']
        if revenue > most_revenue[1]:
            most_revenue = (car['car_model'], revenue)

        # Find car with the most sales: "The {car model} had the most sales: {total sales}"
        if car['total_sales'] > most_sales[1]:
            most_sales = (car['car_model'], car['total_sales'])

        # Calculate the most popular car_year across all car make/models: "The most popular year was {year} with {total sales in that year} sales."