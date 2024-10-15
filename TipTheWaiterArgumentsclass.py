def total_calc(bill_amount, tip_perc):

    total = bill_amount* (1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")


total_calc(150,20)
total_calc(1098,40)
total_calc(2234,50)
total_calc(342,23)