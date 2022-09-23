#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails
import os


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  most_sales = {"total_sales": 0}
  sales_by_year = {}
  most_popular_year = (0,0)
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item


    # TODO: also handle max sales
    if item["total_sales"] > most_sales["total_sales"]:
        most_sales = item

    # TODO: also handle most popular car_year
    item_car = item['car']
    if item_car["car_year"] not in sales_by_year:
        sales_by_year[item_car["car_year"]] = item["total_sales"]
    else:
        sales_by_year[item_car["car_year"]] += item["total_sales"]
    if sales_by_year[item_car["car_year"]] > most_popular_year[1]:
        most_popular_year = (item_car["car_year"],sales_by_year[item_car["car_year"]])
  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(format_car(most_sales["car"]), most_sales["total_sales"]),
    "The most popular year was {} with {} slaes".format(most_popular_year[0], most_popular_year[1])
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("/home/student-03-c4fdf88b3489/car_sales.json")
  summary = process_data(data)
  print(summary)

  # TODO: turn this into a PDF report
  table_for_pdf = cars_dict_to_table(data)
  pdf_title = "Sales Summary for Last Month"
  pdf_para = ""
  for sentence in summary:
    pdf_para += sentence + "<br/>"
  reports.generate('/tmp/cars.pdf', pdf_title, pdf_para, table_for_pdf)

  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "student-03-c4fdf88b3489@example.com"
  subject = "Sales summary for last month"
  body = pdf_para.replace("<br/>", "\n")
  path_to_attachment = '/tmp/cars.pdf'
  message = emails.generate(sender, receiver, subject, body, path_to_attachment)
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)