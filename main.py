

def process_data(list_of_dict_of_cars):
    most_revenue = ('model', 0)
    most_sales = ('model' , 0)
    sales_by_year = {}
    most_popular_year = (0, 0) #(year, total_sales)
    for car in list_of_dict_of_cars:

        # Find car with the most revenue (price * total sales)
        revenue = car['price'] * car['total_sales']
        if revenue > most_revenue[1]:
            most_revenue = (car['car_model'], revenue)

        # Find car with the most sales: "The {car model} had the most sales: {total sales}"
        if car['total_sales'] > most_sales[1]:
            most_sales = (car['car_model'], car['total_sales'])

        # Calculate the most popular car_year across all car make/models: "The most popular year was {year} with {total sales in that year} sales."
        if car['year'] not in sales_by_year:
            sales_by_year[car['year']] = car['total_sales']
        else:
            sales_by_year[car['year']] += car['total_sales']

        if sales_by_year[car['year']] > most_popular_year[1]:
                most_popular_year = (car['year'], sales_by_year[car['year']])

        return {
            'most_revenue' : most_revenue,
            'most_sales' : most_sales,
            'most_popular_year' : most_popular_year,
        }

# Generate PDF:
    # reports.generate(filename, title, addittional_info, table_data)
    # filename = /tmp/carsreport.pdf
    # title =
    # addittional_info =
    # table_data = cars_dict_to_table(___)


#Email:
    #emails.generate(sender, recipient, subject, body, attachment_path)

    #emails.send(message)
