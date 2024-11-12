#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:39:37 2024

@author: vaibhav
"""

# import calendar

# # Function to display the calendar for a given month and year
# def generate_calendar(year, month):
#     # Create a text calendar object
#     cal = calendar.TextCalendar(calendar.SUNDAY)
    
#     # Display the calendar
#     calendar_output = cal.formatmonth(year, month)
#     print(calendar_output)

# # Input: Year and Month
# year = int(input("Enter year: "))
# month = int(input("Enter month (1-12): "))

# # Generate and display the calendar
# generate_calendar(year, month)


# 2. Calendar Generator
import calendar

def generate_calendar(year, month):
    return calendar.month(year, month)


