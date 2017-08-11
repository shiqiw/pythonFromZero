exempt = 6300

fed_rate = 0.28
fed_limit = 91150
fed_tax = 18558.75

state_lv1_rate = 0.0125
state_lv1_limit = 7060
state_lv2_rate = 0.0225
state_lv2_limit = 16739

def washington(income):
    income = income*1.18*(1-0.15-0.18)

    total = (income-exempt-fed_limit)*fed_rate+fed_tax
    income -= total

    return income

def california(income):
    income = income*1.10*(1-0.15-0.18)

    total = (income-exempt-fed_limit)*fed_rate+fed_tax
    total += state_lv1_limit*state_lv1_rate
    total += (income-state_lv1_limit)*state_lv2_rate

    income -= total
    return income

def main():
    print "Washington:"
    print washington(128000)
    print "California:"
    print california(145000)

main()


